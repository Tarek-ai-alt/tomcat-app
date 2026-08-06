# tomcat-app

Production-style FastAPI application with PostgreSQL and Docker.

## Start

```bash
docker compose up --build -d
```

## Open

```text
http://localhost:8000
```

## Swagger UI

```text
http://localhost:8000/docs
```

## Health

```text
http://localhost:8000/health
```

## Products API

```text
GET    http://localhost:8000/api/v1/products
GET    http://localhost:8000/api/v1/products/{id}
POST   http://localhost:8000/api/v1/products
DELETE http://localhost:8000/api/v1/products/{id}
```

## Logs

```bash
docker compose logs -f
```

## Stop

```bash
docker compose down
```

## Remove database data

```bash
docker compose down -v
```

## Build only the image

```bash
docker build -t tomcat-app:1.0 .
```
