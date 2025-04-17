from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/produk",
    tags=["Produk"]
)

class Produk(BaseModel):
    id: int
    nama: str
    harga: float

class ProdukCreate(BaseModel):
    nama: str
    harga: float

produk_list = [
    {"id": 1, "nama": "Kopi Hitam", "harga": 15000},
    {"id": 2, "nama": "Teh Manis", "harga": 10000}
]

@router.get(
    "/", 
    response_model=List[Produk], 
    summary="Daftar Semua Produk",
    responses={
        200: {
            "description": "Daftar produk berhasil diambil",
            "content": {
                "application/json": {
                    "example": [
                        {"id": 1, "nama": "Kopi Hitam", "harga": 15000},
                        {"id": 2, "nama": "Teh Manis", "harga": 10000}
                    ]
                }
            }
        }
    }
)
def get_all_produk():
    return produk_list

@router.get(
    "/{produk_id}", 
    response_model=Produk, 
    summary="Detail Produk Berdasarkan ID",
    responses={
        200: {
            "description": "Detail produk ditemukan",
            "content": {
                "application/json": {
                    "example": {"id": 1, "nama": "Kopi Hitam", "harga": 15000}
                }
            }
        },
        404: {
            "description": "Produk tidak ditemukan",
            "content": {
                "application/json": {
                    "example": {"detail": "Produk tidak ditemukan"}
                }
            }
        }
    }
)
def get_produk(produk_id: int):
    for item in produk_list:
        if item["id"] == produk_id:
            return item
    raise HTTPException(status_code=404, detail="Produk tidak ditemukan")

@router.post(
    "/", 
    response_model=Produk, 
    summary="Tambah Produk Baru",
    status_code=201,
    responses={
        201: {
            "description": "Produk berhasil ditambahkan",
            "content": {
                "application/json": {
                    "example": {"id": 3, "nama": "Coklat Panas", "harga": 17000}
                }
            }
        }
    }
)
def create_produk(produk: ProdukCreate):
    new_id = max([p["id"] for p in produk_list], default=0) + 1
    new_data = {"id": new_id, **produk.dict()}
    produk_list.append(new_data)
    return new_data

@router.put(
    "/{produk_id}", 
    response_model=Produk,
    summary="Perbarui Data Produk",
    responses={
        200: {
            "description": "Data produk berhasil diperbarui",
            "content": {
                "application/json": {
                    "example": {"id": 1, "nama": "Kopi Susu", "harga": 18000}
                }
            }
        },
        404: {
            "description": "Produk tidak ditemukan untuk diperbarui",
            "content": {
                "application/json": {
                    "example": {"detail": "Produk tidak ditemukan"}
                }
            }
        }
    }
)
def update_produk(produk_id: int, produk: ProdukCreate):
    for i, p in enumerate(produk_list):
        if p["id"] == produk_id:
            produk_list[i].update(produk.dict())
            produk_list[i]["id"] = produk_id
            return produk_list[i]
    raise HTTPException(status_code=404, detail="Produk tidak ditemukan")

@router.delete(
    "/{produk_id}", 
    summary="Hapus Produk Berdasarkan ID",
    responses={
        200: {
            "description": "Produk berhasil dihapus",
            "content": {
                "application/json": {
                    "example": {"message": "Produk dengan ID 2 telah dihapus"}
                }
            }
        },
        404: {
            "description": "Produk tidak ditemukan untuk dihapus",
            "content": {
                "application/json": {
                    "example": {"detail": "Produk tidak ditemukan"}
                }
            }
        }
    }
)
def delete_produk(produk_id: int):
    for i, p in enumerate(produk_list):
        if p["id"] == produk_id:
            del produk_list[i]
            return {"message": f"Produk dengan ID {produk_id} telah dihapus"}
    raise HTTPException(status_code=404, detail="Produk tidak ditemukan")