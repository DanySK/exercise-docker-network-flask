# Esercizio: Connessione di due container tramite rete Docker

## Obiettivo
Creare due container che comunicano fra loro tramite una rete Docker personalizzata:

* un’app Flask minimale che espone un endpoint HTTP
* un database PostgreSQL che fornisce persistenza

È consentito l’uso di Docker Compose.

## Struttura del repo

### Struttura di partenza:

```
docker-network-exercise/
 ├── README.md
 └── app/
      ├── requirements.txt
      └── app.py
```

- `app/`: contiene il codice e il Dockerfile dell'app Flask (`app.py` e `requirements.txt` vengono forniti)

### Struttura attesa finale:

```
docker-network-exercise/
 ├── README.md
 ├── docker-compose.yml
 └── app/
      ├── Dockerfile
      ├── requirements.txt
      └── app.py
```

- `docker-compose.yml`: definisce i servizi web (Flask) e db (Postgres)

## Traccia

1. Creare una rete Docker personalizzata chiamata `appnet`.
2. Avviare un container PostgreSQL collegato a `appnet`, con:
    * nome `db`
    * utente e password configurati tramite variabili d’ambiente
    * volume per la persistenza.
3. Scrivere un `Dockerfile` per l’app Flask (fornita). Note:
    * Sono disponibili immagini ufficiali Python su Docker Hub, che includono `pip` e `python`.
    * Il file `requirements.txt` contiene le dipendenze.
    * L'installazione delle dipendenze avviene tramite `pip install -r requirements.txt`.
    * Prima di installare le dipendenze, è consigliabile aggiornare `pip` con `pip install --upgrade pip`.
    * L'applicazione può essere avviata con `python app.py`.
4. Collegare l’app al DB tramite la rete `appnet`.
5. Testare che sia possibile inserire dati nel DB e leggerli tramite l’endpoint Flask.

## Verifica del funzionamento

```bash
docker-compose up --build
````

Aprire:

* [http://localhost:5000/](http://localhost:5000/) → deve rispondere "OK"
* [http://localhost:5000/users](http://localhost:5000/users) → mostra utenti dal DB
