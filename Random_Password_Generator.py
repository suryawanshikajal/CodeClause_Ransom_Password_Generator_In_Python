# choosing secrets module instead of radom module to avoid pseudo randomness
import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

pwd_length = 12

# Genereating a password with constraints

# new password will be generated till we get a password that matches both constraints ie.
# 1. password must have a special character
# 2. password must have at least 2 digits

while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

    # checking constraints
  if (any(char in special_chars for char in pwd) and 
      sum(char in digits for char in pwd)>=2):
          break
print(pwd)
