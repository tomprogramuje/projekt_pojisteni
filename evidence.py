import sqlite3
conn = sqlite3.connect('databaze_pojistencu.db')
cursor = conn.cursor()


class Evidence:

    """
    Třída reprezentuje nástroj pro správu pojišťenců.
    """

    def nacti_volbu(self, text_zadani, text_chyba):
        spatne = True
        while spatne:
            try:
                cislo = int(input(text_zadani))
                assert 0 < cislo < 7
                spatne = False
            except ValueError:
                print(text_chyba)
            except AssertionError:
                print(text_chyba)
        else:
            return cislo

    def volba(self, cislo_akce):
        if cislo_akce == 1:
            self.pridej_pojistence()
        elif cislo_akce == 2:
            self.vypis_vsechny_pojistence()
        elif cislo_akce == 3:
            self.vyhledej_pojistence()
        elif cislo_akce == 4:
            self.uprav_pojistence()
        elif cislo_akce == 5:
            self.smaz_pojistence()
        else:
            conn.close()
            exit()

    def hlavni_menu(self):
        print("----------------------------")
        print("Evidence pojištěných")
        print("----------------------------")
        print()
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Uprav pojištěného")
        print("5 - Smaž pojištěného")
        print("6 - Konec")
        cislo_akce = self.nacti_volbu("", "Neplatné zadání!\n")
        self.volba(cislo_akce)

    def pridej_pojistence(self):
        jmeno = input("Zadejte jméno pojištěného:")
        prijmeni = input("Zadejte příjmení pojištěného:")
        vek = input("Zadejte věk:")
        telefonni_cislo = input("Zadejte telefonní číslo:")
        email = input("Zadejte email:")
        ulice = input("Zadejte adresu bydliště - ulice a č.p.:")
        mesto = input("Město:")
        psc = input("PSČ:")

        cursor.execute("INSERT INTO pojistenci (UZIVATEL_ID,JMENO,PRIJMENI,VEK,EMAIL,TELEFONNI_CISLO,ULICE,MESTO,PSC) \
            VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?)", (jmeno, prijmeni, vek, email, telefonni_cislo, ulice, mesto, psc))
        conn.commit()

        input("Data byla uložena. Pokračujte stiskem libovolné klávesy...")
        self.hlavni_menu()

    def vypis_vsechny_pojistence(self):

        print("{:<5} {:<12} {:<12} {:<5} {:<30} {:<15} {:<20} {:<15} {:<5}".format("ID", "Jméno", "Příjmení", "Věk",
                                                                "Email", "Tel. číslo", "Ulice a č.p.", "Město", "PSČ"))

        vypis = cursor.execute("SELECT * FROM pojistenci")
        for row in vypis:
            print("{:<5} {:<12} {:<12} {:<5} {:<30} {:<15} {:<20} {:<15} {:<5}".format(row[0], row[1], row[2], row[3],
                                                                            row[4], row[5], row[6], row[7], row[8]))

        input("Pokračujte libovolnou klávesou...")
        self.hlavni_menu()

    def vyhledej_pojistence(self):
        jmeno = input("Zadejte jméno pojištěného:")
        prijmeni = input("Zadejte příjmení pojištěného:")

        vyhledej = cursor.execute("SELECT * FROM pojistenci WHERE JMENO=? AND PRIJMENI=?", (jmeno, prijmeni))
        if vyhledej.fetchone() is None:
            print("Pojištěnec nenalezen")
        else:
            print("{:<5} {:<12} {:<12} {:<5} {:<30} {:<15} {:<20} {:<15} {:<5}".format("ID", "Jméno", "Příjmení", "Věk",
                                                                 "Email", "Tel. číslo", "Ulice a č.p.", "Město", "PSČ"))
            vyhledej = cursor.execute("SELECT * FROM pojistenci WHERE JMENO=? AND PRIJMENI=?", (jmeno, prijmeni)) #dost fuj, opakování
            for row in vyhledej:
                print("{:<5} {:<12} {:<12} {:<5} {:<30} {:<15} {:<20} {:<15} {:<5}".format(row[0], row[1], row[2],
                                                                       row[3], row[4], row[5], row[6], row[7], row[8]))

        input("Pokračujte libovolnou klávesou...")
        self.hlavni_menu()

    def uprav_pojistence(self):
        id_pojisteneho = input("Zadejte ID pojištěného:")
        jmeno = input("Zadejte jméno pojištěného:")
        prijmeni = input("Zadejte příjmení pojištěného:")
        vek = input("Zadejte věk:")
        telefonni_cislo = input("Zadejte telefonní číslo:")
        email = input("Zadejte email:")
        ulice = input("Zadejte adresu bydliště - ulice a č.p.:")
        mesto = input("Město:")
        psc = input("PSČ:")

        cursor.execute("UPDATE pojistenci SET JMENO=?,PRIJMENI=?,VEK=?,EMAIL=?,TELEFONNI_CISLO=?,ULICE=?,MESTO=?,PSC=? "
            "WHERE UZIVATEL_ID=?", (jmeno, prijmeni, vek, email, telefonni_cislo, ulice, mesto, psc, id_pojisteneho))
        conn.commit()

        input("Data byla uložena. Pokračujte stiskem libovolné klávesy...")
        self.hlavni_menu()

    def smaz_pojistence(self):
        id_pojisteneho = input("Zadejte ID pojištěného:")

        vymaz = cursor.execute("DELETE FROM pojistenci WHERE UZIVATEL_ID == ?", (id_pojisteneho))
        conn.commit()

        input("Pojištěný byl vymazán. Pokračujte libovolnou klávesou...")
        self.hlavni_menu()