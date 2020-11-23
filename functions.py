import linecache

def genera(list):
    lista = []
    for a in list:
        if len(a) == 19:
            for i in range(100):
                nuevo = a[:len(a)-2] + "{:02d}".format(i) #por el /n
                if nuevo not in list: 
                    lista.append(nuevo)
    return lista

def get_apuntador():
	f = open("apuntador.txt", "r")
	ap = int(f.read())
	f.close()
	return ap

def get_codigo():
	apuntador = get_apuntador()
	return linecache.getline('generados.txt', apuntador)

def siguiente():
	apuntador = get_apuntador()
	f = open("apuntador.txt", "w")
	f.write(str(apuntador+1))
	f.close()

def anterior():
	apuntador = get_apuntador()
	f = open("apuntador.txt", "w")
	f.write(str(apuntador-1))
	f.close()

