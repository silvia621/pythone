#chiedere il nome del file di input
nome_file = input("Scrivi il nome del file: ")

import os
if os.path.exists(nome_file) :
    # print(f" il file '{nome_file}' esiste")
    #aprire il file di input
    input_file = open(nome_file, "r")
    for line in input_file :
        contrario = line[::-1]
        print(contrario)
    input_file.close()
else :
    print(f"il file '{nome_file}' non esiste")