*Este proyecto ha sido creado como parte del currículo de 42 por Francysa.*

# Printf - Implementar el comportamiento de esta función.

## Descripción
Este proyecto consiste en reimplementar el comportamiento de la función `printf`, aprendiendo a utilizar funciones variadicas y optimizando la estructura del código.

El proyecto exige el desarrollo de la función `ft_printf`, la cual debe replicar al original en el número de caracteres impresos y en el formato de salida.

## Convertidores (Parte Obligatoria)

| Convertidor | Descripción |
| :---: | :--- |
| `%c` | Imprime un único carácter. |
| `%s` | Imprime una cadena de caracteres (string). Si es `NULL`, imprime `(null)`. |
| `%p` | Imprime la dirección de un puntero en formato hexadecimal. |
| `%d` / `%i` | Imprime un número entero con signo en base 10. |
| `%u` | Imprime un número entero sin signo en base 10. |
| `%x` | Imprime un número hexadecimal en minúsculas (base 16). |
| `%X` | Imprime un número hexadecimal en mayúsculas (base 16). |
| `%%` | Imprime el signo del porcentaje de manera literal. |

## Instrucciones

El proyecto ha sido diseñado de manera modular, incluyendo un `Makefile` con las reglas estándar. Para compilar la librería clona el repositorio y ejecuta:

```make``` o ```make all```: Compila los archivos base y genera libft.a.

```make clean```: Elimina los archivos objeto (.o).

```make fclean```: Elimina los objetos y el archivo de la librería (libft.a).

```make re```: Limpia y vuelve a compilar todo.

## Recursos

* Documentación oficial de GNU C Library.

* Manual de programador de Linux (man pages).

* Tutoriales sobre punteros y funciones variadicas en C.

* Manual de IBM y Geeksforgeeks

* Uso de IA
Para este proyecto se ha utilizado inteligencia artificial (como Gemini/Chat GPT) para las siguientes tareas:

* Para comprender a fondo la lógica de las funciones variádicas y cómo se desplazan los argumentos en la pila de memoria

* Para interpretar algunos `warning` del compilador.

## Detalles de Algoritmo

Para la resolucion de este proyecto, he utilizado algoritmos recursivos. Al procesr un numero entero con peraciones aritmeticas como `num % 10` o `num % 16`, los dígitos se extraen de derecha a izquierda (desde unidades hacia arriba). La recursividad utiliza la propia pila del sistema. Al realizar la llamada recursiva `num / 10` antes de ejecutar la fuuncion `write()`, el agorito "espera" a llegar al dígito mas sigificaivo (base) para empezar a imprimir en el orden correcto.