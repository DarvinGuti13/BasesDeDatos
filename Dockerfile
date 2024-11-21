
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /usr/src/app


ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Exponer el puerto 5000 para Flask
EXPOSE 5000

# Usa gunicorn como servidor WSGI
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--workers", "3"]
