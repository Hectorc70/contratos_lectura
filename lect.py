from pdf import ArchivoPdf
from buscador import Buscador
from rutas import Rutas, unir_cadenas

"""patrones = ['CONTROL: [0123456789]{8}',
						'PERIODO:[0123456789]{1,2}/[0123456789]{4}'
						] """


ruta = '2.pdf'
_carpeta = 'C:\\Users\\Usuario\\Documents\\NOMINAS\\TRABAJOS_2021\\12\\HONORARIOS_RESTANTES'

def eje(carpeta):
    patron_periodo = '[0123456789]{2}/[0123456789]{2}/[0123456789]{4} al [0123456789]{2}/[0123456789]{2}/[0123456789]{4}'
    #patron_importe = '$[0123456789]+'
    #patron_importe = '$[0123456789]+,[0123456789]+.[0123456789]{2}'
    patron_importe = '[0123456789]+,[0123456789]{3}.[0123456789]{2}'
    patron_nombre = "PARTE, ^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"

    patrones = [patron_periodo, patron_importe]

    directorio = Rutas()
    archivos_rutas = directorio.recuperar_rutas(carpeta, split=True)

    datos_archivo = list()

    for i in archivos_rutas:
        nombre_archivo = i[-1]
        extencion = nombre_archivo.split('.')[-1]

        if extencion == 'pdf':
            ruta_completa = unir_cadenas('\\', i)
            
            nombre = extraer(patron_nombre, ruta_completa)
            #importe = extraer(patron_importe, ruta_completa)
            #cadena = nombre_archivo + '|' + str(nombre) + '|' + str(importe)
            cadena = nombre_archivo + '|' + str(nombre) + '|'
            print(cadena)



def extraer(patron, ruta):

    archivo =  ArchivoPdf(ruta)
    contenido = archivo.extraer_contenido()
    
    extraer_texto = lambda pos_i, pos_f, texto: texto[pos_i:pos_f]
    for hoja in contenido.values():
        buscador = Buscador(patron, str(hoja[0]))
        posiciones = buscador.buscar()

        if posiciones != None:
            texto_encontrado = extraer_texto(
                            posiciones[0], posiciones[1], str(hoja[0]))
            
            return texto_encontrado

        else:
            continue


def extraer_importe(patron):

    archivo =  ArchivoPdf(ruta)
    contenido = archivo.extraer_contenido()
    
    extraer_texto = lambda pos_i, pos_f, texto: texto[pos_i:pos_f]
    data = list()
    for hoja in contenido.values():
        buscador = Buscador(patron, str(hoja[0]))
        posiciones = buscador.buscar()

        if posiciones != None:
            texto_encontrado = extraer_texto(
                            posiciones[0], posiciones[1], str(hoja[0]))

            
            
            data.append(texto_encontrado)

            
            

        else:
            continue

    return data[-1]
eje(_carpeta)

