# Network-Tracking-en-Python
Basado en el tutorial de **Vinsloev Academy** cuyo programa tiene el proposito de capturar, procesar y visualizar el tráfico en la red haciendo uso de Wireshark, GeoLiteCity Database y Google Maps.
A diferencia del programa original a este se le añadio:
<li>La obtencion de ip publica automatica</li>
<li>La obtencion automatica de un archivo kml</li>

## Wireshark
<li>Seleccionar la red que vas a capturar</li> 
<li>Despues de unos segundos deten la captura de paquetes</li>
<li>En Archivo, selecciona exportar paquetes especificados y seleciona el tipo de archivo tcpdump//... pcap</li> 

![image](https://github.com/user-attachments/assets/0d1bac1e-5a50-473e-bc86-201d966e9b82)

<li>Guarda el archivo en la misma raiz que el main.py</li>
 
## GeoLiteCity Database
<li>Descarga el GeoLiteCity database de https://github.com/mbcc2006/GeoLiteCity-data</li> 
<li>Añadelo a la misma raiz que el main.py</li>

## Google Maps

Al ejecutar el codigo se se creara un archivo de tipo kml, el cual debera ser agregado a google maps:

<li>Ingresa a Google My Maps https://www.google.com/maps/d/u/0/</li>
<li>Selecciona  crear un mapa nuevo</li>
<li>Selecciona importar y añade el archivo kml</li>

![image](https://github.com/user-attachments/assets/4fa75eb7-5d29-4ea6-92c5-274dab667fa5)




