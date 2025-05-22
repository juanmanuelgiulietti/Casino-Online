Documentación de proyecto “Casino Online”

Integrantes:
1.	Acuña Tobias
2.	Frasso Ignacio
3.	Giulietti Juan Manuel
4.	Rivas Mendez Jose

Requerimientos Funcionales del Juego de Ruleta

Descripción General
Este programa simula un juego de ruleta en el que el jugador puede apostar en diferentes tipos de apuestas. El juego incluye una serie de validaciones para garantizar que el jugador ingrese opciones correctas, así como un sistema de ganancia basado en las apuestas realizadas y el resultado aleatorio de la ruleta. El jugador puede decidir continuar jugando o finalizar el juego en cualquier momento.

Funcionalidades Principales
Ingreso de Usuario:

- El programa solicita al usuario su nombre al inicio del juego. Se validan los datos para asegurar que no contenga caracteres especiales ni espacios.

Definición de Dinero Inicial:

- El jugador debe ingresar la cantidad de dinero con la que desea comenzar. El valor debe ser mayor a cero.

Selección de Apuesta:

- El jugador puede seleccionar entre diferentes tipos de apuestas:

Pleno: Apostar a un número específico entre 0 y 36.

Rojo / Negro: Apostar al color de la ruleta (Rojo o Negro).

Par / Impar: Apostar si el número es par o impar.

Rango de 1 a 18 / 19 a 36: Apostar a un rango de números.

Columna 1, 2, 3: Apostar a una columna de números.

Docena 1 (1-12), 2 (13-24), 3 (25-36): Apostar a una docena específica.

El jugador selecciona la opción a través de un número del 1 al 13.

Creación de Apuesta:

- El jugador ingresa la cantidad de dinero a apostar. Se valida que la cantidad esté dentro del saldo disponible y que sea mayor a cero.

Giro de la Ruleta:

- La ruleta genera un resultado aleatorio (número, color y paridad) mediante la función random.choice aplicada a una lista de resultados posibles.

Determinación de Resultados:

- Se compara el resultado del giro de la ruleta con la apuesta seleccionada por el jugador. Si el jugador gana, su saldo se incrementa; si pierde, su saldo se decrementa.

Continuar o Terminar Juego:

- Después de cada ronda, el jugador puede elegir si desea seguir jugando o terminar el juego. Si elige continuar, el juego sigue con una nueva ronda.

Flujo de Juego
Inicio del Juego:

1. El jugador ingresa su nombre y el saldo inicial con el que desea jugar.

Selección de Apuesta:

2. Se muestran las opciones de apuestas y el jugador elige una opción.

Validación de Apuesta:

3. Se valida que la apuesta seleccionada sea correcta y, si es necesario, se solicita un número específico en el caso de apuestas tipo "Pleno".

Giro de la Ruleta y Determinación de Resultados:

4. La ruleta gira y el programa determina si el jugador ha ganado o perdido según su apuesta.

Actualización de Saldo:

5. El saldo del jugador se actualiza y se muestra al final de cada ronda.

Continuación del Juego:

6. El jugador decide si desea continuar jugando o finalizar el juego.

Requerimientos Técnicos

Entrada y Salida:

> Entrada por consola para los datos de usuario, apuestas y dinero.

> Salida por consola con los resultados de cada ronda, ganancias, pérdidas y el saldo actualizado.

Funciones Principales
continuarJuego(): Permite al jugador decidir si continúa jugando o no.

determinarResultado(): Determina si el jugador ha ganado o perdido y actualiza el saldo.

girarRuleta(): Simula el giro de la ruleta y devuelve el resultado.

crearApuesta(): Permite al jugador realizar una apuesta dentro de los límites de su saldo.

validarApuestaSeleccionada(): Valida la apuesta seleccionada por el jugador.

elegirApuesta(): Muestra las opciones de apuesta y permite al jugador elegir una.

ingresarDinero(): Permite al jugador ingresar la cantidad de dinero con la que desea comenzar el juego.

crearUsuario(): Solicita el nombre del jugador y valida la entrada.