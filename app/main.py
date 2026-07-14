from fastapi import FastAPI

app = FastAPI(title="dart-tracker-agent")


@app.get("/health")
def health():
    return {"status": "ok"}
