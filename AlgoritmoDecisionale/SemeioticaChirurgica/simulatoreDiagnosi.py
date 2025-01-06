import re
import json

def leggi_referto(file_path):
  file = open(file_path)
  return file.read()

def analizza_referto(contenuto_referto):
    referto_json = {
        "rumori_anomali": [],
        "dolore_toracico": {
            "pleurico": False,
            "antalgica": False
        },
        "tosse_secca": False,
        "dispnea": 0,
        "esame_obiettivo": {
            "ispezione": False,
            "palpazione": None,
            "percussione": None,
            "auscultazione": None
        }
    }

  # Parsing contenuto referto
  if re.search(r"rantoli", contenuto_referto, re.IGNORECASE)
    referto_json["rumori_anomali"].append("rantoli")
    if re.search(r"sfregamenti pleurici", contenuto_referto, re.IGNORECASE):
        referto_json["rumori_anomali"].append("sfregamenti pleurici")
    if re.search(r"tosse secca", contenuto_referto, re.IGNORECASE):
        referto_json["tosse_secca"] = True

    # Dolore toracico
    if re.search(r"dolore pleurico", contenuto_referto, re.IGNORECASE):
        referto_json["dolore_toracico"]["pleurico"] = True
    if re.search(r"posizione antalgica", contenuto_referto, re.IGNORECASE):
        referto_json["dolore_toracico"]["antalgica"] = True

    # Dispnea
    match_dispnea = re.search(r"dispnea livello (\d+)", contenuto_referto, re.IGNORECASE)
    if match_dispnea:
        referto_json["dispnea"] = int(match_dispnea.group(1))

    # Esame obiettivo
    if re.search(r"riduzione dei movimenti respiratori", contenuto_referto, re.IGNORECASE):
        referto_json["esame_obiettivo"]["ispezione"] = True
    match_palpazione = re.search(r"fremito vocale (normale|ridotto)", contenuto_referto, re.IGNORECASE)
    if match_palpazione:
        referto_json["esame_obiettivo"]["palpazione"] = match_palpazione.group(1)
    match_percussione = re.search(r"percussione (normale|ottuso)", contenuto_referto, re.IGNORECASE)
    if match_percussione:
        referto_json["esame_obiettivo"]["percussione"] = match_percussione.group(1)
    match_auscultazione = re.search(r"auscultazione (normale|assente|soffio pleurico)", contenuto_referto, re.IGNORECASE)
    if match_auscultazione:
        referto_json["esame_obiettivo"]["auscultazione"] = match_auscultazione.group(1)

    return referto_json

def salva_referto_json(referto_json, output_file):
  file = open(output_file, 'w')
  json.dump(referto_json, file, indent=4)

if __name__ == '__main__':
  input_file = 'referto.txt'
  output_file = 'referto_analizzato.json'

  contenuto_referto = leggi_referto(input_file)
  referto_analizzato = analizza_referto(contenuto_referto)

  salva_referto_json(referto_analizzato, output_file)

  print("Referto analizzato e salvato in formato JSON:", output_file)
