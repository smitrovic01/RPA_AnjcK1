import random

class Anjc:
    def __init__(self):
        self.SPIL = {'2': 2, '3':3, '4': 4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':10, 'Decko':10, 'Dama':10, 'Kralj': 10, 'Kec':1}
        
    def display_title_bar(self):
        print("\t********************************************")
        print("\t***  Anjc - Razvoj poslovnih aplikacija  ***")
        print("\t********************************************")
    
    def get_user_choice(self):
        print("\n[1] Igraj Anjc.")
        print("[x] Izlaz")
        return input("Odaberite što želite napraviti?")
    
    def player_input(self):
        # vraca True za stop i False za vuci
        # while petlja za Meni u kojem su vuci ili stop
            while True:
                # lower metoda se koristi kako bi unos spustio na mala slova radi lakše usporedbe i provjere
                vuci = input("Želite li odabrati (V)uci ili (S)top").lower() 
                if vuci in ("vuci", "v"):
                    return False # to mi treba u metodi koja obraduje logiku povlacenja karata iz liste ili ispisa rezultata
                elif vuci in ("stop", "s"):
                    return True # to mi treba u metodi koja obraduje logiku povlacenja karata iz liste ili ispisa rezultata
                else:
                    print("HVATANJE IZUZETKA!!")
    
    def start_game(self):
        deck = (['2', '3', '4', '5', '6', '7', '8', '9', '0', 'Decko', 'Dama', 'Kralj', 'Kec'])*4 # puta 4 je zato što ima četiri boje u decku/kutiji karata
        random.shuffle(deck)
        # Igrač/Računalo dobiva po jednu kartu
        player = [deck.pop() for _ in range(1)] # random.int(1 10)
        computer = [deck.pop() for _ in range(1)]
        
        while True:
            print("Igračeva (Vaša) ruka: {}".format(player))
            stop = self.player_input()
            if not stop:
                player.append(deck.pop())
                computer.append(deck.pop())
            else:
                player_total = sum(self.SPIL[card] for card in player)
                computer_total = sum(self.SPIL[card] for card in computer)
                if player_total > computer_total:
                    print("Igrač pobjeđuje. Rezultat Igrač {} vs. Računalo {}".format(player_total, computer_total))
                else:
                    print("Računalo pobjeđuje. Rezultat: Računalo {} vs. Igrač {}".format(computer_total, player_total))
            
            total = sum(self.SPIL[card] for card in player)
            if total > 21:
                print("Premašili ste rezultat, vaša ruka je {}".format(total))
                break
            elif total == 21:
                print("Pobjeđujete! Imate Anjc! Vaša ruka je {}".format(total))
                break
            elif stop:
                print("Stali ste s igrom. Završni rezultat je: Igrač {} vs Računalo {}".format(total, sum(self.SPIL[card] for card in computer)))
                break
    
    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':# u ovoj situaciji choice ima vrijednost '1' što je string (tekst), a vi ga uspoređujete s brojem 1
                self.start_game()
            elif choice == 'x':
                print("\nHvala na igranju Anjca. Pozdrav!")
            else:
                print("Hvatanje IZUZETKA")
        
    
if __name__ == '__main__':
    game = Anjc()
    game.play()
            
                    


            
            
            