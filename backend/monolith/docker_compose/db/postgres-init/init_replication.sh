#!/bin/bash
set -e

echo "host replication replication 0.0.0.0/0 md5" >> "$PGDATA/pg_hba.conf"
