from abc import ABC, abstractmethod


class Document(ABC):
    """Classe de base abstraite représentant un document de la médiathèque."""

    def __init__(self, titre, annee, code):
        self._titre = titre
        self.annee = annee
        self._code = code
        self.disponible = True

    @property
    def titre(self):
        return self._titre

    @property
    def code(self):
        return self._code

    @abstractmethod
    def duree_pret(self):
        """Nombre de jours de prêt autorisé pour ce type de document."""
        ...

    def __str__(self):
        return f'Document "{self.titre}" ({self.annee})'

    def __eq__(self, other):
        if not isinstance(other, Document):
            return NotImplemented
        return self.code == other.code


class Livre(Document):
    """Un livre, avec un auteur et un nombre de pages. Prêt de 21 jours."""

    def __init__(self, titre, annee, code, auteur, nb_pages):
        super().__init__(titre, annee, code)
        self.auteur = auteur
        self.nb_pages = nb_pages

    def duree_pret(self):
        return 21

    def __str__(self):
        base = super().__str__()
        return f'{base} - Livre de {self.auteur}, {self.nb_pages} pages'


class DVD(Document):
    """Un DVD, avec un réalisateur et une durée. Prêt de 7 jours."""

    def __init__(self, titre, annee, code, realisateur, duree_min):
        super().__init__(titre, annee, code)
        self.realisateur = realisateur
        self.duree_min = duree_min

    def duree_pret(self):
        return 7

    def __str__(self):
        base = super().__str__()
        return f'{base} - DVD réalisé par {self.realisateur}, {self.duree_min} min'