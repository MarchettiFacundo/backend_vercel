from fastapi import FastAPI

# 👇 Este objeto debe llamarse exactamente "app"
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola desde FastAPI en Vercel 🚀"}
@app.get("/lean")
def hola():
    return {"message": "hola putito levante un backend en vercel y con python"}
