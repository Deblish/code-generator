import functions

f = open("ref.txt", "r")
refcodes = f.read().split('\n')
f.close()
refcodes.sort()
generados = functions.genera(refcodes)
f = open("generados2.txt", "w")
for i in generados: 
	f.write("%s\n" %i)
    #print ("%s\n" %i),
f.close()