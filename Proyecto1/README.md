# Proyecto 1

La solución a implementar debe contar con los siguientes componentes:
- El servidor PIBL.
- Tres servidores de aplicación web. La aplicación se debe replicar en los tres
servidores, es decir, es la misma.

## Documentación
La documentación se debe incluir en el repo en un archivo _README.md_. En este archivo se requiere que usted incluya los detalles de implementación donde como
mínimo se esperan las siguientes secciones:

  - **Introducción:**
      Proxi inverso:Basically, a reverse proxy is a server that sit between you and the real destination of your request. It will query the real ressource you want to access for you and give you back the response it got after having tampered with it.

  - **Desarrollo:**
    Su PIBL debe ser escrito en lenguaje de programación C, Rust, Python. Debe justificar la elección de su lenguaje de programación.
      - There are many reasons why I went for python as my choice language for the implementation. Excluding the fact that it’s syntax is arguably one of the easiest to understand, here are some of the reasons:
          - It’s present on most “modern” servers
          - It comes with a package manager (PIP)
          - Integrate well with virtual environment that can be installed with user permission
          - You don’t need root access to the server
  - **Conclusiones:**
  - **Referencias:**
