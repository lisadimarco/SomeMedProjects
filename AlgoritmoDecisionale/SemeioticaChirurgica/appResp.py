def valutazione_versamento_pleurico(rumori_anomali, dolore_toracico, tosse_secca, dispnea, esame_obiettivo):
    """
    Funzione per identificare segni e sintomi compatibili con un versamento pleurico.
    
    Args:
        rumori_anomali (list): Elenco dei rumori auscultati (es. ["rantoli", "sfregamenti pleurici"]).
        dolore_toracico (dict): Informazioni sul dolore toracico (es. {"pleurico": True, "antalgica": True}).
        tosse_secca (bool): Presenza di tosse secca.
        dispnea (int): Intensità della dispnea (valore da 0 a 10).
        esame_obiettivo (dict): Risultati dell'esame obiettivo (es. {"ispezione": True, "palpazione": "ridotto", ...}).

    Returns:
        dict: Esito della valutazione con indicazioni su diagnosi e prossimi passi.
    """

  def raccogli_input():
    # Rumori anomali
    rumori_anomali = input("Inserisci i rumori anomali riscontrati, separati da virgola (es: rantoli,sfregamenti pleurici): ")
    rumori_anomali = [rumore.strip() for rumore in rumori_anomali.split(",")] if rumori_anomali else []

    # Dolore toracico
    pleurico = input("Il dolore è pleurico? (sì/no): ").strip().lower() == "sì"
    antalgica = input("Il paziente adotta una posizione antalgica? (sì/no): ").strip().lower() == "sì"
    dolore_toracico = {"pleurico": pleurico, "antalgica": antalgica}

    # Tosse secca
    tosse_secca = input("La tosse è secca? (sì/no): ").strip().lower() == "sì"

    # Dispnea
    dispnea = int(input("Inserisci il livello di dispnea (da 0 a 10): ").strip())

    # Esame obiettivo
    ispezione = input("Riduzione dei movimenti respiratori del lato affetto? (sì/no): ").strip().lower() == "sì"
    palpazione = input("Fremito vocale (normale/ridotto): ").strip().lower()
    percussione = input("Percussione (normale/ottuso): ").strip().lower()
    auscultazione = input("Auscultazione (normale/assente/soffio pleurico): ").strip().lower()
    esame_obiettivo = {
        "ispezione": ispezione,
        "palpazione": palpazione,
        "percussione": percussione,
        "auscultazione": auscultazione
    }

    return rumori_anomali, dolore_toracico, tosse_secca, dispnea, esame_obiettivo

# Raccolta dei dati
rumori_anomali, dolore_toracico, tosse_secca, dispnea, esame_obiettivo = raccogli_input()

# Esecuzione dell'algoritmo decisionale
risultato = valutazione_versamento_pleurico(
    rumori_anomali=rumori_anomali,
    dolore_toracico=dolore_toracico,
    tosse_secca=tosse_secca,
    dispnea=dispnea,
    esame_obiettivo=esame_obiettivo
)

# Output del risultato
print(\"\\nRisultato della valutazione:\")\nprint(risultato)

  
    risultato = {
        "versamento_probabile": False,
        "diagnosi": [],
        "raccomandazioni": []
    }

    # Analisi dei rumori anomali
    if "rantoli" in rumori_anomali:
        risultato["diagnosi"].append("Possibile presenza di liquido o secrezioni bronchiali.")
    if "sfregamenti pleurici" in rumori_anomali:
        risultato["diagnosi"].append("Segno di pleurite.")
    if "soffi bronchiali" in rumori_anomali:
        risultato["diagnosi"].append("Possibile broncopolmonite.")

    # Analisi del dolore toracico
    if dolore_toracico.get("pleurico"):
        risultato["diagnosi"].append("Dolore pleurico indicativo di irritazione del cavo pleurico.")
        if dolore_toracico.get("antalgica"):
            risultato["raccomandazioni"].append("Il paziente trova sollievo in posizione antalgica (decubito sul lato affetto).")

    # Analisi della tosse
    if tosse_secca:
        risultato["diagnosi"].append("Tosse secca, spesso non produttiva.")

    # Analisi della dispnea
    if dispnea > 0:
        risultato["diagnosi"].append(f"Dispnea proporzionale al grado di compressione polmonare: livello {dispnea}/10.")

    # Esame obiettivo
    if esame_obiettivo.get("ispezione"):
        risultato["diagnosi"].append("Riduzione dei movimenti respiratori del lato affetto.")
    if esame_obiettivo.get("palpazione") == "ridotto":
        risultato["diagnosi"].append("Fremito vocale ridotto a causa della presenza di liquido.")
    if esame_obiettivo.get("percussione") == "ottuso":
        risultato["diagnosi"].append("Ottusità alla percussione, segno di liquido nella parte declive del torace.")
    if esame_obiettivo.get("auscultazione") == "assente":
        risultato["diagnosi"].append("Assenza di murmure vescicolare dovuta al liquido pleurico.")
    elif esame_obiettivo.get("auscultazione") == "soffio pleurico":
        risultato["diagnosi"].append("Soffio pleurico al confine superiore del versamento, indicativo di infiammazione.")

    # Determinazione del versamento probabile
    if any(keyword in risultato["diagnosi"] for keyword in ["liquido", "pleurite", "ottusità", "murmure"]):
        risultato["versamento_probabile"] = True
        risultato["raccomandazioni"].append("Confermare la diagnosi con ecografia toracica o radiografia del torace.")
        risultato["raccomandazioni"].append("Considerare il drenaggio pleurico se clinicamente indicato.")

    return risultato

# Esempio di utilizzo
risultato = valutazione_versamento_pleurico(
    rumori_anomali=["rantoli", "sfregamenti pleurici"],
    dolore_toracico={"pleurico": True, "antalgica": True},
    tosse_secca=True,
    dispnea=6,
    esame_obiettivo={
        "ispezione": True,
        "palpazione": "ridotto",
        "percussione": "ottuso",
        "auscultazione": "assente"
    }
)

print(risultato)
