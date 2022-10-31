# Proyecto 2. Despliegue e integración de Servicios 
Paulina Ocampo Duque - Maria Jose Gutierrez Estrada 


## Objetivo:
> Desarrollar habilidades en la configuración, así como despliegue de aplicaciones y servicios en red, particularmente las que requieren de una arquitectura cliente/servidor
 
## Problemática 
La empresa MiCompany S.A., requiere de un mecanismo basado en tecnologías de información (TI) que le permita capturar la opinión de los consumidores en relación con 
los diferentes productos que tienen en el mercado, para darle solución a este problema se decidió implementar y desplegar una aplicación web. 

**Productos utilizados para el desarrollo del software**
- **AWS:** conjunto de herramientas y servicios de computación en la nube de Amazon 
- **Amazon RDS database:** es un servicio web que facilita la configuración, la operación y la escala de una base de datos relacional en Nube de AWS. Proporciona una capacidad rentable y de tamaño ajustable para una base de datos relacional estándar y se ocupa de las tareas de administración de bases de datos comunes, permite la escalabilidad horizontal y ofrece copias de seguridad automatizadas. 
- **Direcciones IP elásticas AWS:** son direcciones IPv4 estáticas diseñadas para la informática en la nube dinámica. Con una dirección IP elástica, puede enmascarar los errores de una instancia o software volviendo a mapear rápidamente la dirección a otra instancia de su cuenta. 
- **Balanceador de cargas AWS: distribuye automáticamente el tráfico de aplicaciones entrantes entre varios destinos y dispositivos virtuales en una o varias zonas de disponibilidad 
- **Amazon Linux 2:** proporciona un entorno de ejecución estable, seguro y de alto rendimiento para las aplicaciones que se ejecutan en Amazon EC2 
- **Wordpress:** es un software de código abierto que se puede usar para crear un sitio web, un blog o una aplicación. 
- **MariaDB:** es un sistema de gestión de bases de datos relacional, derivado de MySQL. 
- **Freenom:** proveedor de dominios gratuitos 
 

## Vista arquitectónica y despliegue de la aplicación

**Creación de instancias Amazon**
  - Creamos una instancia Amazon EC2 en la consola de AWS y utilizamos la AMI de Amazon Linux 2 para lanzarla en un entorno virtual 

**Creación de dirección estática**
  - Vamos a la sección de ip elásticas y asignamos una dirección nueva, la seleccionamos y la asociamos a nuestra instancia 

**Creación de base de datos MySQL con RDS**
  - En la configuración de Amazon RDS se elegirá el motor de base de datos que utilizaremos, en nuestro caso MySQL, debido a que WordPress utiliza esta base de datos. Para la configuración de conectividad y red, se creará una VPC (red separada lógicamente) en donde estarán los recursos aprovisionados.   

En el grupo de seguridad de la VPC cambiamos la propiedad y la regla que permite todo el tráfico por MYSQL/Aurora y en la fuente ponemos el grupo de seguridad que estaba asociado a la instancia. 

**Conexión de la instancia EC2 a través de SSH**  
En un primer momento debemos verificar que estemos ubicado en la carpeta donde se guardan las llaves. Para luego iniciar la máquina virtual de la instancia principal escribimos el siguiente comando 

    ssh -i "Practica.pem" ec2-user@ec2-34-236-19-101.compute-1.amazonaws.com 

Una vez iniciada la instancia, instalamos MySQL a través de los comandos:  

    sudo yum install -y mysql 

Para establecer una variable de entorno para nuestro anfitrion utilizamos este comando: 

    export MYSQL_HOST=wordpress.cxxkjny6wlnd.us-east-1.rds.amazonaws.com 

Para conectar la base de datos, el siguiente comando: 

    mysql --user=admin --password=**** wordpress 


**Configuración de WordPress con EC2**

Para desplegar este servicio instalaremos e iniciaremos Apache con los siguientes comandos: 

    sudo yum install -y httpd 

Inicializar
   
    sudo service httpd start 

Luego descargaremos WordPress:  

    wget https://wordpress.org/latest.tar.gz 

    tar -xzf latest.tar.gz 
    
y editaremos la configuración de la base datos: 

    nano wp-config.php 

**Implementación de WordPress**

Instalaremos las dependencias de la aplicación que se necesita para WordPress: 

    sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2 

Copiaremos los archivos de la aplicación de WordPress que Apache utiliza para luego reiniciarlo: 

    sudo cp -r wordpress/* /var/www/html/  

    sudo service httpd restart 

**Creación de página web**

En WordPress realizamos un catálogo de productos de maquillaje en el cual un usuario puede dejar su comentario, el formulario para los comentarios lo hicimos con un plugin que ofrece WordPress para personalizarlo. 

**Clonación de instancia**

Copiaremos la AMI de nuestra instancia principal y luego lanzaremos nuestra segunda instancia que ya estará asociada a la base de datos y a la información que tenemos en WordPress. 

**Creación de balanceador de cargas**

Asociaremos nuestras dos instancias a través de un grupo de destino para luego crear el balanceador de cargas que ofrece AWS 

**DNS**

Para escoger los dominios utilizamos un proveedor llamado freenom y cambiamos el nombre del host del sistema, agregando unos permisos en el .vim desde la terminal. 

## Implementación  

Al ser un servidor desplegado en la nube, no hay necesidad de iniciar localmente este mismo, solo hay que ingresar a la dirección y revisar su contenido el cual fue generado con las especificaciones y necesidades de la problemática presentada en el proyecto.  

    http://primarymakeupcompany.tk/ 

    http://secondmakeupcompany.tk/  

## Referencias  
https://www.ticportal.es/temas/cloud-computing/amazon-web-services 
https://docs.aws.amazon.com/es_es/AmazonRDS/latest/UserGuide/Welcome.html 
https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html 
https://aws.amazon.com/es/elasticloadbalancing/ 
https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html 
https://www.incosa.com.uy/blog/que-es-mariadb/ 
https://es-co.wordpress.org/ 
https://www.freenom.com/es/aboutfreenom.html 

**Referencias imágenes**

https://images.app.goo.gl/msnvBgeJq5bUmDwK9 
https://images.app.goo.gl/HJwxvWsC5ssK1dsn6 
https://images.app.goo.gl/SyG6BUNjsL4Tqst47 
https://images.app.goo.gl/g95w6Nr55NTrzT7c9 
https://images.app.goo.gl/Lazg43ixCn5R8EJx8 
https://images.app.goo.gl/E9GcWNbM8wCEn9KC8 
https://images.app.goo.gl/RbFBRF4YBbGWr9fo7 
https://images.app.goo.gl/7Yt6XYQFznScfKoo9 
https://images.app.goo.gl/u7k2HFKm4LLxeR8r8 
https://images.app.goo.gl/WciWzdmaW39kAPn7A 
https://images.app.goo.gl/vJcMkxUQuRhGzovq7 
https://images.app.goo.gl/qdx9sbBDt8d62tvEA 
https://images.app.goo.gl/JSameA761w18sneb7 

 

 

 

 
