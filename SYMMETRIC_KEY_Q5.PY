def calculate_shared_key(g, p, x, y):
    
    A = pow(g, x, p) 
    B = pow(g, y, p)  

   
    shared_key_A = pow(B, x, p)  
    shared_key_B = pow(A, y, p)  

    
    assert shared_key_A == shared_key_B

    return shared_key_A

g = int(input("Enter the common base:"))  
p = int(input("Enter the common modulus:"))  

x = int(input("Enter the Private key for party A:"))  
y = int(input("Enter the Private key for party B:"))  
shared_key = calculate_shared_key(g, p, x, y)
print("Shared Key:", shared_key)
