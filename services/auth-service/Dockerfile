# services/auth-service/Dockerfile
FROM python:3.12.10-slim

# Crear carpeta de trabajo
WORKDIR /code

# Instalar dependencias del sistema necesarias para psycopg2 y compilaciones
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY ./app ./app

# Exponer el puerto del servicio
EXPOSE 8000

# Comando por defecto: levantar FastAPI con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
