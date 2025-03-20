MESI = ("Gennaio  " + "Febbraio " + "Marzo    " + "Aprile   " + "Maggio   " + "Giugno   " +
         "Luglio   "+ "Agosto   " + "Settembre" + "Ottobre  " + "Novembre " + "Dicembre ")
# print(MESI[18])

numero_mese = int(input("scrivi il numero del mese: "))
indice = (numero_mese-1)*9
print("il mese corrispondente è: " + MESI[indice] + MESI[indice+1] + MESI[indice+2] + MESI[indice+3] + MESI[indice+4] +
       MESI[indice+5] + MESI[indice+6] + MESI[indice+7] + MESI[indice+8])