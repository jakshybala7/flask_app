# Flask Docker Project

A simple Flask REST API with SQLite, deployed using Docker.

## Features:
- Add messages via POST /add
- Retrieve messages via GET /messages
- Docker container + docker-compose
- SQLite database persists outside the container

## How to run:
1. docker-compose build
2. docker-compose up
3. Open http://localhost:5000 in your browser
