# SGPaquetes

## Tabla de Contenidos
1. [Descripción](#descripción)
2. [Comenzando](#comenzando)
   - [Prerrequisitos](#prerrequisitos)
   - [Instalación](#instalación)
3. [Uso](#uso)
4. [Arquitectura](#arquitectura)
   - [Estructura del Proyecto](#estructura-del-proyecto)
   - [Componentes](#componentes)
5. [API](#api)
   - [Gestión de Usuarios](#gestión-de-usuarios)
   - [Gestión de Paquetes](#gestión-de-paquetes)
   - [Gestión de Envíos](#gestión-de-envíos)
   - [Gestión de Facturas](#gestión-de-facturas)
6. [Tecnologías](#tecnologías)
7. [Equipo](#equipo)
8. [Contribución](#contribución)
9. [Licencia](#licencia)

## Descripción
SGPaquetes es un sistema de gestión de paquetes que permite a los usuarios gestionar envíos, paquetes, usuarios y facturas. El sistema está diseñado para facilitar la administración de estos elementos a través de una interfaz de línea de comandos.

## Comenzando

### Prerrequisitos
- Python 3.8 o superior
- Sistema Operativo: Windows, Linux o macOS
- Memoria RAM: 4GB mínimo recomendado
- Espacio en disco: 100MB mínimo
- Conexión a Internet (para la instalación de dependencias)

### Instalación
1. Clonar el repositorio:
```bash
git clone <URL_DEL_REPOSITORIO>
```

2. Crear y activar el entorno virtual:

**Windows**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso
Para ejecutar el sistema:
```bash
python main.py
```

## Arquitectura

### Estructura del Proyecto
```
SGPAQUETES
├── .github/
│   └── ci.yml
├── src/
│   ├── data/
│   │   ├── Invoices.csv
│   │   ├── Packages.csv
│   │   ├── Shipments.csv
│   │   └── Users.csv
│   ├── controllers.py
│   ├── models.py
│   ├── utils.py
│   └── views.py
├── tests/
│   ├── test_main.py
│   ├── test_models.py
│   ├── test_utils.py
│   └── test_views.py
├── .dockerignore
├── .flake8
├── .gitignore
├── Dockerfile
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

### Componentes

#### Modelos (`models.py`)
- **Package**: Representa un paquete con un ID, nombre, peso y destino
- **User**: Representa un usuario con un ID, nombre de usuario, contraseña, nombre, email, dirección y permisos
- **Shipment**: Representa un envío con un ID, ID de usuario, paquete, costo, fecha y estado
- **Invoice**: Representa una factura con un ID, ID de usuario, envío, costo y fecha

#### Controladores (`controllers.py`)
- **Manager**: Clase base para la gestión de datos
- **LoginManager**: Gestiona el inicio de sesión y registro de usuarios
- **PaymentsManager**: Gestiona los pagos
- **ShipmentManager**: Gestiona los envíos
- **PackageManager**: Gestiona los paquetes
- **InvoiceManager**: Gestiona las facturas
- **UserManager**: Gestiona los usuarios

#### Utilidades (`utils.py`)
- `validate_input`: Valida que los campos de entrada no estén vacíos
- `generate_id`: Genera un ID único basado en los IDs existentes

#### Vistas (`views.py`)
- **Menu**: Clase base para la creación de menús
- **LoginMenu**: Menú de logueo
- **MainMenu**: Menú principal del sistema
- **PackageMenu**: Menú para la gestión de paquetes
- **ShipmentMenu**: Menú para la gestión de envíos
- **InvoicesMenu**: Menú para la gestión de facturas

## API

### Gestión de Usuarios (`LoginManager`, `UserManager`)
- `login(username, password)`: Permite a los usuarios autenticarse en el sistema
- `sign_in(username, password, name, email, address, permissions)`: Registra nuevos usuarios
- `update_user(user_id, username, password, name, email, address, permissions)`: Actualiza datos de usuarios
- `delete_user(user_id)`: Elimina usuarios
- `search_user(search_criteria)`: Busca usuarios

### Gestión de Paquetes (`PackageManager`)
- `show_packages()`: Muestra todos los paquetes registrados
- `add_package(name, weight, destination)`: Agrega nuevos paquetes
- `update_package(package_id, name, weight, destination)`: Modifica paquetes existentes
- `delete_package(package_id)`: Elimina paquetes
- `search_package(search_criteria)`: Busca paquetes

### Gestión de Envíos (`ShipmentManager`)
- `show_shipments()`: Muestra todos los envíos registrados
- `create_shipment(user_id, package_id, cost, date, state)`: Crea nuevos envíos
- `update_shipment_state(shipment_id, new_state)`: Actualiza estado de envíos
- `delete_shipment(shipment_id)`: Elimina envíos
- `search_shipment(search_criteria)`: Busca envíos

### Gestión de Facturas (`InvoiceManager`)
- `show_invoices()`: Muestra todas las facturas registradas
- `generate_invoice(user_id, shipment_id, cost, date)`: Genera nuevas facturas
- `update_invoice(invoice_id, cost, date)`: Actualiza facturas
- `delete_invoice(invoice_id)`: Elimina facturas
- `search_invoice(search_criteria)`: Busca facturas

## Tecnologías

### Lenguajes y Frameworks
- Python 3.8

### Bibliotecas Principales
- pandas: Para el manejo de datos tabulares
- pytest: Para pruebas unitarias
- flake8: Para el análisis estático de código

### Herramientas de Desarrollo
- Docker: Para la containerización
- Git: Para el control de versiones
- GitHub Actions: Para CI/CD

### Almacenamiento
- CSV: Para el almacenamiento de datos

## Equipo

### Desarrolladores Principales
- **Omar Hernandez** - *Programador* - [Oyhs-co](https://github.com/Oyhs-co)
- **Andres Ahumada** - *Programador* - [andreztxt](https://github.com/andreztxt)

### Contribuidores
- **Dylan Ecker** - *Code quality* - [dylecker](https://github.com/dylecker)
- **William Cuello** - *CI/CD* - [vollereiseelee](https://github.com/vollereiseelee)
- **Juan Serpa** - *CI/CD* - [jdssmdna](https://github.com/jdssmdna)

### Supervisión
- **Edwin Puerta** - *AI Software Architect - Project Manager*

## Contribución
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.