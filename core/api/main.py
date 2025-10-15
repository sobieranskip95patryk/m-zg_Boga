from fastapi import FastAPI
from endpoints.api_endpoints import app as endpoints_app

app = FastAPI(title="MIGI Core Main")
app.mount("/", endpoints_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
