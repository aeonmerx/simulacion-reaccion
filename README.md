# Simulación de Conversión de Sustancias Químicas en Reacciones de Primer Orden

Este proyecto ilustra cómo una sustancia química se convierte en otra en una reacción de **primer orden**, utilizando un modelo matemático para representar el proceso de cambio de concentraciones con el tiempo.

## Descripción del Proyecto

En las reacciones químicas de **primer orden**, una sustancia reactante **A** se transforma en un producto **B** de manera progresiva. La velocidad de la reacción depende directamente de la concentración de **A**. Esto significa que, a medida que la concentración de **A** disminuye, la reacción se ralentiza.

Este proyecto simula este proceso y muestra cómo:

- **A**: La sustancia original se **consume** con el tiempo.
- **B**: La sustancia producto **se forma** progresivamente.

La reacción sigue la fórmula cinética de primer orden:

\[
[A](t) = [A]_0 e^{-kt}
\]

Donde:
- **[A](t)** es la concentración de **A** en cualquier momento **t**.
- **[A]_0** es la concentración inicial de **A**.
- **k** es la constante de velocidad de la reacción.
- **t** es el tiempo transcurrido.

## Librerías Utilizadas

Este proyecto usa las siguientes librerías de Python:

- **NumPy**: Para el manejo de datos numéricos y cálculos matemáticos.
- **SciPy**: Para resolver las ecuaciones diferenciales que modelan la cinética de la reacción.
- **Matplotlib**: Para graficar los resultados y visualizar las concentraciones de **A** y **B** con el tiempo.

## Instalación

Si quieres ejecutar este código en tu entorno local, sigue estos pasos:

1. Clona el repositorio o copia el código de la notebook.
    
    ```bash
    git clone https://github.com/aeonmerx/simulacion-reaccion.git
    ```

2. Instala las dependencias utilizando `pip`:

    ```bash
    pip install rdkit scipy numpy matplotlib
    ```

## Uso

Para ejecutar la simulación, asegúrate de tener todas las dependencias instaladas y simplemente corre el script:

```bash
python simulacion_reaccion.py
