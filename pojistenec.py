class Pojistenec:

    """
    Třída reprezentuje pojištěnce vedené v evidenci pojišťovny.
    """

    def __init__(self, jmeno, prijmeni, telefonni_cislo, vek, email, ulice, mesto, psc):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefonni_cislo = telefonni_cislo
        self.vek = vek
        self.email = email
        self.ulice = ulice
        self.mesto = mesto
        self.psc = psc

    def __str__(self):
        return ("{:<5} {:<12} {:<12} {:<5} {:<30} {:<15} {:<20} {:<15} {:<5}".format(self.jmeno, self.prijmeni, self.vek,
                            self.email, self.telefonni_cislo, self.ulice, self.mesto, self.psc))