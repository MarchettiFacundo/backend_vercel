from fastapi import FastAPI

# 👇 Este objeto debe llamarse exactamente "app"
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola desde FastAPI en Vercel 🚀"}
