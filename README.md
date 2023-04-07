Polymorphic Encryption Program

This is a polymorphic encryption program written in Python. The program can read its own code, search for eligible files in the current directory, encrypt the files using a randomly generated key, and insert the encrypted code into the target file.

Installation:

To use this program, you will need Python 3 installed on your machine. You can download Python 3 here.

Once you have Python 3 installed, you can clone this repository using the following command:

bash

git clone https://github.com/<your-username>/polymorphic-encryption.git

Usage

To use the encryption program, navigate to the cloned repository in your terminal and run the following command:

python3 encryption.py

The program will then read its own code and search for eligible files in the current directory. If an eligible file is found, the program will generate a crypt key, encrypt the file using a randomly chosen encryption method, create a string of the encrypted code, generate a random filename, and create a decryption routine. The program will then replace some of its own variables with randomly generated variables, insert the encrypted code into the target file, and delete itself from the directory.
Contributing

If you would like to contribute to this project, please follow these steps:

    Fork this repository
    Create a new branch (git checkout -b my-new-feature)
    Make your changes
    Commit your changes (git commit -am 'Add some feature')
    Push to the branch (git push origin my-new-feature)
    Create a new pull request

License

This program is licensed under the MIT license. See the LICENSE file for more information.
Credits

This program was created by TUKRU
