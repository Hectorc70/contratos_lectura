from pdf_to_text import convert_pdf_to_txt
from pdf import ArchivoPdf
from buscador import Buscador
from rutas import Rutas, unir_cadenas
from txt import ArchivoTxt




ruta = '2.pdf'
_carpeta = 'C:\\Users\\Usuario\\Documents\\NOMINAS\\TRABAJOS_2021\\12\\HONORARIOS_RESTANTES\\PRUEBAS'
_carpeta = 'C:\\Users\\Usuario\\Documents\\NOMINAS\\TRABAJOS_2021\\12\\HONORARIOS_RESTANTES\\TXT'

def eje2(carpeta):
    patron_periodo = '[0123456789]{2}/[0123456789]{2}/[0123456789]{4} al [0123456789]{2}/[0123456789]{2}/[0123456789]{4}'
    #patron_importe = '$[0123456789]+'
    #patron_importe = '$[0123456789]+,[0123456789]+.[0123456789]{2}'
    patron_importe = '[0123456789]+,[0123456789]{3}.[0123456789]{2}'
    #patron_nombre = "PARTE, ^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"
    #patron_nombre = 'OTRA PARTE, [A-Z]+ [A-Z]+ [A-Z]+'
    patron_nombre = 'OTRA PARTE, [ A-Za-zäÄëËïÏöÖüÜáéíóúáéíóúÁÉÍÓÚÂÊÎÔÛâêîôûàèìòùÀÈÌÒÙ.-]+ [ A-Za-zäÄëËïÏöÖüÜáéíóúáéíóúÁÉÍÓÚÂÊÎÔÛâêîôûàèìòùÀÈÌÒÙ.-]+ [ A-Za-zäÄëËïÏöÖüÜáéíóúáéíóúÁÉÍÓÚÂÊÎÔÛâêîôûàèìòùÀÈÌÒÙ.-]+'
    patron_per = 'dia [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+ [a-z]+'
    patron_anno = 'de dos mil [a-z]+, pudiéndose para tal efecto' 
    patron_nac = 'haber nacido el día [a-z]+ [a-z]+ [a-z]+ [a-z]+ \n [a-z]+ [a-z]+,' 
    patron_curp = '[0-9A-Z]{18}' 
    patron_ine = 'folio [0-9A-Z]+'
    patron_rfc = 'n[u-ú]mero [0-9A-Z]{13}'
    patrones = [patron_periodo, patron_importe]

    directorio = Rutas()
    archivos_rutas = directorio.recuperar_rutas(carpeta, split=True)

    datos_archivo = list()

    for i in archivos_rutas:
        nombre_archivo = i[-1]
        extencion = nombre_archivo.split('.')[-1]

        if extencion == 'txt':
            ruta_completa = unir_cadenas('\\', i)
            
            nombre = extraer(patron_nombre, ruta_completa)
            periodo = extraer(patron_per, ruta_completa)
            anno = extraer(patron_anno, ruta_completa)
            curp = extraer(patron_curp, ruta_completa)
            rfc = extraer(patron_rfc, ruta_completa)
            ine = extraer(patron_ine, ruta_completa)
            nac = extraer(patron_nac, ruta_completa)
            
            #importe = extraer(patron_importe, ruta_completa)
            #cadena = nombre_archivo + '|' + str(nombre) + '|' + str(importe)
            cadena = nombre_archivo + '|' + str(nombre) + '|' + str(periodo) + '|' + str(anno)  +'|' + str(curp) + '|' + str(rfc) + '|'+ str(ine) + '|' + str(nac)
            """ cadena = unir_cadenas('|'[nombre_archivo, nombre, periodo, anno, curp]) """
            txt = ArchivoTxt('datos2.txt')
            txt.escribir(cadena)
            print(cadena)



def extraer(patron, ruta):
    txt = ArchivoTxt(ruta)
    text = txt.leer(lineas=True)
    
    
    extraer_texto = lambda pos_i, pos_f, texto: texto[pos_i:pos_f]
    for text_pdf in text:
        buscador = Buscador(patron, text_pdf)
        posiciones = buscador.buscar()

        if posiciones != None:
            texto_encontrado = extraer_texto(
                            posiciones[0], posiciones[1], text_pdf)
            
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
eje2(_carpeta)

