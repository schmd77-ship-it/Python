notes = [12, 8, 15, 17, 9, 11, 14, 6, 13, 16]

# 1. Nombre de notes, moyenne, min et max
nb_notes = len(notes)
moyenne = sum(notes) / nb_notes
print(f"{nb_notes} notes, moyenne {moyenne:.2f}, min {min(notes)}, max {max(notes)}")

# 2. Notes >= 10 par compréhension et nombre d'ajournés
admis = [n for n in notes if n >= 10]
ajournes = len([n for n in notes if n < 10])
print("Admis :", admis)
print(f"{ajournes} ajournés")

# 3. Tri croissant (sans modifier l'originale) et 3 meilleures notes
notes_triees = sorted(notes)
trois_meilleures = sorted(notes, reverse=True)[:3]
print("Triées :", notes_triees)
print("3 meilleures :", trois_meilleures)

# 4. Bonus de 2 points pour les notes < 10 (sans dépasser 10)
notes_bonus = [min(10, n + 2) if n < 10 else n for n in notes]
print("Après bonus :", notes_bonus)

# 5. Fonction histogramme
def histogramme(liste_notes):
    tranches = {"0-4": 0, "5-9": 0, "10-14": 0, "15-20": 0}
    for n in liste_notes:
        if n <= 4: tranches["0-4"] += 1
        elif n <= 9: tranches["5-9"] += 1
        elif n <= 14: tranches["10-14"] += 1
        else: tranches["15-20"] += 1
    for tranche, count in tranches.items():
        print(f"{tranche:6} | " + "*" * count)

histogramme(notes)

def rang(liste_notes, note_cherche):
    classement_dec = sorted(liste_notes, reverse=True)
    return classement_dec.index(note_cherche) + 1

print("Rang de 14 :", rang(notes, 14))

supplement = [15, 6, 18]
fusion = list(dict.fromkeys(notes + supplement))
print("Fusion sans doublons :", fusion)