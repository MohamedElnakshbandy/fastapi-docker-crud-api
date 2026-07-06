\# FastAPI Docker CRUD API



A professional REST API built with \*\*FastAPI\*\*, \*\*PostgreSQL\*\*, \*\*SQLAlchemy\*\*, and \*\*Docker Compose\*\*.



\---



\## Features



\- CRUD API for Items

\- FastAPI with automatic Swagger documentation

\- PostgreSQL database

\- SQLAlchemy ORM

\- Docker \& Docker Compose

\- Environment variables using `.env`

\- Persistent PostgreSQL data with Docker Volumes

\- Health checks for PostgreSQL

\- Layered project architecture

\- Clean separation of routers, CRUD logic, models, and configuration



\---



\## Tech Stack



\- Python 3.12

\- FastAPI

\- SQLAlchemy

\- PostgreSQL

\- Docker

\- Docker Compose

\- Pydantic



\---



\## Project Structure



```text

FastAPI-Docker/

│

├── app/

│   ├── config.py

│   ├── crud.py

│   ├── database.py

│   ├── main.py

│   ├── models.py

│   ├── schemas.py

│   └── routers/

│       ├── items.py

│       └── system.py

│

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── .env.example

├── .gitignore

└── README.md

```



\---



\## API Endpoints



| Method | Endpoint | Description |

|---------|----------|-------------|

| GET | / | Home |

| GET | /health | Health Check |

| GET | /db-check | Database Connection Check |

| POST | /items | Create Item |

| GET | /items | Get All Items |

| GET | /items/{id} | Get Item by ID |

| PUT | /items/{id} | Update Item |

| DELETE | /items/{id} | Delete Item |



\---



\## Run with Docker



Clone the repository:



```bash

git clone <repository-url>

cd FastAPI-Docker

```



Create your environment file:



```bash

cp .env.example .env

```



Start the application:



```bash

docker compose up --build

```



Swagger UI:



```

http://localhost:8000/docs

```



\---



\## Environment Variables



Example:



```

POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_database

DATABASE_URL=postgresql://your_username:your_password@postgres:5432/your_database

```



\---



\## Future Improvements



\- Alembic Database Migrations

\- Authentication (JWT)

\- User Management

\- Unit Testing

\- CI/CD Pipeline

\- Deployment

