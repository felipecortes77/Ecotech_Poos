# EcoTech POOS

Aplicacion de consola en Python para administrar empleados. Permite registrar, listar, buscar, actualizar y eliminar empleados mediante un menu interactivo. El proyecto tambien contiene modelos de dominio para departamentos, proyectos y registros de tiempo.

## Estructura
- `src/presentacion`: distintos menus
- `src/main.py`: punto de entrada  para los menus de la aplicacion.
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

Para configurar valores propios, copia `.env.example` como `.env` y edita sus variables. El motor predeterminado es SQLite (`DB_ENGINE=sqlite`). Para usar MySQL, configura `DB_ENGINE=mysql`, `DB_NAME`, `DB_HOST`, `DB_PORT`, `DB_USER` y `DB_PASSWORD`; la base de datos debe existir previamente. No publiques `.env` ni credenciales reales.

## Ejecutar

Con el entorno virtual activo y desde la raiz del repositorio:

```bash
python src/main.py
```

Al iniciar, se cargan cinco cuentas de administrador y cinco cuentas de empleado,
asociadas a empleados existentes. Las cuentas de empleado solo pueden consultar
su ficha, actualizar su nombre y correo, y ver sus propios registros de tiempo.
Los usuarios autenticados también pueden consultar la cotización del dólar
desde la API de ExchangeRate-API en sus respectivos menús.
Cada consulta guarda en `indicador_api` la fecha UTC y el valor CLP/USD:
si ya existe un valor para esa fecha, se actualiza; de lo contrario, se agrega
un nuevo día al historial.

Credenciales iniciales de demostracion:

- El nombre de usuario de cada cuenta es el nombre de su empleado asociado.
  Los administradores son Juan Perez (`admin123`), Maria Gonzalez, Carlos
  Silva, Ana Rodriguez y Jose Muñoz (los cuatro últimos usan `Admin2026!`).
- Los empleados son Laura Rojas, Pedro Diaz, Sofia Contreras, Miguel Soto y
  Carolina Martinez; todos usan `Empleado2026!`.

El menu de administrador permite administrar empleados, departamentos,
proyectos, registros de tiempo y usuarios. Cambia las contraseñas iniciales
antes de utilizar estas cuentas fuera de un entorno de demostracion.
