reddito = int(input("Qual è il tuo reddito? "))
ALIQUOTA_1=0.23
ALIQUOTA_2=0.35
ALIQUOTA_3=0.43
if reddito <= 28000 :
    tasse = float(reddito*ALIQUOTA_1)
else :
   if reddito <= 50000 :
    tasse = 28000*ALIQUOTA_1 + (reddito-28000) * ALIQUOTA_2
   else :
    tasse =28000*ALIQUOTA_1 + (22000) * ALIQUOTA_2 + (reddito-50000)*ALIQUOTA_3
print ("L'imposta è " + str(tasse))