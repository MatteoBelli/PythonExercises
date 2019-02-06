'''
Definire una funzione es3(lista, testo) che prende:
- una lista di parole (nessuna delle quali e' prefisso dell'altra)
- una stringa di testo. Il testo e' stato ottenuto concatenando alcune delle parole presenti nella lista 'lista'
(una stessa parola puo' comparire piu' volte nella stringa di testo).
- restituisce una coppia (tupla) formata da:
- la lista delle parole che, concatenate producono il testo
- la parola che vi occorre piu' spesso
(se questa parola non e' unica allora viene restituita quella che precede le altre lessicograficamente).
Nella lista di output ogni parola appare una sola volta e le parole
risultano ordinate in base alla loro prima apparizione nella concatenazione che produce il testo
(i.e. quella che compare per prima al primo posto ecc.ecc.)
Infine al termine della funzione la lista 'lista' deve risultare modificata come segue:
in essa saranno state cancellate tutte le parole utilizzate in testo, e tornate come risultato.
Ad esempio: se lista=['gatto','cane','topo']
- con  testo='topogattotopotopogattogatto' la risposta e' la coppia (['topo','gatto'],'gatto')
e lista diviene ['cane']
se lista=['ala','cena','elica','nave','luce','lana','vela']
- con testo='lucenavelanavelanaveelica' la risposta e' (['luce','nave','lana','vela','elica'],'nave')
e ls diviene ['ala','cena']

NOTA: il timeout previsto per questo esercizio è di 5 secondi per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
'''


def es3(lista, testo):
    # inserite qui il vostro codice
    copia_testo = testo
    occorrenze = {}
    for i in lista:
        occorrenze.setdefault(i, 0)

    parole_usate = []
    while len(copia_testo) > 0:
        for i in lista:
            word_len = len(i)
            if(i != copia_testo[:word_len]):
                continue
            if parole_usate.count(i) == 0:
                parole_usate.append(i)
            occorrenze[i] += 1
            copia_testo = copia_testo.replace(i, "", 1)

    occorrenze_massime = sorted(occorrenze.values(), reverse=True)[0]
    lista_parole_più_usate = []
    parole_non_usate = []
    for nome, occorrenze in occorrenze.items():
        if occorrenze == 0:
            parole_non_usate.append(nome)
        if occorrenze == occorrenze_massime:
            lista_parole_più_usate.append(nome)

    parola_più_usata = sorted(lista_parole_più_usate)[0]
    for i in parole_usate:
        lista.remove(i)

    return(parole_usate, parola_più_usata)


lista = ['gatto', 'cane', 'topo']
testo = 'topogattotopotopogattogatto'

tupla = es3(lista, testo)
print(tupla, lista)

lista = ['ala', 'cena', 'elica', 'nave', 'luce', 'lana', 'vela']
testo = "lucenavelanavelanaveelica"

tupla = es3(lista, testo)
print(tupla, lista)
