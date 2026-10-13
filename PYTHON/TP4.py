import time
from functools import wraps

# 1 & 5. Décorateur chronometrer avec paramètre (unité)
def chronometrer(unite="s"):
    def decorateur(fonction):
        @wraps(fonction)
        def enveloppe(*args, **kwargs):
            debut = time.perf_counter()
            resultat = fonction(*args, **kwargs)
            fin = time.perf_counter()
            duree = fin - debut
            if unite == "ms":
                print(f"{fonction.__name__} a pris {duree * 1000:.2f} ms")
            else:
                print(f"{fonction.__name__} a pris {duree:.2f} s")
            return resultat
        return enveloppe
    return decorateur

# 2. Décorateur majuscules
def majuscules(fonction):
    @wraps(fonction)
    def enveloppe(*args, **kwargs):
        resultat = fonction(*args, **kwargs)
        return resultat.upper() if isinstance(resultat, str) else resultat
    return enveloppe

# 3. Décorateur compter_appels
def compter_appels(fonction):
    @wraps(fonction)
    def enveloppe(*args, **kwargs):
        enveloppe.appels += 1
        return fonction(*args, **kwargs)
    enveloppe.appels = 0
    return enveloppe

# 4. Décorateur verifier_positifs
def verifier_positifs(fonction):
    @wraps(fonction)
    def enveloppe(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Argument négatif interdit")
        for val in kwargs.values():
            if isinstance(val, (int, float)) and val < 0:
                raise ValueError("Argument négatif interdit")
        return fonction(*args, **kwargs)
    return enveloppe

# Test rapide d'une fonction décorée
@chronometrer(unite="s")
def lente():
    time.sleep(0.5)
    return "Terminé"

lente()