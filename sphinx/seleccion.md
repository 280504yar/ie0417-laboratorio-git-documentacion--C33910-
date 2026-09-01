
# Parte 2. Selección del proyecto Python para Sphinx

## 1. Proyecto seleccionado

### Nombre

**NumPy**

### Descripción breve

NumPy es una biblioteca de software libre orientada a la computación numérica y científica en Python. Proporciona estructuras de datos y funciones para trabajar eficientemente con arreglos multidimensionales, operaciones matemáticas, álgebra lineal, transformadas, generación de números aleatorios y otras tareas de cálculo científico.

NumPy constituye uno de los proyectos fundamentales del ecosistema científico de Python y es utilizado como dependencia por una gran cantidad de bibliotecas relacionadas con ciencia de datos, ingeniería y análisis numérico.

Se trata de un proyecto público, real y ampliamente mantenido, por lo que no corresponde a un ejemplo creado específicamente para Sphinx ni a un proyecto trivial.

---

## 2. Repositorio original

Repositorio oficial:

```text
https://github.com/numpy/numpy
```

---

## 3. Licencia

NumPy se distribuye bajo una licencia permisiva de software libre de la familia:

**BSD 3-Clause**

La licencia correspondiente se encuentra incluida dentro del repositorio.

Archivo principal de licencia:

```text
LICENSE.txt
```

---

## 4. Lenguaje principal considerado

El lenguaje analizado para esta parte del laboratorio es:

**Python**

Para verificar los requisitos de tamaño se consideran principalmente los archivos:

```text
.py
```

El repositorio también contiene componentes desarrollados en otros lenguajes, pero estos no se utilizarán para comprobar el requisito de 10 000 líneas correspondientes específicamente a Python.

---

## 5. Commit exacto analizado

Después de clonar el repositorio se ejecutó:

```bash
git rev-parse HEAD
```

Resultado:

```text
7b1601b17709e616373d1f0635d6014b09fa306d
```

El hash anterior identifica exactamente la versión del proyecto que fue utilizada para realizar las mediciones y generar posteriormente la documentación.

---

## 6. Medición del tamaño del proyecto

Para medir únicamente el código Python se utilizó:

**cloc**

El comando empleado fue:

```bash
cloc . --include-lang=Python --exclude-dir=.git,build,dist,doc,benchmarks,tools
```

La salida obtenida fue:

```text
1471 text files.
    1400 unique files.                                          
     807 files ignored.

github.com/AlDanial/cloc v 2.10  T=20.39 s (33.5 files/s, 17301.3 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                         684          46990          80927         224930
-------------------------------------------------------------------------------
SUM:                           684          46990          80927         224930
-------------------------------------------------------------------------------
```

Los resultados obtenidos fueron:

| Métrica | Resultado |
|---|---:|
| Archivos Python relevantes | 684 |
| Líneas en blanco | 46990 |
| Líneas de comentarios | 80927 |
| Líneas de código Python | 224930 |

Los requisitos establecidos por el laboratorio son:

- Al menos 30 archivos `.py`.
- Al menos 10 000 líneas de código Python.

De acuerdo con los resultados obtenidos, NumPy:

**CUMPLE**

con los requisitos mínimos.

---

## 7. Alcance seleccionado para la documentación

Para la generación de documentación con Sphinx no se documentó la totalidad de los módulos internos de NumPy, debido al gran tamaño del proyecto y a que una generación completa mediante `sphinx-apidoc` incluía numerosos módulos internos, módulos de pruebas y elementos poco relevantes para el objetivo del laboratorio.

Por esta razón, se seleccionó una muestra representativa de la API pública de NumPy, compuesta por los siguientes módulos:

- `numpy`
- `numpy.linalg`
- `numpy.random`
- `numpy.fft`
- `numpy.polynomial`

Estos módulos permiten representar distintas áreas funcionales importantes del proyecto:

- `numpy`: contiene la API principal y numerosos objetos fundamentales de la biblioteca.
- `numpy.linalg`: incluye funciones relacionadas con álgebra lineal.
- `numpy.random`: contiene herramientas para generación y manejo de números aleatorios.
- `numpy.fft`: incluye funciones relacionadas con la Transformada Rápida de Fourier.
- `numpy.polynomial`: contiene clases y funciones para trabajar con polinomios.

### Justificación del alcance

Inicialmente se utilizó `sphinx-apidoc` para generar automáticamente documentación sobre una parte más amplia del paquete. Sin embargo, esta estrategia incluía una gran cantidad de módulos internos y de pruebas, lo que provocaba numerosas advertencias durante la construcción y producía documentación demasiado extensa para el propósito del laboratorio.

Por este motivo, se decidió concentrar la documentación final en módulos públicos representativos que permitieran evaluar correctamente el funcionamiento de Sphinx y sus extensiones sin intentar reproducir toda la infraestructura de documentación oficial de NumPy.

La selección mantiene suficiente variedad para analizar:

- generación automática de documentación mediante `autodoc`;
- interpretación de docstrings con `numpydoc`;
- organización de módulos mediante archivos `.rst`;
- navegación mediante `toctree`;
- documentación de funciones, clases, métodos y otros objetos públicos;
- parámetros, tipos de datos, valores de retorno y excepciones presentes en los docstrings;
- enlaces hacia el código fuente mediante `viewcode`, cuando es técnicamente posible.


---

## 8. Razón por la cual NumPy es apropiado para Sphinx

NumPy resulta especialmente adecuado para Sphinx porque su código Python posee una gran cantidad de módulos, funciones, clases y objetos públicos acompañados por docstrings estructurados.

Sphinx permite generar documentación de API utilizando extensiones como:

```text
sphinx.ext.autodoc
sphinx.ext.autosummary
```

Además, el formato de docstrings utilizado por NumPy puede procesarse mediante:

```text
numpydoc
```

Los docstrings de NumPy suelen incluir apartados como:

- Parameters.
- Returns.
- Raises.
- See Also.
- Notes.
- References.
- Examples.

Esto permite que Sphinx transforme la información escrita directamente en el código fuente en documentación HTML organizada y navegable.

Por esta razón, NumPy constituye un proyecto apropiado para evaluar tanto documentación narrativa como documentación generada automáticamente a partir de la API.

---

## 9. Presencia inicial de docstrings

Antes de generar la documentación se revisaron varios archivos Python del proyecto.

Archivos revisados:

```text
numpy/_core/multiarray.py
numpy/ma/core.py
numpy/linalg/_linalg.py
```

Ejemplo de docstring encontrado:

```python
 """
    Dot product of two arrays.

    Parameters
    ----------
    a : array_like
        First argument.
    b : array_like
        Second argument.
    out : ndarray, optional
        Output argument.

    Returns
    -------
    output : ndarray
        Returns the dot product of `a` and `b`.
    """
```

### Calidad inicial de los docstrings

La calidad de los docstrings se considera:

**ALTA**

Justificación:

La calidad se considera alta porque una gran parte de las funciones públicas contiene documentación estructurada con descripción, parámetros, valores retornados, notas y ejemplos. Esto permite que herramientas como Sphinx y numpydoc generen documentación útil a partir del código fuente sin necesidad de agregar manualmente toda la información.

---

## 10. Dependencias y dificultades previstas

Durante la generación de la documentación se prevén las siguientes dificultades:

1. NumPy contiene componentes Python y componentes compilados.
2. Algunas partes del paquete pueden requerir que NumPy se encuentre correctamente instalado para que Sphinx pueda importarlas.
3. El uso de `autodoc` puede generar advertencias si algún módulo no puede importarse.
4. La documentación oficial utiliza varias extensiones adicionales que no necesariamente son requeridas para este laboratorio.
5. Será necesario crear un entorno virtual para evitar modificar la instalación global de Python.
6. Algunas dependencias utilizadas por la documentación pueden necesitar instalarse mediante `pip`.
7. El repositorio posee una cantidad considerable de módulos, por lo que generar toda la API puede producir una documentación extensa.
8. Será necesario excluir directorios que no representen código fuente relevante para las métricas.

Entre las principales dependencias previstas se encuentran:

```text
Sphinx
numpydoc
```

---

## 11. Entorno virtual

Para aislar las dependencias utilizadas para la documentación se creará un entorno virtual.

### Crear el entorno

En Windows:

```bash
python -m venv .venv
```

### Activarlo en PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Activarlo en CMD

```cmd
.venv\Scripts\activate.bat
```

### Activarlo en Linux/macOS

```bash
source .venv/bin/activate
```

---

## 12. Dependencias de documentación

Las dependencias principales podrán instalarse mediante:

```bash
python -m pip install sphinx numpydoc
```

---

## 13. Herramientas utilizadas

| Herramienta | Versión |
|---|---|
| Git | version 2.50.1.windows.1 |
| Python | 3.12.0 |
| cloc | 2.10 |
| Sphinx | 9.1.0 |
| numpydoc | 1.10.0 |

Los comandos para consultar las versiones fueron:

```bash
git --version
python --version
cloc --version
sphinx-build --version
python -m pip show numpydoc
```