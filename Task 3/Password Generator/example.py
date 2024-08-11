#Its Just a example , how  password generate ---

import random
import string
# Function for password generate
def generate_password():
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    number = string.digits
    special_chars = "!@#$%^&*()"

    combine = uppercase
    coombine += lowercase
    combine += number
    combine += special_chars

    length =10

    password = "".join(random.sample(combine,length))

    print(password)

passoword_generate()