from irasas import Irasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        pajamos = Irasas("Pajamos", suma)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma):
        islaidos = Irasas("Išlaidos", suma)
        self.zurnalas.append(islaidos)

    def gauti_balansą(self):
        suma = 0
        for irasas in self.zurnalas:
            if irasas.tipas == "Pajamos":
                suma += irasas.suma
            if irasas.tipas == "Išlaidos":
                suma -= irasas.suma
        print(suma)

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(f"{irasas.tipas}: {irasas.suma}")
