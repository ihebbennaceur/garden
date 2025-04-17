from datetime import datetime

def get_lunar_phase(date: datetime = None):
    """Retourne la phase lunaire pour une date donnée"""
    if date is None:
        date = datetime.now()
    
    # Implémentation simplifiée - à remplacer par un vrai calcul lunaire
    day = date.day
    if day < 7:
        return "Nouvelle lune"
    elif day < 14:
        return "Premier quartier"
    elif day < 21:
        return "Pleine lune"
    else:
        return "Dernier quartier"