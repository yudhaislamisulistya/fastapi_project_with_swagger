# Gunakan image dasar Python
FROM python:3.9-slim

# Tentukan direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt dan instal dependensi
COPY requirements.txt .

# Instal dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi ke dalam container
COPY . .

# Tentukan port yang akan digunakan oleh aplikasi FastAPI
EXPOSE 5151

# Perintah untuk menjalankan aplikasi menggunakan Uvicorn di port 5151
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5151"]