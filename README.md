# Flask + PostgreSQL Docker App

Semplice web app containerizzata con Flask e PostgreSQL.

Permette di visualizzare e salvare messaggi tramite interfaccia web.
Tutto viene avviato con Docker Compose e i dati restano persistenti.

---

## Avvio

```bash
docker compose up --build
```

Apri nel browser:

```
http://localhost:5000
```

---

## Stack

* Flask
* PostgreSQL
* Docker
* Docker Compose

---

## Struttura

```
app.py
Dockerfile
docker-compose.yml
requirements.txt
templates/
```

---

## Stop

```bash
docker compose down
```
