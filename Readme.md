# 🚴 Proyecto Final: RockBike Management System

## Descripción del Proyecto

Este proyecto es una aplicación web desarrollada con el framework Django de Python, diseñada para la gestión de inventario, clientes y ventas de una tienda de bicicletas (`RockBike`). Permite el registro, la consulta y la búsqueda de las principales entidades del negocio: Fabricantes, Bicicletas, Clientes y Ventas.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Framework Web:** Django
* **Base de Datos:** SQLite (por defecto en desarrollo)
* **Frontend:** HTML5, CSS3, Bootstrap.

---

## 📦 Entidades del Modelo de Datos

El sistema se basa en cuatro modelos principales conectados por relaciones:

1.  **Fabricante:** Registra la marca de las bicicletas (Ej: Specialized, Trek, Giant).
    * Campos clave: `nombre`, `pais_origen`.

2.  **Bicicleta:** El producto en sí. Relacionada con Fabricante.
    * Campos clave: `modelo`, `rodado`, `precio`, `fabricante` (ForeignKey).

3.  **Cliente:** La persona que realiza la compra.
    * Campos clave: `nombre`, `apellido`, `email`, `telefono`.

4.  **Venta:** Registra una transacción. Relacionada con Cliente y Bicicleta.
    * Campos clave: `cliente` (ForeignKey), `bicicleta` (ForeignKey), `fecha_venta`, `total`.

---

## 🚀 Funcionalidades Implementadas

El proyecto cumple con los requisitos fundamentales de gestión de datos, incluyendo la creación de registros y las consultas avanzadas:

## 🚀 Funcionalidades Implementadas

### I. Gestión Integral (CRUD Completo)
Se permite el ciclo de vida completo de los datos para las 4 entidades principales:
* **Fabricantes, Bicicletas, Clientes y Ventas:** Alta, Listado, Edición y Borrado.
* **Seguridad:** Las funciones de Alta, Edición y Borrado están protegidas y solo son accesibles para usuarios autenticados.

### II. Usuarios y Perfiles (Punto 3.2)
* **Registro y Login:** Sistema completo de autenticación de usuarios.
* **Avatares:** Cada usuario puede subir y actualizar una foto de perfil (Avatar).
* **Edición de Perfil:** Los usuarios pueden modificar sus datos personales y su imagen desde su panel.

### III. Consultas (Búsqueda Avanzada)
* Implementación de filtros dinámicos utilizando objetos `Q` de Django para búsquedas complejas por múltiples campos en todas las entidades.

### IV. Edición de Texto Enriquecido
* Uso de **CKEditor** en el modelo de Bicicletas para permitir descripciones con formato profesional.

---

## 💻 Instalación y Ejecución Local

Sigue estos pasos para levantar el proyecto en tu máquina local:

### 1. Requisitos Previos

Asegúrate de tener Python instalado.

### 2. Acceder a la Carpeta del Proyecto

## 🔐 Acceso al Panel de Administración

Para evaluar las funcionalidades protegidas y el panel de Django, utilice las siguientes credenciales:

* **Usuario:** fabricio
* **Contraseña:** 12345

### 3. Instalación de Dependencias
```bash
python pip install -r requirements.txt
