from setuptools import setup, find_packages

setup(
    name="SGPaquetes",
    version="1.0",
    packages=find_packages(where="src"),  # Encuentra todos los paquetes dentro de "src"
    package_dir={"": "src"},  # Define "src" como la raíz del paquete
)
