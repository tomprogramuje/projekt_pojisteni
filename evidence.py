from pojistenec import Pojistenec


class Evidence:

    """"
    Třída reprezentuje nástroj pro správu pojišťenců.
    """

    def __init__(self):
        self._databaze_pojistenych = {}

    """
    Metoda přijímá volbu/vstup uživatele.
    """
    def nacti_volbu(self, text_zadani, text_chyba):
        spatne = True
        while spatne:
            try:
                cislo = int(input(text_zadani))
                assert 0 < cislo < 5
                spatne = False
            except ValueError:
                print(text_chyba)
            except AssertionError:
                print(text_chyba)
        else:
            return cislo

    """
    Metoda zpracovává volbu/vstup uživatele.
    """
    def volba(self, cislo_akce):
        if cislo_akce == 1:
            self.pridej_pojistence()
        elif cislo_akce == 2:
            self.vypis_vsechny_pojistence()
        elif cislo_akce == 3:
            self.vyhledej_pojistence()
        else:
            exit()

    """
    Metoda reprezentuje hlavní menu aplikace a zobrazuje možnosti volby.
    """
    def hlavni_menu(self):
        print("----------------------------")
        print("Evidence pojištěných")
        print("----------------------------")
        print()
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")
        cislo_akce = self.nacti_volbu("", "Neplatné zadání!\n")
        self.volba(cislo_akce)

    """
    Metoda vytváří novou instanci třídy Pojištěnec a ukládá ji do kolekce.
    """
    def pridej_pojistence(self):
        jmeno = input("Zadejte jméno pojištěného:")
        prijmeni = input("Zadejte příjmení pojištěného:")
        telefonni_cislo = input("Zadejte telefonní číslo:")
        vek = input("Zadejte věk:")
        novy_pojistenec = Pojistenec(jmeno, prijmeni, telefonni_cislo, vek)
        self._databaze_pojistenych.update({jmeno+prijmeni: novy_pojistenec})
        input("Data byla uložena. Pokračujte stiskem libovolné klávesy...")
        self.hlavni_menu()

    """
    Metoda vypisuje všechny instance třídy Pojištěnec uložené v kolekci.
    """
    def vypis_vsechny_pojistence(self):
        for i in self._databaze_pojistenych:
            print(self._databaze_pojistenych[i])
        input("Pokračujte libovolnou klávesou...")
        self.hlavni_menu()

    """
    Metoda vyhledá na základě vstupu uživatele instanci třídy Pojištěnec uloženou v kolekci a zobrazí ji.
    """
    def vyhledej_pojistence(self):
        jmeno = input("Zadejte jméno pojištěného:")
        prijmeni = input("Zadejte příjmení pojištěného:")
        if jmeno+prijmeni in self._databaze_pojistenych:
            print(self._databaze_pojistenych[jmeno+prijmeni])
        else:
            print("Pojištěnec nenalezen")
        input("Pokračujte libovolnou klávesou...")
        self.hlavni_menu()
