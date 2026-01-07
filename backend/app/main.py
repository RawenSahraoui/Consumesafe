from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from app.api.routes import router

app = FastAPI(title="ConsumeSafe API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "ConsumeSafe API", "version": "1.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}