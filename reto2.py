"""
Creacion de Algoritmo para encontrar clave:

ej:
-las palabras aabbabbaba, abbabababa y bbabbabab. 
 Contraseña oculta es abbaba, ya que esta es la subpalabra común más larga.

Problematica:
-Ayudar a K a encontrar una clave en un juego de palabras

RF01:
Crear Algoritmo:

input:
Cuatro lineas:
1.linea = tres enteros " M, N y K
2.linea = palabra con letras M
3.linea = palabras con letra N
4.linea = palabras con letra K
output:
1.linea = sub palabra mas comun mas larga, entre las tres palabras de entrada
si hay mas de una subpalabra comun mas larga informe cualquiera.

Datos de prueba:
-N,M,K <= 300 en el 80% de la entradas
-N,M,K <= 2000

"""
# Crear un for para recorrer los strings de prueba
# Crear una lista y agragar elementos con coinsidencia
# Castirlo a string y retornarlo
def matches(lis_uno, lis_dos):
    set(lis_uno) & set(lis_dos)



def find_password(p_uno,p_dos, p_tres):
    #convertimos string en listas
    p_u = list(p_uno)
    p_d = list(p_dos)

    #Se crean listas vaias para agragar de uno en uno los similares
    res_uno =[]
    res_dos = []


    j =0
    b =0

    # Se usa el for para recorrer la lista con la cantidad de posiciones de los 10 caracteres
    for i in p_u:
        # se suma y se resta j para ir avanzando de uno en uno
        pp_o = p_u[0+j:1+j]
        # Se guarda en otra lista el resultado
        res_uno.append(pp_o)
        j+=1

    #mismo proceso para el segundo string
    for a in p_d:
        pp_t = p_d[0+b:1+b]
        res_dos.append(pp_t)
        b +=1
    
 

    res_zip = []
    #Con el metodo zip juntamos las dos listas con la condicion de que sean igual
    for h,t in zip(res_uno,res_dos):
        if h == t:
            #obtenemos el resultado en lista de listas 
            res_zip.append(t)
    
    s =""
    # Creamos un string vacion para generear el resultado en str
    for i in res_zip:
        #Con el metodo join pasamos de una lista a un string y lo guardamos en la variable s
        restultado = ''.join(i)
        s+=restultado
    
    #recorremos las tres palabras para constatar que si es la clave esperada
    
    res_uno = s in p_uno
    res_dos = s in p_dos
    res_tres = s in p_tres

    print(f"""
    El resultados {s} en {p_uno} es: {res_uno}
    El resultados {s} en {p_dos} es: {res_dos}
    El resultados {s} en {p_tres} es: {res_tres}
    """)


find_password("aabbabbaba","abbabababa","bbabbabab")