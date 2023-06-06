def calculate_shared_key(g, p, x, y):
    # Calculate public keys for both parties
    A = pow(g, x, p)  # A = g^x mod p
    B = pow(g, y, p)  # B = g^y mod p

    # Calculate the shared secret key for both parties
    shared_key_A = pow(B, x, p)  # shared_key_A = B^x mod p
    shared_key_B = pow(A, y, p)  # shared_key_B = A^y mod p

    # Ensure both parties have the same shared secret key
    assert shared_key_A == shared_key_B

    return shared_key_A

# Example usage
g = int(input("Enter the common base:"))  # Common base
p = int(input("Enter the coommon modulus:"))  # Common modulus

x = int(input("Enter the Private key for party A:"))  # Private key for Party A
y = int(input("Enter the Private key for party B:"))  # Private key for Party B

shared_key = calculate_shared_key(g, p, x, y)
print("Shared Key:", shared_key)
