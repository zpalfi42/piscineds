SHELL	= /bin/sh

NAME	= ex00

all:
	docker-compose up -d
test_postgres:
	docker exec -it postgres sh \
		-c "psql -U zpalfi -d piscineds -h localhost -W"
logs:
	docker compose logs postgres
down:
	docker compose down
rm_volume:
	docker volume rm ex00_postgres_data
clean: down rm_volume