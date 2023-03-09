class Pojistenec:

    """
    Třída reprezentuje pojištěnce vedené v evidenci pojišťovny.
    """

    def __init__(self, jmeno, prijmeni, telefonni_cislo, vek):
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._telefonni_cislo = telefonni_cislo
        self._vek = vek

    """
    Metoda vrací textovou reprezentaci instance třídy Pojištěnec
    """
    def __str__(self):
        return "{:<15} {:<15} {:<7} {:<10}".format(self._jmeno, self._prijmeni, self._vek, self._telefonni_cislo)
