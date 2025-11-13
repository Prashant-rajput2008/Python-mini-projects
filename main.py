import random
import string

chars = string.ascii_letters + string.digits
length = int(input("Enter password length: "))
password = ''.join(random.choice(chars) for _ in range(length))

print("Generated Password:", password)
