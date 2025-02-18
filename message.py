class Message :
    def __init__(self, mittente, destinatario) :
        self._mittente = mittente #imposta il valore di mittente
        self._destinatario = destinatario
        self._corpoMessaggio = [] #inizializzazione
    
    def mittente(self) : #è un buon metodo per l'incapsulamento, dichiara e implementa funzione che restituisce una copia del contenuto di una stringa
        return self._mittente
    def destinatario(self):
        return self._destinatario
    
    def append(self, riga) :
        self._corpoMessaggio.append(riga)

    def toString(self) :
        return "Mittente: " + self._mittente + "\nDestinatario: " + self._destinatario + "\nMessaggio: \n" +"\n" .join(self._corpoMessaggio)
    

m1 = Message ("nome_mittente", "nome_destinatario")

m1.append("Ciao")
m1.append("come stai?")
m1.append("A presto")

print(m1.toString())
