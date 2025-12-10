# Flask App with Docker

A simple Flask web application running in Docker, showcasing full-stack DevOps skills.

## Features

- REST API endpoints (GET/POST)  
- Dockerized for easy deployment  
- Configurable via `docker-compose.yml`  
- Ready for production deployment with WSGI server  

## Tech Stack

- **Backend:** Python, Flask  
- **Containerization:** Docker, Docker Compose  
- **Version Control:** Git, GitHub  

## Getting Started

### Prerequisites

- Docker Desktop installed  
- Git installed  

### Clone Repository

```bash
git clone https://github.com/AdilbekMamatov/flask_app.git
cd flask_app
```

### Run with Docker Compose

```bash
docker-compose up --build
```

- App runs on: `http://localhost:5001` (mapped from container port 5000)

### API Endpoints (example)

- `GET /` → Returns welcome message  
- `POST /data` → Accepts JSON data and returns response  

### Stop Containers

```bash
docker-compose down
```

## Project Structure

```
flask_app/
├─ app.py
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ README.md
├─ .gitignore
├─ LICENSE
└─ data/  # optional for storage
```

## License

This project is licensed under the MIT License.

