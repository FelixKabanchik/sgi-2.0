# SGI 2.0 - Sistema de Gestión de Inventario

## Descripción del Proyecto
Sistema informático desarrollado en Python para centralizar la gestión operativa de un comercio. Permite el control preciso y automatizado de productos, categorías e inventario.

## Integrantes del Equipo
- **Lautaro Zunino** - Procesamiento avanzado de cadenas de caracteres y reduce
- **Felipe Larrañaga** - Validaciones con expresiones regulares y algoritmos de ordenamiento
- **Felix Cabanchik** (Referente) - Configuración Git, control de ramas y módulo de login
- **Agustín Poggi** - Módulo de consultas estadísticas con funciones Lambda

## Funcionalidades Principales
- Control de acceso (Login)
- ABM de Productos, Categorías e Inventario
- Algoritmos de ordenamiento (burbuja, selección, inserción)
- Búsquedas secuencial y binaria
- Validaciones con expresiones regulares
- Reportes con matrices y funciones de orden superior
- Funciones Lambda: map, filter, reduce
- Gestión completa con Git

## Estructura del Proyecto
```
sgi-2.0/
├── src/
│   ├── main.py           # Punto de entrada del sistema
│   ├── login.py          # Módulo de control de acceso
│   ├── productos.py      # ABM de Productos
│   ├── categorias.py     # ABM de Categorías
│   ├── inventario.py     # ABM de Inventario
│   └── reportes.py       # Módulo de reportes estadísticos
├── README.md
└── .gitignore
```

## Branches del Proyecto
- **main** - Rama principal (producción)
- **lautaro-zunino** - Desarrollo de procesamiento de cadenas
- **felipe-larranaga** - Desarrollo de validaciones y ordenamiento
- **felix-cabanchik** - Desarrollo de login y configuración
- **agustin-poggi** - Desarrollo de reportes estadísticos
