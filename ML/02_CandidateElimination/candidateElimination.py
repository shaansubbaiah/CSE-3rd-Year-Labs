import numpy as np  
import pandas as pd

data = pd.DataFrame(data=pd.read_csv('enjoysport.csv'))  
concepts = np.array(data.iloc[:,0:-1]) 
print('Concepts:', concepts)  
target = np.array(data.iloc[:,-1])   
print('Target:', target) 
 
def learn(concepts, target):  
    print("Initialization of specific_h and general_h")      
    
    specific_h = concepts[0].copy()      
    print('\t specific_h:', specific_h)

    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]      
    print('\t general_h:', general_h)

    for i, h in enumerate(concepts):  
        if target[i] == "yes":  
            for x in range(len(specific_h)):  
                if h[x]!= specific_h[x]:                     
                    specific_h[x] ='?'                      
                    general_h[x][x] ='?'  
        if target[i] == "no":             
            for x in range(len(specific_h)):  
                if h[x]!= specific_h[x]:                     
                    general_h[x][x] = specific_h[x]                 
                else:                     
                    general_h[x][x] = '?'         
        
        print("\n Steps of Candidate Elimination Algorithm",i+1)
        print('\t specific_h', specific_h)       
        print('\t general_h:', general_h)

    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]     
    for i in indices:    
        general_h.remove(['?', '?', '?', '?', '?', '?'])  
    return specific_h, general_h

s_final, g_final = learn(concepts, target)

print("\n Final specific_h:", s_final, sep="\n") 
print("\n Final general_h:", g_final, sep="\n") 
