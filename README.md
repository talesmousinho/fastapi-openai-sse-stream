# FastAPI OpenAI Server-Sent Events Stream

This is a Python FastAPI application that return OpenAI's response has a stream of Server-Sent Events.

## Setup

Install the dependencies:

```bash
poetry install
```

### Environment Variables

Before running the application or the tests, copy `.env.example` to `.env` and fill in the appropriate values:

```bash
cp .env.example .env
```

## Usage

To run the application:

```bash
poetry run uvicorn app.main:app
```

This will start a development server at `http://localhost:8000/`.

## Testing

To run the tests:

```bash
poetry run pytest
```
