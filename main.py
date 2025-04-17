from fastapi import FastAPI
from routers import pelanggan, produk

app = FastAPI(
    title="Studi Kasus FastAPI - Dua Group Service",
    description="API untuk mengelola data produk dan pelanggan.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Produk",
            "description": "Semua endpoint untuk mengelola data produk yang dijual dalam sistem. Termasuk melihat daftar, detail, tambah, edit, dan hapus produk."
        },
        {
            "name": "Pelanggan",
            "description": "Semua endpoint terkait data pelanggan. Anda bisa menambahkan, mengubah, menghapus, dan melihat daftar pelanggan."
        }
    ]
)

# Daftarkan router
app.include_router(produk.router)
app.include_router(pelanggan.router)