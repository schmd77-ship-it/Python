import math

villes = [
    ("Antananarivo", -18.88, 47.51),
    ("Toamasina", -18.15, 49.40),
    ("Mahajanga", -15.72, 46.32),
    ("Fianarantsoa", -21.45, 47.09)
]

# 1. Parcourir et afficher
for nom, lat, lon in villes:
    print(f"{nom}: {lat}, {lon}")

# 2. Ville la plus au nord (latitude max)
plus_au_nord = max(villes, key=lambda v: v[1])
print("Ville la plus au nord :", plus_au_nord[0])

# 3. Fonction bornes
def bornes(liste_villes):
    lats = [v[1] for v in liste_villes]
    lons = [v[2] for v in liste_villes]
    return min(lats), max(lats), min(lons), max(lons)

lat_min, lat_max, lon_min, lon_max = bornes(villes)
print(f"Bornes -> Lat: [{lat_min}, {lat_max}], Lon: [{lon_min}, {lon_max}]")

# 4. Fonction distance euclidienne
def distance(p1, p2):
    return math.dist(p1, p2)

# 5. Dictionnaire des paires de distances
paires_distances = {}
for i in range(len(villes)):
    for j in range(i + 1, len(villes)):
        v1, v2 = villes[i], villes[j]
        paires_distances[(v1[0], v2[0])] = distance((v1[1], v1[2]), (v2[1], v2[2]))
print(f"Nombre de paires : {len(paires_distances)}")

# 6. Test d'immutabilité
try:
    villes[0][1] = -19.0
except TypeError as e:
    print("Erreur interceptée avec succès :", e)
# Correction : on recrée un nouveau tuple
villes[0] = ("Antananarivo", -19.0, 47.51)