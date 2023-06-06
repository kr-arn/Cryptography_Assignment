def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y

def find_inverse(a, m):
    gcd, x, _ = extended_euclidean_algorithm(a, m)

    if gcd != 1:
        raise ValueError("Inverse does not exist.")

    inverse = x % m
    return inverse


a = int(input("Enter the number whose inverse is to be found:"))
m = int(input("Enter the number whose modulus is to be taken:"))

inverse = find_inverse(a, m)

print("Modular inverse of ",a,"mod",m,":" ,inverse)
