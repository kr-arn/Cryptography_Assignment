def compute_hash(message):
    hash_value = hash(message) % (10 ** 8)  # hash() is an in built function in python
    return hash_value

#Enter the message sent to two recievers.
message = input("Enter the message to be sent:")
hash_value = compute_hash(message)

print("Original Message:", message)
print("Hash Value:", hash_value)

# Simulate receiver1 computing hash again and ensuring integrity
received_message = input("\nEnter the message recieved by the receiver1:")
received_hash_value = compute_hash(received_message)

print("\nReceived Message:", received_message)
print("Received Hash Value:", received_hash_value)

if received_hash_value == hash_value:
    print("Integrity: The received message is unaltered.\n")
else:
    print("Integrity: The received message has been altered.\n")

# Simulate Receiver2 computing hash again and ensuring integrity
altered_message = input("Enter the message recieved by recievr2:")
altered_hash_value = compute_hash(altered_message)

print("\nAltered Message:", altered_message)
print("Altered Hash Value:", altered_hash_value)

if altered_hash_value == hash_value:
    print("Integrity: The altered message matches the original hash.")
else:
    print("Integrity: The altered message does not match the original hash.")
