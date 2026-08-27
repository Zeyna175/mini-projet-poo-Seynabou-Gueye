class MediathequeError(Exception):
    """Classe de base pour toutes les erreurs de la médiathèque."""
    pass


class DocumentIndisponible(MediathequeError):
    """Levée quand on tente d'emprunter un document déjà prêté."""
    pass


class TropDEmprunts(MediathequeError):
    """Levée quand un adhérent essaie d'emprunter plus de 3 documents."""
    pass


class DocumentInconnu(MediathequeError):
    """Levée quand on référence un document (ou un adhérent) qui n'existe pas."""
    pass