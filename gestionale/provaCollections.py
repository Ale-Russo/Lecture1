import copy
from enum import nonmember

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine

p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello =[p1, p2, p3, ProdottoRecord("Tablet", 700.0)]

print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

#Aggiungere ad una lista
carrello.append(ProdottoRecord("Monitor", 150.0))

carrello.sort(key = lambda x: x.prezzo_unitario, reverse=True)

print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")

#Aggiungere
carrello.append(ProdottoRecord("Propdo", 100.0))
carrello.extend([ProdottoRecord("aaa", 100.0), ProdottoRecord("bbb", 100.0)])
carrello.insert(2, ProdottoRecord("ccc", 100.0))

#Rimuovere
carrello.pop() # rimuove l'ultimo elemento
carrello.pop(2) # rimuove l'elemento in posizione 2
carrello.remove(p1) #elimino la prima occorrenza di p1
# carrello.clear() #svuoto la lista

#Sorting
# carrello.sort() #ordina seguendo ordinamento naturale -- questo non funziona se gli oggetti contenuti non definisco un metodo __lt__
# carrello.sort(reverse=True) #ordina al contrario
# carrello.sort(key = function)
# carrello_ordinato = sorted(carrello)

#Copie ed altro
carrello.reverse() # inverte l'ordine
carrello_copia = carrello.copy() # shallow copy
carrello_copia2 = copy.deepcopy(carrello) # deep copy, ovvero copio anche il contenuto

# TUPLE
sede_principale = (45, 8) #lat e long della sede di torino
sede_milano = (45, 9) #lat e long della sede di milano

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

AliquoteIVA = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)
)

for descr, valore in AliquoteIVA:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))


tot, media, max, min = calcola_statistiche_carrello(carrello)

# tot, *altri_campi = calcola_statistiche_carrello(carrello)
print(tot)

#SET
categorie = {"Gold", "Silver", "Bronze", "Gold"}
print(categorie)
print(len(categorie))
categorie2 = {"Platinum", "Elite", "Gold"}
# categorie_all = categorie.union(categorie2)
categorie_all = categorie | categorie2 # unione
print(categorie_all)

categorie_comuni = categorie & categorie2 # solo elementi comuni
print(categorie_comuni)

categorie_esclusive = categorie - categorie2 #solo gli elementi presenti in uno dei due set
print(categorie_esclusive)

categorie_esclusive_symm = categorie ^ categorie2 # differenza simmetrica
print(categorie_esclusive_symm)

prodotti_ordine_A = {ProdottoRecord("Laptop", 1200),
                     ProdottoRecord("Mouse", 20),
                     ProdottoRecord("Tablet", 700)}

prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200),
                     ProdottoRecord("Mouse2", 20),
                     ProdottoRecord("Tablet", 700)}

#Metodi utili per i set
s = set()
s1 = set()

#aggiungere
s.add(ProdottoRecord("aaa", 20.0)) #aggiunge un elemento
s.update([ProdottoRecord("aaa", 20.0), ProdottoRecord("bbb", 20.0)]) #aggiungo più elementi

#togliere
#s.remove(elem) #rimuove un elemento. Raise KeyError se non esiste.
#s.discard(elem) #rimuove un elemento, senza "arrabbiarsi" se questo non esiste.
s.pop() #rimuove e restituisce un elemento.
s.clear()

#operazioni insiemistiche
s.union(s1) # s | s1, ovvero genera un set che unisce i due set di partenza
s.intersection(s1) # s & s1, ovvero solo elementi comuni
s.difference(s1) # s-s1, ovvero elementi di s che non sono contenuti in s1
s.symmetric_difference(s1) #s ^s1, ovvero elementi di s non contenuti in s1 ed elementi di s1 non contenuti in s

s1.issubset(s) #se gli elementi di s1 sono contenuti in s
s1.issuperset(s) # se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) # se gli elementi di s e quelli di s1 sono diversi

#Dictionary
catalogo={
    "LAP001":ProdottoRecord("Laptop", 1200.0),
    "LAP002":ProdottoRecord("LaptopPro", 2300.0),
    "MAU001":ProdottoRecord("Mouse", 20.0),
    "AUR001":ProdottoRecord("Auricolari", 250.0),
}

cod="LAP002"
prod=catalogo[cod]

print(f"Il prodotto con codice {cod} è {prod}")

#print(f"Cerco un altro oggetto: {catalogo["NonEsiste!"]}")

prod1=catalogo.get("NonEsiste!")

if prod1 is None:
    print(f"Prodotto non trovato")

prod2=catalogo.get("NonEsiste!",ProdottoRecord("Sconosciuto", 0.0))
print(prod2)

keys = catalogo.keys()
values=catalogo.values()

for k in keys:
    print(k)

for v in values:
    print(v)

for key,val in catalogo.items():
    print(f"Cod {key} è associato a {val}")

#rimuovere dal dizionario
rimosso=catalogo.pop("LAP002")
print(rimosso)

#dict comprehension
prezzi={codice:prod.prezzo_unitario for codice,prod in catalogo.items()}

#DA RICORDARE PER DICT
#v=d[key] #leggere -- restituisce key error se non esiste
#v=d.get(key,default) #legge senza rischiare KeyError -- se non esiste restituisce default
#d.pop(key) #restituisce un valore e lo cancella dal dizionario
#d.clear() #Svuota il dizionario
#d.keys() #restituisce le chiavi
#d.values() #restituisce i valori
#d.items() #restituisce le coppie
#key in d #condizione che verifica se key è presente nel diz

""" Esercizio live
Per ciuscuno dei seguenti casi decidere quale struttura usare:"""
""""
1) Memorizzare un elenco di ordini che dovranno poi essere processati in ordine di arrivo"""
#Lista
ordini_da_processare=[]
o1=Ordine([],ClienteRecord("Mario Rossi", "mario@polito.it","Gold"))
o2=Ordine([], ClienteRecord("Mario Bianchi", ))

"""    
    
2) Memorizzare i CF dei clienti (univoco)
    set
    
3) Creare un database di prodotti che posso cercare con un codice univoco
    dizionario
    
4) Memorizzare le coordinate gps della nuova sede di Roma
    tupla
    
5) Tenere traccia della categoria di clienti che hanno fatto un ordine in un certo range temporale"""


