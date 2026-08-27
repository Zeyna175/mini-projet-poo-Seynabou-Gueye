from .erreurs import TropDEmprunts

MAX_EMPRUNTS = 3


class Adherent:
    """Un adhérent de la médiathèque, avec ses emprunts en cours."""

    def __init__(self, nom, numero):
        self.nom = nom
        self.numero = numero
        self.emprunts = []

    def ajouter_emprunt(self, document):
        if len(self.emprunts) >= MAX_EMPRUNTS:
            raise TropDEmprunts(
                f"{self.nom} a déjà {MAX_EMPRUNTS} emprunts en cours."
            )
        self.emprunts.append(document)

    def retirer_emprunt(self, document):
        self.emprunts.remove(document)

    def __len__(self):
        return len(self.emprunts)

    def __str__(self):
        return f"Adhérent {self.nom} (n°{self.numero})"