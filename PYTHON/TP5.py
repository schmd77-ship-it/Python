import json
from datetime import datetime
from functools import wraps

# Structure de données imposée[cite: 28]
etudiants = {
    "L3-001": {
        "nom": "Rakoto",
        "prenom": "Soa",
        "notes": {"Python": [15, 14], "Réseaux": [12]},
    },
    "L3-002": {
        "nom": "Rabe",
        "prenom": "Andry",
        "notes": {"Python": [9, 13], "Réseaux": [11, 10]},
    }
}

# Liste globale pour l'historique des modifications
historique = []

# ==========================================
# DÉCORATEURS REQUIS
# ==========================================

def journaliser(fonction):
    """Enregistre l'appel dans l'historique[cite: 28]."""
    @wraps(fonction)
    def enveloppe(*args, **kwargs):
        date_heure = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        historique.append((date_heure, fonction.__name__, args, kwargs))
        return fonction(*args, **kwargs)
    return enveloppe

def note_valide(fonction):
    """Vérifie que la note est comprise entre 0 et 20[cite: 28]."""
    @wraps(fonction)
    def enveloppe(matricule, matiere, note):
        if not isinstance(note, (int, float)) or not (0 <= note <= 20):
            print(f"Erreur : La note {note} est invalide (doit être entre 0 et 20)[cite: 28].")
            return
        return fonction(matricule, matiere, note)
    return enveloppe

def etudiant_existe(fonction):
    """Vérifie que le matricule existe avant l'exécution[cite: 28]."""
    @wraps(fonction)
    def enveloppe(matricule, *args, **kwargs):
        if matricule not in etudiants:
            print(f"Erreur : Le matricule '{matricule}' n'existe pas[cite: 28].")
            return
        return fonction(matricule, *args, **kwargs)
    return enveloppe

# ==========================================
# FONCTIONS DU PROJET
# ==========================================

@journaliser
def ajouter_etudiant(matricule, nom, prenom):
    """Crée un étudiant, refuse un matricule existant[cite: 28]."""
    if matricule in etudiants:
        print(f"Erreur : Le matricule {matricule} existe déjà[cite: 28].")
        return
    etudiants[matricule] = {
        "nom": nom,
        "prenom": prenom,
        "notes": {}
    }
    print(f"Étudiant {prenom} {nom} ({matricule}) ajouté avec succès[cite: 28].")

@journaliser
@etudiant_existe
@note_valide
def ajouter_note(matricule, matiere, note):
    """Ajoute une note, crée la matière si besoin via setdefault[cite: 28]."""
    etudiants[matricule]["notes"].setdefault(matiere, []).append(note)
    print(f"Note de {note} ajoutée en {matiere} pour le matricule {matricule}[cite: 28].")

def moyenne_matiere(matricule, matiere):
    """Calcule la moyenne d'un étudiant dans une matière[cite: 28]."""
    notes = etudiants[matricule]["notes"].get(matiere)
    if not notes:
        return 0.0
    return sum(notes) / len(notes)

@etudiant_existe
def moyenne_generale(matricule):
    """Calcule la moyenne générale des matières par compréhension[cite: 28]."""
    matieres = etudiants[matricule]["notes"]
    if not matieres:
        return 0.0
    moyennes = [sum(notes) / len(notes) for notes in matieres.values() if notes]
    if not moyennes:
        return 0.0
    return sum(moyennes) / len(moyennes)

def classement():
    """Renvoie une liste de tuples (nom complet, moyenne) triée par ordre décroissant[cite: 28]."""
    resultats = []
    for mat, info in etudiants.items():
        nom_complet = f"{info['prenom']} {info['nom']}"
        mg = moyenne_generale(mat)
        resultats.append((nom_complet, mg))
    return sorted(resultats, key=lambda x: x[1], reverse=True)

def majors():
    """Associe chaque matière au nom du meilleur étudiant[cite: 28]."""
    toutes_matieres = set()
    for info in etudiants.values():
        toutes_matieres.update(info["notes"].keys())
    
    majors_dict = {}
    for matiere in toutes_matieres:
        meilleur_etudiant = None
        meilleure_moyenne = -1
        for mat, info in etudiants.items():
            if matiere in info["notes"] and info["notes"][matiere]:
                m = moyenne_matiere(mat, matiere)
                if m > meilleure_moyenne:
                    meilleure_moyenne = m
                    meilleur_etudiant = f"{info['prenom']} {info['nom']}"
        if meilleur_etudiant:
            majors_dict[matiere] = meilleur_etudiant
    return majors_dict

@journaliser
def sauvegarder(fichier):
    """Sauvegarde le dictionnaire au format JSON[cite: 28]."""
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(etudiants, f, ensure_ascii=False, indent=2)
    print(f"Données sauvegardées dans {fichier}[cite: 28].")

def charger(fichier):
    """Charge les données depuis un fichier JSON[cite: 28]."""
    global etudiants
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            etudiants = json.load(f)
        print(f"Données chargées depuis {fichier}[cite: 28].")
    except FileNotFoundError:
        print("Fichier introuvable.")

# ==========================================
# MENU INTERACTIF
# ==========================================

def menu():
    """Boucle while affichant le menu numéroté[cite: 28]."""
    while True:
        print("\n--- CARNET DE NOTES (MENU) ---")
        print("1. Ajouter un étudiant")
        print("2. Ajouter une note")
        print("3. Afficher le classement général")
        print("4. Afficher les majors par matière")
        print("5. Afficher l'historique des modifications")
        print("6. Sauvegarder les données")
        print("7. Charger les données")
        print("8. Quitter")
        
        choix = input("Votre choix : ")
        
        if choix == "1":
            mat = input("Matricule : ")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            ajouter_etudiant(mat, nom, prenom)
        elif choix == "2":
            mat = input("Matricule : ")
            matiere = input("Matière : ")
            try:
                note = float(input("Note (0 à 20) : "))
                ajouter_note(mat, matiere, note)
            except ValueError:
                print("Erreur de saisie pour la note.")
        elif choix == "3":
            print("\n--- CLASSEMENT ---")
            for pos, (nom, moy) in enumerate(classement(), 1):
                print(f"{pos}. {nom} — {moy:.2f}")
        elif choix == "4":
            print("\n--- MAJORS ---")
            for matiere, etudiant in majors().items():
                print(f"{matiere} : {etudiant}")
        elif choix == "5":
            print("\n--- HISTORIQUE ---")
            for h in historique:
                print(h)
        elif choix == "6":
            sauvegarder("carnet.json")
        elif choix == "7":
            charger("carnet.json")
        elif choix == "8":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()