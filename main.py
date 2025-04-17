from fastapi import FastAPI
from routers import produk, pelanggan

app = FastAPI(
    title="KPL API",
    description="API untuk KPL Case Project",
    version="0.0.1"
)

app.include_router(produk.router)
app.include_router(pelanggan.router)