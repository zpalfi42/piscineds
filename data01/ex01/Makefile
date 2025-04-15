SHELL	= /bin/sh

NAME	= ex01

all:
	docker-compose build && \
		docker-compose up -d
test_postgres:
	docker exec -it postgres sh \
		-c "psql -U zpalfi -d piscineds -h localhost -W"
logs:
	docker compose logs postgres
down:
	docker compose down
rm_volume:
	docker volume rm ex01_postgres_data ex01_pgadmin_data
clean: down rm_volume