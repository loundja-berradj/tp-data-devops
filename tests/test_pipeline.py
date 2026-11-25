
import pandas as pd

from pipeline import transformer, agreger_par_ville, agreger_par_categorie


def donnees_test():
    return pd.DataFrame({
        "date": ["2026-01-05", "2026-01-05", "2026-01-06"],
        "produit": ["Clavier", "Clavier", "Souris"],
        "categorie": ["Informatique", "Informatique", "Informatique"],
        "quantite": [2, 2, 5],
        "prix_unitaire": [45.0, 45.0, 15.0],
        "ville": ["Paris", "Paris", " paris "]
    })


def test_supprimer_doublons():
    resultat = transformer(donnees_test())
    assert len(resultat) == 2


def test_nettoyer_ville():
    resultat = transformer(donnees_test())
    assert "Paris" in resultat["ville"].values


def test_calculer_chiffre_affaires_ville():
    resultat = transformer(donnees_test())
    total = agreger_par_ville(resultat)
    assert total["montant"].sum() == 165.0


def test_calculer_chiffre_affaires_categorie():
    resultat = transformer(donnees_test())
    total = agreger_par_categorie(resultat)
    assert total["montant"].sum() == 165.0