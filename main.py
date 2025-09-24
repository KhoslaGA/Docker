from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="FastAPI on Cloud Run", version="1.0.0")


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI on Cloud Run!"}


@app.get("/hello/{name}")
def hello(name: str, emoji: Optional[str] = "👋"):
    return {"message": f"Hello, {name}! {emoji}"}


class Product(BaseModel):
    name: str = Field(..., min_length=3)
    price: float = Field(..., gt=0)
    in_stock: bool = True


@app.post("/products")
def add_product(p: Product):
    return {"status": "ok", "product": p}


# Health check for Cloud Run
@app.get("/healthz")
def healthz():
    return {"ok": True}
