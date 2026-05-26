#!/bin/bash

#создание бэкапа из контейнера
BACKUP_DIR="/opt/backups"
CONTAINER_NAME="digital-backpack-db"
DB_NAME="backpack"
DB_USER="backpack_user"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_${TIMRSTAMP}.sql.gz"

#создание директории для бэкапа
mkdir -p $BACKUP_DIR

#дамп
docker exec $CONTAINER_NAME pg_dump -U $DB_USER $DB_NAME | gzip > $BACKUP_FILE

#удаление бэкапа старше 7 дней
find $BACKUP_DIR -name "*.sql.gz" -mtime +7 -delete

echo "Бэкап создан: $BACKUP_FILE"