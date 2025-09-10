# Exercise: Connecting Two Containers via Docker Network

## Objective
Create two containers that communicate with each other through a custom Docker network:

* a minimal Flask app exposing an HTTP endpoint
* a PostgreSQL database providing persistence

You may use Docker Compose.

## Repository Structure

### Initial structure:

```
docker-network-exercise/
├── README.md
└── app/
├── requirements.txt
└── app.py
```

- `app/`: contains the code and Dockerfile for the Flask app (`app.py` and `requirements.txt` are provided)

### Expected final structure:

```
docker-network-exercise/
├── README.md
├── docker-compose.yml
└── app/
├── Dockerfile
├── requirements.txt
└── app.py
```

- `docker-compose.yml`: defines the web (Flask) and db (Postgres) services

## Steps

1. Create a custom Docker network called `appnet`.
2. Start a PostgreSQL container connected to `appnet`, with:
    * name `db`
    * user and password configured via environment variables
    * volume for persistence.
3. Write a `Dockerfile` for the Flask app (provided). Notes:
    * Official Python images are available on Docker Hub, including `pip` and `python`.
    * The `requirements.txt` file contains the dependencies.
    * Install dependencies with `pip install -r requirements.txt`.
    * It is recommended to upgrade `pip` first with `pip install --upgrade pip`.
    * The application can be started with `python app.py`.
4. Connect the app to the DB via the `appnet` network.
5. Test that it is possible to insert data into the DB and read it through the Flask endpoint.

## How to verify it works

```bash
docker-compose up --build
```

Open:

* [http://localhost:5000/](http://localhost:5000/) → should respond "OK"
* [http://localhost:5000/users](http://localhost:5000/users) → shows users from the DB
