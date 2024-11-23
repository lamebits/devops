FROM mysql:8.0
LABEL ProjectName="vprofile"
LABEL Username="Meenal"

ENV MYSQL_ROOT_PASSWORD="vprodbpass"
ENV MYSQL_DATABASE="accounts"

ADD db_backup.sql /docker-entrypoint-initdb.d/db_backup.sql