import json

stock = {
    "riz": {"prix": 3200, "quantite": 50},
    "huile": {"prix": 9500, "quantite": 12},
    "sucre": {"prix": 4000, "quantite": 30},
    "savon": {"prix": 1500, "quantite": 0}
}

# 1. Afficher chaque produit
for produit, infos in stock.items():
    print(f"{produit} - Prix: {infos['prix']} Ar - Quantité: {infos['quantite']}")

# 2. Valeur totale du stock
valeur_totale = sum(infos["prix"] * infos["quantite"] for infos in stock.values())
print(f"Valeur totale : {valeur_totale:,} Ar")

# 3. Produits en rupture de stock
rupture = [p for p, infos in stock.items() if infos["quantite"] == 0]
print("En rupture :", rupture)

# 4. Fonction vendre
def vendre(st, produit, qte):
    info = st.get(produit)
    if not info:
        return False, "Produit inconnu"
    if info["quantite"] < qte:
        return False, "Quantité insuffisante"
    info["quantite"] -= qte
    return True, "Vente réussie"

print(vendre(stock, "riz", 5))

# 5. Ajouter un produit
def ajouter_produit(st, nom, prix, qte):
    if nom in st:
        return "Erreur : le produit existe déjà"
    st[nom] = {"prix": prix, "quantite": qte}
    return "Produit ajouté"

# 6. Dictionnaire prix_hausse (+10%)
prix_hausse = {p: {"prix": round(infos["prix"] * 1.1), "quantite": infos["quantite"]} for p, infos in stock.items()}
print("Prix hausses :", prix_hausse)

# 7. Compter des ventes avec Counter
from collections import Counter
ventes = ["riz", "sucre", "riz", "huile", "riz"]
print(Counter(ventes))

# 8. Sauvegarde JSON
with open("stock.json", "w", encoding="utf-8") as f:
    json.dump(stock, f, ensure_ascii=False, indent=2)