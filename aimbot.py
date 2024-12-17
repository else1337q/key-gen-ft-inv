import random
import string

def generate_key():
 characters = string.ascii_letters + string.digits
 return ''.join(random.choice(characters) for _ in range(30))

key = generate_key()
print(key)