import functions

f = open("ref.txt", "r")
refcodes = f.read().split('\n')
print()
functions.bubbleSort(refcodes)
generados = functions.genera(refcodes)
print ("Codigos Generados son:") 
for i in range(len(generados)): 
    print ("%s\n" %generados[i]),