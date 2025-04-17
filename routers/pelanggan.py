from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(
    prefix="/pelanggan",
    tags=["Pelanggan"]
)

class Pelanggan(BaseModel):
    id: int
    nama: str
    email: str

class PelangganCreate(BaseModel):
    nama: str
    email: str

pelanggan_list = [
    {"id": 1, "nama": "Andi", "email": "andi@mail.com"},
    {"id": 2, "nama": "Siti", "email": "siti@mail.com"}
]

@router.get(
    "/", 
    response_model=List[Pelanggan],
    summary="Daftar Semua Pelanggan",
    responses={
        200: {
            "description": "Daftar pelanggan berhasil diambil",
            "content": {
                "application/json": {
                    "example": [
                        {"id": 1, "nama": "Andi", "email": "andi@mail.com"},
                        {"id": 2, "nama": "Siti", "email": "siti@mail.com"}
                    ]
                }
            }
        }
    }
)
def get_all_pelanggan():
    return pelanggan_list

@router.get(
    "/{pelanggan_id}",
    response_model=Pelanggan,
    summary="Detail Pelanggan Berdasarkan ID",
    responses={
        200: {
            "description": "Data pelanggan ditemukan",
            "content": {
                "application/json": {
                    "example": {"id": 1, "nama": "Andi", "email": "andi@mail.com"}
                }
            }
        },
        404: {
            "description": "Pelanggan tidak ditemukan",
            "content": {
                "application/json": {
                    "example": {"detail": "Pelanggan tidak ditemukan"}
                }
            }
        }
    }
)
def get_pelanggan(pelanggan_id: int):
    for p in pelanggan_list:
        if p["id"] == pelanggan_id:
            return p
    raise HTTPException(status_code=404, detail="Pelanggan tidak ditemukan")

@router.post(
    "/",
    response_model=Pelanggan,
    summary="Tambah Pelanggan Baru",
    status_code=201,
    responses={
        201: {
            "description": "Pelanggan berhasil ditambahkan",
            "content": {
                "application/json": {
                    "example": {"id": 3, "nama": "Budi", "email": "budi@mail.com"}
                }
            }
        }
    }
)
def create_pelanggan(pelanggan: PelangganCreate):
    new_id = max([p["id"] for p in pelanggan_list], default=0) + 1
    new_data = {"id": new_id, **pelanggan.dict()}
    pelanggan_list.append(new_data)
    return new_data

@router.put(
    "/{pelanggan_id}",
    response_model=Pelanggan,
    summary="Perbarui Data Pelanggan",
    responses={
        200: {
            "description": "Data pelanggan berhasil diperbarui",
            "content": {
                "application/json": {
                    "example": {"id": 1, "nama": "Andi Update", "email": "andi@update.com"}
                }
            }
        },
        404: {
            "description": "Pelanggan tidak ditemukan untuk diperbarui",
            "content": {
                "application/json": {
                    "example": {"detail": "Pelanggan tidak ditemukan"}
                }
            }
        }
    }
)
def update_pelanggan(pelanggan_id: int, pelanggan: PelangganCreate):
    for i, p in enumerate(pelanggan_list):
        if p["id"] == pelanggan_id:
            pelanggan_list[i].update(pelanggan.dict())
            pelanggan_list[i]["id"] = pelanggan_id
            return pelanggan_list[i]
    raise HTTPException(status_code=404, detail="Pelanggan tidak ditemukan")

@router.delete(
    "/{pelanggan_id}",
    summary="Hapus Pelanggan Berdasarkan ID",
    responses={
        200: {
            "description": "Pelanggan berhasil dihapus",
            "content": {
                "application/json": {
                    "example": {"message": "Pelanggan dengan ID 1 telah dihapus"}
                }
            }
        },
        404: {
            "description": "Pelanggan tidak ditemukan untuk dihapus",
            "content": {
                "application/json": {
                    "example": {"detail": "Pelanggan tidak ditemukan"}
                }
            }
        }
    }
)
def delete_pelanggan(pelanggan_id: int):
    for i, p in enumerate(pelanggan_list):
        if p["id"] == pelanggan_id:
            del pelanggan_list[i]
            return {"message": f"Pelanggan dengan ID {pelanggan_id} telah dihapus"}
    raise HTTPException(status_code=404, detail="Pelanggan tidak ditemukan")