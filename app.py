from fastapi import FastAPI
from funciones import get_materias
import uvicorn
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola desde FastAPI en Vercel 🚀"}
@app.get("/lean")
def hola():
    return {"message": "hola putito levante un backend en vercel y con python"}
@app.get('/materias')
def obtener_materias():
    materias = get_materias()
    return materias
def main():
    uvicorn.run("app:app", port=3001,host= '0.0.0.0')
if __name__ == "__main__":
    main()