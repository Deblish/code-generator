def genera(list):
    lista = []
    for a in list:
        if len(a) is 19:
            for i in range(100):
                nuevo = a[:len(a)-2] + "{:02d}".format(i) #por el /n
                if nuevo not in list: 
                    lista.append(nuevo)
    return lista

def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 