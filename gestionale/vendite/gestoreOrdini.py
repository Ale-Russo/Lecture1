#Scrivere un software gestionale che abbia le seguenti funzionalità:
#1)supportare l'arrivo e la gestione di ordini
#1bis) quando arriva un nuovo ordine, lo aggiungo ad una coda, assicurandomi che sia eseguito solo dopo gli altri
#2)avere delle funzionalità per avere statistiche sugli ordini
#3)fornire statistiche sulla distribuzione di ordini per categoria di cliente
from collections import deque, Counter, defaultdict

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdini:
    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati=[]
        self._statistiche_prodotti=Counter()
        self._ordini_per_categoria=defaultdict(list)

    def add_ordine(self, ordine:Ordine):
        #Aggiunge un nuovo ordine negli elementi da gestire
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}")
        print(f"Ordini ancora da evadere {len(self._ordini_da_processare)}")

    def processa_prossimo_ordine(self):
        #Questo metodo legge il prossimo ordine in coda e lo gestisce:
        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda")
            return False

        ordine=self._ordini_da_processare.popleft() #Logica FIFO
        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(f"{ordine.riepilogo()}")

        #Aggiornare statistiche sui prodotti venduti --
        #Laptop - 10+1

        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name]+=riga.quantita

        #Raggruppare gli ordini per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        #Archiviamo l'ordine
        self._ordini_processati.append(ordine)
        print("Ordine correttamente processato")

        return True

    def processa_tutti_ordini(self):
        #Processa tutti gli ordini attualmente presenti in coda
        print(f"Processando {len(self._ordini_da_processare)} ordini")
        while self._ordini_da_processare:
            self.processa_prossimo_ordine()

        print("Tutti gli ordini sono stati processati")

    def get_statistiche_prodotti(self,top_n: int=5):
        valori=[]
        for prodotto,quantita in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto,quantita))
        return valori

    def get_distribuzione_categorie(self):
        #Questo metodo restituisce info sul totale fatturato per ogni categoria presente
        valori=[]
        for cat in self._ordini_per_categoria.keys():
            ordini=self._ordini_per_categoria[cat]
            totale_fattturato=sum([o.totale_lordo(0.22) for o in ordini])
            valori.append((cat,totale_fattturato))
        return valori

    def stampa_riepilogo(self):
        print("\n"+"="*60)
        print("Stato attuale del business")
        print(f"Ordini corretamente gestiti: {len(self._ordini_processati)}")
        print(f"Ordini in coda: {len(self._ordini_da_processare)}")

        print("Prodotti più venduti:")
        for prod, quantita in self.get_statistiche_prodotti():
            print(f"{prod}: {quantita}")

        print("Fatturato per categoria:")
        for cat,fatturato in self.get_distribuzione_categorie():
            print(f"{cat}: {fatturato}")

def test_modulo():
    sistema=GestoreOrdini()

    ordini=[
        Ordine([RigaOrdine(ProdottoRecord("Laptop",1200.0),1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
               ClienteRecord("Mario Rossi","mariorossi@polito.it","Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Tablet", 2000.0), 1),
                RigaOrdine(ProdottoRecord("Cuffie", 100.0), 3)],
               ClienteRecord("Fulvio Bianchi","fulviobianchi@polito.it","Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop",1200.0),1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
               ClienteRecord("Giuseppe Averta", "giuseppeaverta@polito.it","Silver")),
        Ordine([RigaOrdine(ProdottoRecord("Tablet", 2000.0), 1),
                RigaOrdine(ProdottoRecord("Cuffie", 100.0), 3)],
               ClienteRecord("Carlo Masone","carlomasone@polito.it","Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop",1200.0),1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
               ClienteRecord("Francesca Pistilli","francescapistillo@polito.it","Silver")),
    ]

    for o in ordini:
        sistema.add_ordine(o)

    sistema.processa_tutti_ordini()

    sistema.stampa_riepilogo()

if __name__ == "__main__":
    test_modulo()