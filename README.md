# EcoTech POOS

Proyecto Python de ejemplo para gestionar empleados, proyectos, departamentos y registros de tiempo.

## Estructura

- `src/main.py`: punto de entrada y ejemplos de uso.
- `src/dominio/`: clases principales del dominio.
- `docs/`: documentacion del proyecto.

## Requisitos

- Python 3 instalado.
- Visual Studio Code, opcionalmente.

## Preparar el entorno

Desde la carpeta raiz del proyecto, en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Ejecutar

Con el entorno virtual activo:

```powershell
python src/main.py
```

Las variables sensibles deben mantenerse en un archivo `.env` y no deben publicarse en el repositorio.
