from mediatheque.mediatheque import Mediatheque
from mediatheque.documents import Livre, DVD
from mediatheque.erreurs import DocumentIndisponible


def main():
    mediatheque = Mediatheque("Mediatheque de Dakar")

    mediatheque.ajouter_document(
        Livre("L'Aventure ambiguë", 1961, "L001",
              auteur="Cheikh Hamidou Kane", nb_pages=191)
    )
    mediatheque.ajouter_document(
        DVD("Camp de Thiaroye", 1988, "D001",
            realisateur="Sembène Ousmane", duree_min=147)
    )

    awa = mediatheque.inscrire("Awa Diop")

    pret = mediatheque.emprunter(awa.numero, "L001")
    print(pret)
    print(len(awa))

    try:
        mediatheque.emprunter(awa.numero, "L001")
    except DocumentIndisponible as err:
        print("Impossible :", err)

    print("\nDocuments disponibles :")
    for doc in mediatheque.documents_disponibles():
        print(doc)  # même appel, affichage différent : polymorphisme


if __name__ == "__main__":
    main()