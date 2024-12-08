
# GENERATES ALL OF THE PRIMES 2 THROUGH N

N = 10000

lista = []
primes_list = []


"""
#naive implementation

for i in range(2, N):
    bool_val = True
    for j in range(len(lista)):
        if (i % lista[j] == 0):
            bool_val = False
            break
    if (bool_val):
        primes_list.append(i)
    lista.append(i)
print(primes_list)
"""



#optimized implentation

for i in range(2, N + 1):
    bool_val = True
    flag = False
    num_as_str = str(i)
    len_of_num_as_str = len(num_as_str)
    last_digit_as_int = int(num_as_str[len_of_num_as_str - 1])
    digit_sum = 0
    
    #optimization 1     / 2
    if (last_digit_as_int == 0 or last_digit_as_int == 2 or last_digit_as_int == 4 or last_digit_as_int == 6 or last_digit_as_int == 8):
        if (i != 2):
            bool_val = False
            flag = True
        
    #optimization 2    / 5
    if (bool_val == True):
        if (last_digit_as_int == 5 and i != 5):
            bool_val = False
            flag = True
        
        #optimization 3    / 7     
        if (bool_val == True):
            if (len_of_num_as_str >= 2):
                if (((int( num_as_str[:-1] ) - (2 * last_digit_as_int)) % 7 == 0)):  
                    bool_val = False
                    flag = True
                    
            #optimization 4    / 3      we do this last as digit_sum requires another for loop of O(len(n))
            if (bool_val == True):
                for k in range(len_of_num_as_str):
                    digit_sum = digit_sum + int(num_as_str[k])
                if (digit_sum % 3 == 0 and i != 3):
                    bool_val = False
                    flag = True   
    
    len_of_lista = len(lista)
    if (bool_val == True):
        for j in range(len_of_lista):
            if (i % lista[j] == 0):
                bool_val = False
                break
            
    if (bool_val):
        primes_list.append(i)
        
    #optimization 5
    if (flag == False and bool_val == True and i != 2 and i != 3 and i != 5 and i != 7):
        lista.append(i)
        

print("List of Prime Numbers Between 2 and", N, "Inclusive:", primes_list)

# optimization 1 and 2 only optimize slighty if at all. if you just need to look at the end of a number its O(1), compared to the modulo operator, it may sometimes be faster

# optimizaiton 3 and 4 are not even more optimized than doing i % 7 or i % 3, they are just easier for humans to deal with (checking smaller numbers)

# optimization will mainly come from mnimizing lista     
        
        
        
        
        
        
        
        
        
   