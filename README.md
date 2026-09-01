# Laboratorio 01 - Control de versiones y documentación automática de software

## Información del estudiante

- **Nombre:** [Yara Izaguirre Pérez]
- **Carné:** [C33910]

---

## Información del curso

- **Curso:** IE0417 - Diseño de Software para Ingeniería
- **Laboratorio:** Laboratorio 01 - Control de versiones y documentación automática de software

---

## Repositorio de entrega

Repositorio del laboratorio en GitHub:

[URL_DEL_REPOSITORIO](https://github.com/280504yar/ie0417-laboratorio-git-documentacion--C33910-.git)

---

## Sitio público

La documentación generada durante el laboratorio se encuentra publicada en:

[https://lab01documentacion.netlify.app/](https://lab01documentacion.netlify.app/)

### Enlaces directos

- **Documentación C++ - OpenCV con Doxygen:**  
  [https://lab01documentacion.netlify.app/cpp/](https://lab01documentacion.netlify.app/cpp/)

- **Documentación Python - NumPy con Sphinx:**  
  [https://lab01documentacion.netlify.app/python/](https://lab01documentacion.netlify.app/python/)

---

## Contenido del repositorio

| Parte | Enlace |
|---|---|
| Parte I | [Learn Git Branching](git/learn-git-branching.md) |
| Parte II | [Selección del proyecto C++](doxygen/seleccion.md) |
| Parte II | [Selección del proyecto Python](sphinx/seleccion.md) |
| Partes III, IV, V y VI | [Informe de Doxygen, Sphinx, comparación y publicación](informe.md) |


## Proyectos seleccionados y repositorios originales

### OpenCV

Proyecto utilizado para la documentación en C++ mediante Doxygen.

- **Proyecto:** OpenCV (Open Source Computer Vision Library)
- **Lenguaje:** C++
- **Repositorio original:** [https://github.com/opencv/opencv](https://github.com/opencv/opencv)

### NumPy

Proyecto utilizado para la documentación en Python mediante Sphinx.

- **Proyecto:** NumPy
- **Lenguaje:** Python
- **Repositorio original:** [https://github.com/numpy/numpy](https://github.com/numpy/numpy)

---

## Instrucciones breves para regenerar ambas documentaciones

### Doxygen - OpenCV

La configuración de Doxygen se encuentra en:

`doxygen/Doxyfile`

Para regenerar la documentación:

```bash
doxygen doxygen/Doxyfile
```

La documentación HTML se genera en:

`site/cpp/`

El registro de generación se guarda en:

`doxygen/build.log`

### Sphinx - NumPy

Primero se debe crear y activar un entorno virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Luego se instalan las dependencias:

```powershell
python -m pip install -r sphinx\requirements-docs.txt
```

Finalmente se genera la documentación:

```powershell
sphinx-build -E -a -b html sphinx\source site\python 2>&1 | Tee-Object -FilePath sphinx\build.log
```

La documentación HTML se genera en:

`site/python/`

El registro de generación se guarda en:

`sphinx/build.log`

---

## Versiones de las herramientas utilizadas

| Herramienta | Versión |
|---|---|
| Git | 2.50.1.windows.1 |
| cloc | 2.10 |
| Doxygen | 1.18.0 |
| Graphviz | 16.0.0 |
| Python | 3.12.0 |
| Sphinx | 9.1.0 |
| numpydoc | 1.10.0 |
| NumPy | 2.5.2 |