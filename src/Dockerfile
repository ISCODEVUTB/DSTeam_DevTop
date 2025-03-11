# Usar una imagen base de Python
FROM python:3.12-slim

# Usuario no privilegiado
RUN useradd -m devtop

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar solo archivos necesarios
COPY main.py .
COPY Gestion_Paquetes/ ./Gestion_Paquetes/

#Cambiar al usuario no privilegiado
USER devtop

# Exponer el puerto en el que se ejecutará la aplicación (si es necesario)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]