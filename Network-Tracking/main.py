'''Librerias'''
import dpkt
import socket
import pygeoip
import requests
import json

'''Inicializar'''
gi = pygeoip.GeoIP('GeoLiteCity.dat')


'''Obtener IP publica'''
def get():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)
    if response.status_code != 200:
        return 'Status:', response.status_code, 'Hubo un problema con el request. Saliendo.'
        exit()
    data = response.json()
    return data['ip']
my_ip = get()

#Visualizar IP Publica
#print(my_ip)


'''Metodo main'''

def main():
    #En este ejemplo el archivo pcap se llama wire
    f = open('wire.pcap', 'rb')
    pcap = dpkt.pcap.Reader(f)
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
    '<Style id="transBluePoly">' \
                '<LineStyle>' \
                '<width>2.2</width>' \
                '<color>cc000000</color>' \
                '</LineStyle>' \
                '</Style>'
    kmlfooter = '</Document>\n</kml>\n'
    kmldoc=kmlheader+plotIPs(pcap)+kmlfooter
    #print(kmldoc)
    return kmldoc

'''Geo locations'''
def retKML(dstip, srcip):
    dst = gi.record_by_name(dstip)#Destino
    src = gi.record_by_name(my_ip)#Duente
    try:
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        srclongitude = src['longitude']
        srclatitude = src['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        )%(dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml
    except:
        return ''
    


'''Extraer direcciones IP'''
def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            KML = retKML(dst, src)
            kmlPts = kmlPts + KML
        except:
            pass
    return kmlPts


if __name__ == '__main__':
    kml_content = main()



'''Transformar output a un archivo kml'''
def write_to_kml(file_path, kml_content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(kml_content)
kml_content = main()

#obtencion del nombre del archivo
output_file = 'output.kml'

#Obtencion de kml
write_to_kml(output_file, kml_content)

'''Mensajes'''
print(f"\nArchivo KML generado con el nombre: {output_file}")

print("\nAñadir el archivo kml en:   https://www.google.com/maps/d/u/0/\n")