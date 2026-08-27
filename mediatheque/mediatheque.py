from .documents import Document
from .adherent import Adherent
from .erreurs import DocumentIndisponible, DocumentInconnu


class Mediatheque:
    """Gère les documents, les adhérents, et les emprunts/retours."""

    def __init__(self, nom):
        self.nom = nom
        self.documents = []
        self.adherents = []
        self._prochain_numero = 1

    def ajouter_document(self, document):
        self.documents.append(document)

    def inscrire(self, nom):
        numero = str(self._prochain_numero)
        self._prochain_numero += 1
        adherent = Adherent(nom, numero)
        self.adherents.append(adherent)
        return adherent

    def _trouver_document(self, code):
        for doc in self.documents:
            if doc.code == code:
                return doc
        raise DocumentInconnu(f"Aucun document avec le code {code}.")

    def _trouver_adherent(self, numero):
        for adherent in self.adherents:
            if adherent.numero == numero:
                return adherent
        raise DocumentInconnu(f"Aucun adhérent avec le numéro {numero}.")

    def emprunter(self, numero, code):
        adherent = self._trouver_adherent(numero)
        document = self._trouver_document(code)

        if not document.disponible:
            raise DocumentIndisponible(
                f'Le document "{document.titre}" est déjà emprunté.'
            )

        adherent.ajouter_emprunt(document)
        document.disponible = False
        return document

    def rendre(self, numero, code):
        adherent = self._trouver_adherent(numero)
        document = self._trouver_document(code)

        adherent.retirer_emprunt(document)
        document.disponible = True
        return document

    def rechercher(self, mot):
        mot = mot.lower()
        return [doc for doc in self.documents if mot in doc.titre.lower()]

    def documents_disponibles(self):
        return [doc for doc in self.documents if doc.disponible]

    def emprunts_de(self, numero):
        adherent = self._trouver_adherent(numero)
        return list(adherent.emprunts)