import random
import string

def generate_random_string(length, characters=None):

    if characters is None:
        characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate_multiple_random_strings(num_strings, min_length, max_length, characters=None):

    random_strings = []
    for _ in range(num_strings):
        length = random.randint(min_length, max_length)
        random_strings.append(generate_random_string(length, characters))
    return random_strings

strings = generate_multiple_random_strings(100, 50 ,50)
print("Generated random strings:")
for s in strings:
   print(s)