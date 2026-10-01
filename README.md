# EcoTech POOS

Aplicacion de consola en Python para administrar empleados. Permite registrar, listar, buscar, actualizar y eliminar empleados mediante un menu interactivo. El proyecto tambien contiene modelos de dominio para departamentos, proyectos y registros de tiempo.

## Estructura

- `src/main.py`: punto de entrada y menus de la aplicacion.
- `src/dominio/`: modelos de empleado, departamento, proyecto y registro de tiempo.
- `src/persistencia/`: conexion a la base de datos, creacion de tablas y objetos de acceso a datos.
- `requirements.txt`: dependencias de Python.

## Requisitos

- Python 3 instalado y disponible como `python` en Git Bash.
- Git Bash en Windows.

La aplicacion usa SQLite por defecto, por lo que no hace falta instalar ni iniciar un servidor de base de datos. Tambien admite MySQL.

## Preparar el entorno en Git Bash

Ejecuta estos comandos desde la carpeta raiz del repositorio:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Para salir del entorno virtual:

```bash
deactivate
```

## Configuracion de la base de datos

Sin configuracion adicional se usa SQLite y se crea `ecotech.db` en la carpeta desde la que se ejecuta la aplicacion. Al iniciar, la aplicacion crea la tabla de empleados si no existe.

Para configurar valores propios, copia `src/.env.example` como `src/.env` y edita sus variables. El motor predeterminado es SQLite (`DB_ENGINE=sqlite`). Para usar MySQL, configura `DB_ENGINE=mysql`, `DB_NAME`, `DB_HOST`, `DB_PORT`, `DB_USER` y `DB_PASSWORD`; la base de datos debe existir previamente. No publiques `src/.env` ni credenciales reales.

## Ejecutar

Con el entorno virtual activo y desde la raiz del repositorio:

```bash
python src/main.py
```

El menu principal permite entrar al menu de empleados o salir. Las opciones de departamentos y otros modelos aun no estan conectadas al menu de la aplicacion.
