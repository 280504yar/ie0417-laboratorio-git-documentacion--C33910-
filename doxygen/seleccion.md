# Parte 2. Selección del proyecto C++ para Doxygen

## 1. Proyecto seleccionado

### Nombre

**OpenCV (Open Source Computer Vision Library)**

### Descripción breve

OpenCV es una biblioteca de software libre orientada principalmente a visión por computadora, procesamiento de imágenes y aprendizaje automático. El proyecto contiene numerosos módulos para trabajar con imágenes, video, detección de características, transformaciones geométricas, procesamiento numérico y otras aplicaciones relacionadas con visión artificial.

Se trata de un proyecto real, mantenido públicamente y utilizado ampliamente en entornos académicos, industriales y de investigación, por lo que no corresponde a un ejemplo creado específicamente para Doxygen ni a un proyecto trivial.

---

## 2. Repositorio original

Repositorio oficial:

```text
https://github.com/opencv/opencv
```

---

## 3. Licencia

OpenCV se distribuye bajo la licencia:

**Apache License 2.0**

Esta es una licencia de código abierto permisiva que permite utilizar, modificar y redistribuir el software bajo las condiciones establecidas en la licencia.

Archivo de licencia dentro del repositorio:

```text
LICENSE
```

---

## 4. Lenguaje principal

El lenguaje principal considerado para este laboratorio es:

**C++**

OpenCV contiene principalmente archivos fuente con extensiones como:

```text
.cpp
.hpp
.h
.cc
```

La mayor parte del código correspondiente a los módulos principales se encuentra dentro del directorio:

```text
modules/
```

---

## 5. Commit exacto analizado

Después de clonar el repositorio se ejecutó el siguiente comando:

```bash
git rev-parse HEAD
```

Resultado:

```text
390c4fdcb9fea6e58fb635bf88277f2a51e8d4b3
```

Este valor corresponde al commit exacto utilizado durante el análisis y permite reproducir posteriormente la misma versión del proyecto.

---

## 6. Medición del tamaño del proyecto

Para comprobar que el proyecto cumple con los requisitos mínimos del laboratorio se utilizó la herramienta:

**cloc**

El comando utilizado fue:

```bash
cloc modules --include-lang="C++","C/C++ Header" --exclude-dir=test,perf,doc,samples
```

La salida obtenida fue:

```text
> git rev-parse HEAD
390c4fdcb9fea6e58fb635bf88277f2a51e8d4b3
PS C:\Users\YARADEYENISAIZAGUIRR\opencv> cloc modules --include-lang="C++","C/C++ Header" --exclude-dir=test,perf,doc,samples
    2058 text files.
    2004 unique files.                                          
     592 files ignored.

github.com/AlDanial/cloc v 2.10  T=28.62 s (53.5 files/s, 30409.9 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
C++                            706          62619          38939         393005
C/C++ Header                   825          43239          64745         267912
-------------------------------------------------------------------------------
SUM:                          1531         105858         103684         660917
-------------------------------------------------------------------------------
```

De acuerdo con la medición realizada:

| Métrica | Resultado |
|---|---:|
| Archivos fuente C++ y cabeceras relevantes | 1531 |
| Líneas en blanco | 105858 |
| Líneas de comentarios | 103684 |
| Líneas de código fuente | 660917 |

El laboratorio establece como requisito mínimo:

- 30 archivos fuente relevantes.
- 10 000 líneas de código fuente.

Por lo tanto, con los resultados anteriores se determina que OpenCV:

CUMPLE

con los requisitos mínimos establecidos.

---

## 7. Alcance seleccionado para la documentación

Para la generación de la documentación con Doxygen se utilizará el proyecto completo, tomando como alcance principal el directorio:

```text
modules/
```

### Justificación del alcance

> Se decidió utilizar el proyecto completo debido a que el proceso de generación de documentación resultó viable en el equipo utilizado. Se excluirán únicamente directorios correspondientes a pruebas, ejemplos, documentación previa, dependencias externas y archivos generados que no forman parte del código fuente relevante para el análisis.

---

## 8. Razón por la cual OpenCV es apropiado para Doxygen

OpenCV resulta apropiado para Doxygen porque está compuesto principalmente por código C++ organizado mediante clases, funciones, estructuras, enumeraciones, namespaces y módulos.

Doxygen puede analizar directamente este tipo de construcciones y producir documentación técnica de elementos como:

- Clases.
- Métodos.
- Funciones.
- Estructuras.
- Variables.
- Enumeraciones.
- Namespaces.
- Archivos fuente.
- Relaciones entre clases.
- Jerarquías.
- Dependencias entre elementos.

Además, OpenCV posee comentarios estructurados en una parte importante de sus interfaces públicas, lo que permite que Doxygen genere documentación con información más significativa que una simple lista de símbolos.

La organización modular de OpenCV también permite analizar de forma clara cómo Doxygen representa un proyecto C++ de tamaño considerable.

---

## 9. Presencia inicial de comentarios Doxygen

Antes de generar la documentación se revisaron algunos archivos del proyecto para identificar el nivel de documentación existente.

Archivo(s) revisado(s):

```text
modules/core/include/opencv2/core.hpp
modules/imgproc/include/opencv2/imgproc.hpp
modules/features2d/include/opencv2/features2d.hpp
```
Se observaron elementos como:

- @brief
- @param
- @return
- @note
- @see


Ejemplo de comentario encontrado:

```cpp

/** @brief Finds the real roots of a cubic equation.

The function solveCubic finds the real roots of a cubic equation:
-   if coeffs is a 4-element vector:
\f[\texttt{coeffs} [0] x^3 +  \texttt{coeffs} [1] x^2 +  \texttt{coeffs} [2] x +  \texttt{coeffs} [3] = 0\f]
-   if coeffs is a 3-element vector:
\f[x^3 +  \texttt{coeffs} [0] x^2 +  \texttt{coeffs} [1] x +  \texttt{coeffs} [2] = 0\f]

The roots are stored in the roots array.
@param coeffs equation coefficients, an array of 3 or 4 elements.
@param roots output array of real roots that has 0, 1, 2 or 3 elements.
@return number of real roots. It can be -1 (all real numbers), 0, 1, 2 or 3.
*/

 /** @brief finds arbitrary template in the grayscale image using Generalized Hough Transform
*/




```

### Evaluación de la calidad inicial

La calidad inicial de los comentarios se considera:

**ALTA**

Justificación:

La calidad se considera alta en las interfaces públicas, ya que muchas funciones y clases contienen descripciones, información sobre parámetros y explicaciones sobre su comportamiento. Sin embargo, algunos componentes internos poseen comentarios menos detallados, por lo que la calidad de documentación no es completamente uniforme en todo el proyecto.

---

## 10. Dependencias y dificultades previstas

Durante la generación de la documentación se prevén las siguientes dificultades:

1. OpenCV contiene una gran cantidad de archivos fuente, por lo que la generación completa puede requerir un tiempo considerable.
2. El repositorio incluye directorios de pruebas, ejemplos y documentación existente que no necesariamente deben incorporarse a la nueva documentación.
3. Algunas partes del proyecto pueden hacer referencia a dependencias externas.
4. El uso de Graphviz para generar diagramas puede aumentar considerablemente el tiempo de procesamiento.
5. Una configuración de Doxygen demasiado general puede producir una gran cantidad de archivos HTML.
6. Algunos elementos internos pueden no poseer comentarios estructurados suficientes.
7. Es necesario excluir archivos generados y dependencias vendorizadas para evitar alterar las métricas y la calidad de la documentación.
   
Entre las dependencias más comunes se encuentran:

- **CMake**, utilizado para configurar y generar el sistema de compilación.
- **Python**, utilizado por algunas herramientas y scripts auxiliares.
- **Graphviz**, necesario para generar diagramas cuando se utiliza Doxygen
  con opciones gráficas.
- Bibliotecas para procesamiento de imágenes, como **libjpeg**, **libpng**,
  **libtiff** y **WebP**.
- Bibliotecas para video y multimedia, como **FFmpeg** o **GStreamer**.
- Bibliotecas matemáticas y de optimización, como **Eigen** en determinados
  componentes.
- Bibliotecas del sistema y dependencias opcionales asociadas a módulos
  específicos.


---

## 11. Herramientas utilizadas

Las herramientas empleadas durante esta etapa fueron:

| Herramienta | Versión |
|---|---|
| Git | 2.50.1.windows.1 |
| cloc | 2.10 |
| Doxygen | 1.18.0 |
| Graphviz | 16.0.0 |

Los comandos para consultar las versiones fueron:

```bash
git --version
cloc --version
doxygen --version
dot -V
```