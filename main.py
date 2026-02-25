import random


class Domanda:
    def __init__(self, testo: str, livello: int, corretta: str, sbagliata0: str, sbagliata1: str, sbagliata2: str):
        self.testo = testo
        self.livello = livello
        self.corretta = corretta
        self.dom = [corretta, sbagliata0, sbagliata1, sbagliata2]

class Player:
    def __init__(self, nickname: str, punteggio: int):
        self.nickname = nickname
        self.punteggio = punteggio


class Game:

    def __init__(self):
        self.domande = []
        self.utenti = []
        self.liv_max = 0

    # @staticmethod @classmethod
    def leggi_domande(self):
        f = open("domande.txt", "r")
        riga = f.readline()
        while riga != "":
            campi = []
            for i in range(7):
                campi.append(riga.strip())
                riga = f.readline()
            self.domande.append(Domanda(campi[0], int(campi[1]), campi[2], campi[3], campi[4], campi[5]))
            if int(campi[1]) > self.liv_max:
                liv_max = int(campi[1])
        f.close()
        return self.domande

    def leggi_punti(self):
        f = open("punti.txt", "r")
        riga = f.readline()
        while riga != "":
            nickname = riga.split(" ")[0]
            punteggio = int(riga.split(" ")[1])
            self.utenti.append(Player(nickname, punteggio))
            riga = f.readline()
        f.close()

    def dom_liv(self, livello: int, domande):
        dom_liv = []
        for d in domande:
            if d.livello == livello:
                dom_liv.append(d)
        return dom_liv

    @staticmethod
    def stampa_domanda(domanda):
        print(f"Livello: {domanda.livello}) {domanda.testo}")
        random.shuffle(domanda.dom)
        i=1

        for e in domanda.dom:
            print(f"{i}. {e}")
            if e == domanda.corretta:
                cor = i
            i = i + 1

        x = int(input("Inserisci la risposta: "))
        if x==cor:
            return 0
        return cor




punteggio = 0
liv_corrente = 0
continua = True
gioco = Game()
domande = gioco.leggi_domande()
gioco.leggi_punti()

while continua:
    domande_possibili = gioco.dom_liv(liv_corrente, domande)
    domanda = domande_possibili[random.randint(0, len(domande_possibili)-1)]
    corretta = gioco.stampa_domanda(domanda)

    if corretta == 0 & (liv_corrente + 1) <= gioco.liv_max:
        liv_corrente = liv_corrente + 1
        punteggio += 1
        print("Risposta corretta!\n")
    else:
        continua = False
        print(f"Risposta sbagliata! La risposta corretta era: {corretta}\n")
        print(f"Hai totalizzato {punteggio} punti!")
        nickname = input("Inserisci il tuo nickname: ")
        gioco.utenti.append(Player(nickname, punteggio))
        gioco.utenti.sort(key=lambda x: x.punteggio, reverse=True)
        with open("punti.txt", "w", encoding="utf-8") as file:
            res = ""
            for u in gioco.utenti:
                if res != "":
                    res+="\n"
                res+=f"{u.nickname} {u.punteggio}"
            file.write(res)


