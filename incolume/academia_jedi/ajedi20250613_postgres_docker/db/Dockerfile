FROM postgres:17-alpine3.21
ADD scripts/1_init.sql /docker-entrypoint-initdb.d
ADD scripts/2_load_data.sql /docker-entrypoint-initdb.d
RUN chmod a+r /docker-entrypoint-initdb.d/*
EXPOSE 5432
