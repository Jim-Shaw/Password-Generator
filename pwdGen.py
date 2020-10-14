import random
import string

# Generate random passwords
# Random string with the combination of lower and upper case ltters and digits

file = open('pwd.txt', 'w')
for r in range(1, 100):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters_and_digits) for i in range(8))
    # Write password to file above
    file.write(result_str + '\n')
    file.close