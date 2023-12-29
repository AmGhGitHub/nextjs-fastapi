from fastapi import FastAPI

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

import math
import pandas


@app.get("/api/{a}/{b}")
def index(a: int, b: int):
    # a = 1
    # b = 2
    c = math.sqrt(a**2 + b**2)
    return {"message": c}


@app.get("/api/healthchecker")
def healthchecker():
    return {"status": "success", "message": "Integrate FastAPI Framework with Next.js"}
