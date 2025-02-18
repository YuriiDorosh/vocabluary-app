from django.contrib import admin
from django.urls import include, path, re_path
from django.http import HttpResponse
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# TODO TEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMP

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from motor.motor_asyncio import AsyncIOMotorClient

# Той самий серіалізатор
from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    value = serializers.IntegerField()

class AsyncDataAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Підключення до MongoDB один раз при ініціалізації класу
        self.client = AsyncIOMotorClient(settings.MONGO_URI)
        self.db = self.client["test_db"]
        self.collection = self.db["test_collection"]

    async def post(self, request):
        print("Отримано запит:", request.data)
        serializer = DataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        document = serializer.validated_data
        print("Дані для вставки:", document)
        result = await self.collection.insert_one(document)
        print("ID вставленого документа:", result.inserted_id)

        created_document = await self.collection.find_one({"_id": result.inserted_id})
        created_document["_id"] = str(created_document["_id"])  # Конвертуємо ObjectId -> рядок
        print("Вставлений документ:", created_document)

        return Response(created_document, status=status.HTTP_201_CREATED)



# from django.conf import settings
# from rest_framework import serializers, viewsets, permissions
# from rest_framework.response import Response
# from rest_framework.decorators import action
# import motor.motor_asyncio
# import asyncio

# # Підключення до MongoDB
# client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
# db = client.get_database("test_db")
# collection = db.get_collection("test_collection")

# # Схема серіалізації
# class DataSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     value = serializers.IntegerField()

# class DataViewSet(viewsets.ViewSet):
#     permission_classes = [permissions.AllowAny]  # Дозволяємо доступ усім

#     @action(detail=False, methods=["post"])
#     async def create_document(self, request):
#         print("Отримано запит:", request.data)
#         serializer = DataSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
        
#         document = serializer.validated_data
#         print("Дані для вставки:", document)
#         result = await collection.insert_one(document)
#         print("ID вставленого документа:", result.inserted_id)
        
#         created_document = await collection.find_one({"_id": result.inserted_id})
#         created_document["_id"] = str(created_document["_id"])  # Конвертуємо ObjectId у рядок
#         print("Вставлений документ:", created_document)
        
#         return Response(created_document)
# TODO TEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMP

schema_view = get_schema_view(
    openapi.Info(
        title="Vocabulary API",
        default_version="v1",
        description="Documentation for my API",
        contact=openapi.Contact(email="contact.yuriidorosh@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(),
)

API_PATH = "api/"

def index(request):
    return HttpResponse("Hello root!")

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    re_path(
        API_PATH + r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        f"{API_PATH}swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        f"{API_PATH}redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    
    path(f"{API_PATH}", include('src.api.urls')),
    # TODO TEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMP
    # path('api/data/', DataViewSet.as_view({'post': 'create_document'})),
    path('api/data/', AsyncDataAPIView.as_view(), name='async-data'),
    # TODO TEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMPTEMP
]
