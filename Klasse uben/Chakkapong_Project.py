from cgi import print_arguments
from multiprocessing.dummy import Process
from re import I
import pandas as pd

cell = pd.read_excel (r'C:\Users\ADMIN\Desktop\Year3\test.xlsx',sheet_name= "Sheet1")


PR = cell["Process"]
BT = cell["Burst Time"]
AT = cell["Arrival Time"]
PT = cell["Priority"]

D_array = ["Process" , "Burst Time" , "Arrival Time","Priority"],[]

D_array = list()
D_sort_array = list()
D_sort_array.append(["Process" , "Burst Time" , "Arrival Time","Priority","Waiting Time","Status"])
D_array.append([])
for i in range(0,20) :

    D_array.append([PR[i] , BT[i] , AT[i] , PT[i]])


for i in range(0,20) :
    
    element = len(D_array) - 1
    min = D_array[1]

    while element != 0 : 
        if D_array[element][1] >= min[1] :
            max = D_array[element]
            min = max 
            mem = element
        else :
          
            max = min
        element = element - 1 
    D_sort_array.append(D_array[mem])
    D_array.pop(mem)

for i in range (1 , len(D_sort_array)) :
    Adding = D_sort_array[i] 
    Adding.append("0") 
    Adding.append("Inqueue") 

#print(pd.DataFrame(D_sort_array))
Total_time = 0
Waiting = 0
Burst = 0
instant = [],[]
instant = list()
#while sum(x.count('Inqueue') for x in D_sort_array) != 0 :
for i in range (1 , 21) : 
    for i in range (1 , len(D_sort_array)) :  
        if D_sort_array[i][5] == "Inqueue" :
            if D_sort_array[i][2] <= 0 :
                instant = instant + [D_sort_array[i]]
    
    # Maximum Burst value sort
    
    min = instant[0][1]
    q = 0
    for j in range (0,len(instant)):
        
        if int(instant[j][1]) > min :
            min = instant[j][1]
            q = j 
        else :
            min = min
    
    
    uplim = instant[q][1]
    
    
   
    j = 0
    i = 0
    mem = len(instant)
    while j != mem :
        if instant[j-i][1] < uplim :
            instant.pop(j-i)
            #print("checking j =", j , "and pop")
            i = i+1
        else :
            print("\n")
        j = j+1

    


    # Priority sort
    min = instant[0][3]
    q = 0
    for j in range (0,len(instant)):
        
        if int(instant[j][3]) < min :
            min = instant[j][3]
            q = j 
        else :
            min = min
    #print(instant[q])
    Burst = instant[q][1]
    #print(instant[q][0])
    Total_time = Total_time + Burst
    for i in range (1 , len(D_sort_array)) :
        
        if D_sort_array[i][0] == str(instant[q][0]) :
            
            D_sort_array[i][1] = D_sort_array[i][1] - Burst
        D_sort_array[i][2] = D_sort_array[i][2] - Burst


        if D_sort_array[i][1] == 0 :
            D_sort_array[i][5] = "Complete"
        if D_sort_array[i][5] != "Complete" :
            D_sort_array[i][4] = int(D_sort_array[i][4]) + Burst





print("Total run time = ",Total_time)
print(pd.DataFrame(D_sort_array))
#print(pd.DataFrame(instant))


        
                    

        
                        

#print(instant)
#print(priority)
 
  