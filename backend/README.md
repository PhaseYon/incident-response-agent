# Incident Response Agent – Backend

FastAPI backend for the Incident Response Agent project.

## Project structure

```
backend/
  app/
    main.py            # FastAPI application factory
    core/config.py     # App settings (Pydantic BaseSettings)
    utils/logging.py   # Shared logger helper
    db/
      database.py      # In-memory incident store (replace with real DB later)
      models.py        # Dataclass models for the in-memory store
    schemas/           # Pydantic request/response schemas
    services/          # Business logic and external-service stubs
    routes/            # FastAPI routers
  tests/
    test_health.py     # Pytest tests for the /health endpoint
  requirements.txt
  Dockerfile
  README.md
```

## Running locally

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the server with uvicorn

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API is now available at <http://localhost:8000>.  
Interactive docs (Swagger UI) are at <http://localhost:8000/docs>.

### 4. Run tests

```bash
pytest tests/
```

## Available endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| POST | `/tools/search-logs` | Search application logs (Elastic stub) |
| POST | `/tools/get-latency-metrics` | Retrieve latency percentiles (Elastic stub) |
| POST | `/tools/summarize-errors` | Summarise recent errors (Elastic stub) |
| POST | `/tools/get-recent-deployments` | Recent deployment events (stub) |
| POST | `/tools/create-incident-ticket` | Create an incident ticket |
| GET | `/incidents` | List all incidents |
| GET | `/incidents/{incident_id}` | Get a single incident by ID |
| POST | `/scenarios/payment-latency/on` | Activate payment-latency scenario |
| POST | `/scenarios/payment-latency/off` | Deactivate payment-latency scenario |

## Configuration

Environment variables (can be placed in a `.env` file in the `backend/` directory):

| Variable | Default | Description |
|----------|---------|-------------|
| `ELASTIC_HOST` | `http://localhost:9200` | Elasticsearch host URL |
| `ELASTIC_INDEX` | `logs-*` | Default log index pattern |
| `ELASTIC_API_KEY` | _(empty)_ | Elasticsearch API key |
| `DEBUG` | `false` | Enable debug mode |

## Running with Docker

```bash
docker build -t incident-response-backend .
docker run -p 8000:8000 incident-response-backend
```
