import functions

f = open("ref.txt", "r")
refcodes = f.read().split('\n')
refcodes.sort()
generados = functions.genera(refcodes)
f2 = open("generados.txt", "w")
for i in generados: 
	f2.write("%s\n" %i)
    #print ("%s\n" %i),
f2.close()
f.close()