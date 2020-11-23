def genera(list):
    lista = []
    for a in list:
        if len(a) is 19:
            for i in range(100):
                nuevo = a[:len(a)-2] + "{:02d}".format(i) #por el /n
                if nuevo not in list: 
                    lista.append(nuevo)
    return lista