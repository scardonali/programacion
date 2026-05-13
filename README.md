# programacion
# Sistema de Gestión - Software FJ (Fase 4)

Este proyecto es una solución integral orientada a objetos desarrollada para la empresa **Software FJ**, enfocada en la gestión de clientes, servicios y reservas.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.12
* **Paradigma:** Programación Orientada a Objetos (POO)
* **Gestión de Versiones:** Git / GitHub

## 📂 Estructura del Proyecto
* `/src`: Contiene la lógica del sistema (`clases.py`) y el motor de simulación (`main.py`).
* `/docs`: Documentación oficial del proyecto y guía de actividades.
* `/logs`: Registros de eventos y excepciones generados por el sistema.

## 🚀 Cómo ejecutar
1. Asegúrese de tener Python instalado.
2. Navegue a la carpeta `src/`.
3. Ejecute el comando: `python main.py`.

## ⚠️ Manejo de Excepciones
El sistema implementa excepciones personalizadas para garantizar la robustez:
* `ReservaInvalidaError`: Gestiona fallos en el proceso de reserva.
* `ServicioNoDisponibleError`: Controla parámetros fuera de los límites permitidos.