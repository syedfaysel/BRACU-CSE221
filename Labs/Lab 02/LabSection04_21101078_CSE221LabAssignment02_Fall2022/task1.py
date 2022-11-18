

with open("input1.txt", 'r') as file_in:
    
    n = int(file_in.readline())
    
    ids = file_in.readline()
    marks = file_in.readline()
    
    ids = list(map(int, ids.split()))
    marks = list(map(int, marks.split()))
    
    
    # INSERTION SORT - REVERSE OR DESCENDING
    
    def reverse_ins(array):
        
        for j in range(1, len(array)):
            
            key = array[j]
            # Insert array[j] into the sorted sequence A[0...j-1]
            
            i = j-1
            while(i>=0 and array[i]<key):
                
                array[i+1] = array[i]   # Right shifting elements
                
                i = i-1
            
            array[i+1] = key  # putting a[j] or key in the right place
            
            
    
    newDict = {}
    for i in range(n):
        if newDict.get(marks[i]) == None:
            newDict[marks[i]] = [ids[i]]
        else:
            newDict[marks[i]].append(ids[i])
            
    unique_m  = []
    for i in marks:
        if i not in unique_m:
            unique_m.append(i)
        
            
    reverse_ins(unique_m)

    with open("output1.txt", 'w') as file_out:       
        for i in unique_m:
            
            temp = newDict[i]
            reverse_ins(temp)
            for x in temp:
                # print(x)
                file_out.write(f"{x} ")
    
    
    
    