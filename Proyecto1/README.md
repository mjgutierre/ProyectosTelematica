# Proyecto 1
La solución a implementar debe contar con los siguientes componentes:
- El servidor PIBL.
- Tres servidores de aplicación web. La aplicación se debe replicar en los tres servidores, es decir, es la misma.

## Documentación
La documentación se debe incluir en el repo en un archivo _README.md_. En este archivo se requiere que usted incluya los detalles de implementación donde como mínimo se esperan las siguientes secciones:

  - **Introducción:**
Para el despliegue de esta practica se presentan conceptos como lo son el Proxi inverso y el balanceador de cargas para el desarrollo de una aplicación web que escuche peticiones y entregue solicitudes al usuario. 
El proxi Inverso es un servidor que se encuentra entre el cliente y el destino real de la solicitud. Consultará el recurso real al que desea acceder y le devolverá la respuesta que obtuvo después de haberlo manipulado.Al mismo tiempo, se ejecuta el balanceo de carga round robin, que es una forma sencilla de distribuir las peticiones de los clientes entre un grupo de servidores. La solicitud de un cliente se envía a cada servidor por turnos. El algoritmo indica al equilibrador de carga que vuelva al principio de la lista y se repite de nuevo.

    El balanceo de carga en redes provee escalabilidad y fácil manejo a los servicios de TCP/IP, Web, Proxy, VPN y servicios de multimedia. Este brinda un valor especial para que las empresas extiendan sus servicios de TCP/IP así como aplicaciones de e-commerce y de bases de datos. El balanceo de carga distribuye el tráfico IP a múltiples copias o instancias de servicios TCP/IP, cada uno corriendo en un host dentro de los servidores

  - **Desarrollo:**
    Para el desarrollo de la practica el PIBL fue escrito en Python. Hay muchas razones por las cuales decidimos acoger este lenguaje de programación. Excluyendo el hecho de que su sintaxis es posiblemente una de las más fáciles de entender, estas son algunas de las razones:
        - Está presente en la mayoría de los servidores "modernos"
        - Viene con un administrador de paquetes (PIP)
        - Se integra bien con el entorno virtual que se puede instalar con el permiso del usuario
        - No necesita acceso de root al servidor

    ***IMPLEMENTACION***
    - El servidor PIBL.
    - Tres servidores de aplicación web. 

    ![This is an image](https://avinetworks.com/wp-content/uploads/2019/02/round-robin-load-balancing-diagram.png)

    > Toda la arquitectura detallada en el ítem anterior fue desplegada en la nube de Amazon Web Services empleando instancias EC2 para la instalación y configuración de nuestra solución

       - La version utilizada para python es la 3.X y solo se emplearon los siguientes “import”: 
           sys, socket.
       - Se empleo la API Sockets.
       - Soporta peticiones de forma concurrente desde diferentes tipos de clientes que envíen peticiones HTTP.
       - Se procesan peticiones para la versión de protocolo HTTP/1.1.
       - El servidor escucha peticiones en el puerto 8080. 
       - Una vez envié la petición al servidor, se espera la respuesta para enviarla al cliente web que la solicito. 
       - La aplicación PIBL implementa un proceso “log” donde se registran todas las peticiones que recibe. En este sentido, el log debe permitir registrar todas las peticiones que se reciben y debe visualizar la petición que se hace y la respuesta que se entrega. Esto se debe visualizar por la salida estándar, y de igual forma, se debe implementar el registro en un archivo.
       - La función de proxy permite el caché para diferentes recursos que se soliciten por parte de los clientes. Para esto se considera lo siguiente:
        a. Para todos los recursos solicitados en las peticiones hecha por los clientes, la respuesta debe ser almacenada en en un archivo en el disco del servidor. De esta forma se garantiza que el cache persista en caso tal se presente una falla en el servidor PIBL. Así, la próxima vez que se realice la petición de este recurso, se debe acceder desde al disco y enviar la respuesta desde aquí hacia el cliente.
        b. Los recursos para almacenar en el cache deben ser localizados en el directorio donde se ejecuta la aplicación principal del PIBL.
        c. Se debe implementar un mecanismo para implementar un TTL para cada recurso que se mantenga en el cache. Esto debe ser un parámetro que se pase al momento de lanzar la aplicación.
       - Para efectos de distribución de la carga de las peticiones, la política a implementar es Round Robin.
       - Su PIBL debe tener un archivo de configuración que permita parametrizar el puerto en el que se ejecuta (p.ej., por defecto es 8080) así como incluir la lista de servidores (backend) que contestan las peticiones
    
  - **Conclusiones:**
Con este proyecto se pudo lograr la implementación de un servidor de balanceo de carga HTTP, con lo cual se logra mejorar el manejo de las peticiones HTTP simultaneas
de una forma más eficiente e inteligente; lo cual permite disminuir los tiempos de respuesta y aumentar la tasa de rendimiento de una plataforma web. 

Debido al papel clave que juegan, los servidores proxy inversos siempre se deben implementar en modo de alta disponibilidad, junto con las funciones del balanceador de carga que distribuye peticiones entre los servidores. Los requisitos para lograr estos objetivos se basaran en el contenido de configuracion de estos srvicios en donde deberan tener: 
  - Capacidad de gestionar tráfico SSL
  - Capacidad de compresión de datos
  - Failover Optimizado con opciones de alta disponibilidad
  - Almacenamiento en caché
  - Capacidad de reencriptar tráfico

  -**Funcionamiento**
  Para ejecutar el servidor utilizaremos el comando:
  
      python proxyInverse.py
     
  y despues de esto ingresaremos el puerto manualmente por el cual está escuchando nuestro servidor:
 
      8080
      
  Luego de esto estaremos viendo como se envian 3 mensajes de confirmacion y empezaremos a evidenciar el envío de solicitudes.

  - **Referencias:**
      - Round Robin Load Balancer. (2022). Avinetworks.com. https://avinetworks.com/wp-content/uploads/2019/02/round-robin-load-balancing-diagram.png
      - Create a HTTP Proxy Using Python | Hack Ed. (n.d.). Www.youtube.com. Retrieved October 30, 2022, from https://www.youtube.com/watch?v=Lhxwh30kqQ0
      

