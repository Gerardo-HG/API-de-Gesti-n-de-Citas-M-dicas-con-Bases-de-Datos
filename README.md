## Descripción

Esta API permite gestionar citas médicas de manera eficiente. En esta nueva versión del proyecto, se ha realizado una actualización significativa: se ha reemplazado el almacenamiento en archivos JSON por el uso de bases de datos. Este cambio mejora la escalabilidad y eficiencia del sistema, permitiendo una gestión de datos más robusta y adecuada para aplicaciones de mayor envergadura.

Las funcionalidades principales incluyen el registro de pacientes, médicos y citas, con una verificación de consistencia que evita duplicados en los DNIs entre pacientes y médicos.

La API está desarrollada con **FastAPI**, un framework rápido y moderno basado en Python, ideal para construir APIs robustas y escalables.

## Características principales

- Registro de pacientes y médicos con validación de DNIs.
- Registro de citas médicas asegurando la consistencia de los datos.
- Uso de bases de datos para almacenamiento de datos (en vez de archivos JSON).
- Validación automática de datos con **Pydantic**.
- Middleware de autenticación **JWT**.
- Integración con bases de datos SQL.

## Requisitos

- Python 3.10 o superior
- FastAPI
- Uvicorn
- SQLAlchemy (para manejo de bases de datos)
- SQLite o cualquier base de datos SQL compatible

## Instalación

1. Clona este repositorio

git clone https://github.com/Gerardo-HG/API-de-Gesti-n-de-Citas-M-dicas-con-Bases-de-Datos.git

2. Navega al directorio del proyecto

cd API-CitasMedicas

3. Crea un entorno virtual e instala las dependencias

python3 -m venv venv source venv/bin/activate # En Windows: venv\Scripts\activate pip install -r requirements.txt

4. Asegúrate de tener configurada tu base de datos (SQLite o cualquier otra compatible) según las configuraciones de tu proyecto.

## Ejecución

1. Inicializa el servidor con Uvicorn

uvicorn main:app --reload

2. Accede a la documentación interactiva de la API en:
   - **Swagger UI**: http://127.0.0.1:8000/docs
   - **Redoc**: http://127.0.0.1:8000/redoc

## Endpoints principales

### Pacientes

- **POST /pacientes**: Registrar un nuevo paciente.
- **GET /pacientes**: Obtener todos los pacientes.

### Médicos

- **POST /medicos**: Registrar un nuevo médico.
- **GET /medicos**: Obtener todos los médicos.

### Citas Médicas

- **POST /citas**: Registrar una nueva cita.
- **GET /citas**: Obtener todas las citas.

## Estructura del Proyecto

API-CitasMedicas/
│
├── main.py # Archivo principal para iniciar la API
│
├── routes/ # Rutas de la API
│ ├── routes_pacientes.py # Rutas relacionadas con pacientes
│ ├── routes_medicos.py # Rutas relacionadas con médicos
│ ├── routes_citas.py # Rutas relacionadas con citas médicas
│
├── models/ # Modelos de base de datos
│ ├── paciente.py # Modelo de paciente en base de datos
│ ├── medico.py # Modelo de médico en base de datos
│ ├── cita.py # Modelo de cita médica en base de datos
│
├── utils/ # Funciones auxiliares y utilidades
│ ├── jwt_manager.py # Manejo de autenticación JWT
│ ├── validators.py # Validación de datos compartidos (opcional)
│
├── database/ # Configuración de la base de datos
│ ├── config.py # Configuración de conexión a la base de datos
│ ├── session.py # Sesiones de base de datos
│
├── requirements.txt # Dependencias del proyecto
│
├── README.md # Documentación del proyecto
│
└── LICENSE # Licencia del proyecto
