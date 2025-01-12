# src/apps/common/middlewares.py

import logging
from django.db import connections
from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.urls import (
    resolve,
    Resolver404,
)
from django.utils.deprecation import MiddlewareMixin
import json
from typing import Callable
import elasticapm


logger = logging.getLogger(__name__)

class DBLoggingMiddleware(MiddlewareMixin):
    """
    Middleware to log all database queries executed during a request,
    including which database (alias) was used and the type of operation.
    """

    def process_request(self, request):
        """
        Clears existing queries at the start of the request to ensure
        only queries from the current request are logged.
        """
        for alias in connections:
            conn = connections[alias]
            conn.queries.clear()  # Correctly clear the queries list

    def process_response(self, request, response):
        """
        Logs all database queries executed during the request.
        """
        user = getattr(request, 'user', None)
        username = user.username if user and user.is_authenticated else 'Anonymous'

        for alias in connections:
            conn = connections[alias]
            if conn.queries:
                logger.debug(f"\n=== DB Queries for alias '{alias}' by user '{username}' ===")
                for query in conn.queries:
                    sql = query['sql']
                    duration = float(query.get('time', 0))
                    operation = self.get_sql_operation(sql)
                    if self.is_sensitive(sql):
                        sql = '[REDACTED SENSITIVE QUERY]'
                    logger.debug(
                        f"[{alias}] {operation} | Duration: {duration:.3f}s | User: {username}\n{sql}"
                    )
        return response

    def get_sql_operation(self, sql):
        """
        Extracts the SQL operation (SELECT, INSERT, UPDATE, DELETE, etc.)
        from the SQL statement.
        """
        sql = sql.strip().lower()
        if sql.startswith('select'):
            return 'SELECT'
        elif sql.startswith('insert'):
            return 'INSERT'
        elif sql.startswith('update'):
            return 'UPDATE'
        elif sql.startswith('delete'):
            return 'DELETE'
        elif sql.startswith('create'):
            return 'CREATE'
        elif sql.startswith('alter'):
            return 'ALTER'
        elif sql.startswith('drop'):
            return 'DROP'
        elif sql.startswith('commit'):
            return 'COMMIT'
        elif sql.startswith('begin'):
            return 'BEGIN'
        else:
            return 'OTHER'

    def is_sensitive(self, sql):
        """
        Determines if a SQL query contains sensitive information.
        """
        sensitive_keywords = ['password', 'credit_card', 'ssn']
        sql_lower = sql.lower()
        return any(keyword in sql_lower for keyword in sensitive_keywords)


class ElasticApmMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self._client = elasticapm.get_client()

    def __call__(self, request: HttpRequest) -> HttpResponse:
        transaction_name = self._create_transaction_name(request)
        self._start_new_transaction(transaction_name)

        try:
            response = self.get_response(request)
        except Exception as e:
            self._client.end_transaction(transaction_name, "500")
            raise

        if response.status_code == 502:
            elasticapm.capture_message("Got 502 response in Django", level="warning")

        self._client.end_transaction(transaction_name, str(response.status_code))

        self._set_response_body_for_apm(response)

        return response

    def _start_new_transaction(self, transaction_name: str) -> None:
        elasticapm.instrument()
        self._client.begin_transaction("request")
        elasticapm.set_transaction_name(transaction_name)

    def _set_response_body_for_apm(self, response: HttpResponse) -> None:
        try:
            response_body_unicode = response.content.decode("utf-8")
            response_body = json.loads(response_body_unicode)
        except json.JSONDecodeError:
            response_body = response.content
        except AttributeError:
            response_body = ""
        elasticapm.set_context(data={"response_body": response_body})

    def _create_transaction_name(self, request: HttpRequest) -> str:
        try:
            current_url = resolve(request.path_info).route
        except Resolver404:
            current_url = request.path
        return f"{request.method} {current_url}"