import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from mangum import Mangum

app = FastAPI()

# habilitar CORS
origins = [
    "http://localhost:3000",               # desarrollo local
    "https://tu-frontend.vercel.app",      # frontend en Vercel
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
def hello():
    return JSONResponse({"msg": "Hola desde FastAPI en Vercel 🚀"})

# Adaptador serverless
handler = Mangum(app)
