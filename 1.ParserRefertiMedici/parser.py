import re

file = open("referto.txt")
contenuto = file.read()

sezioni = ["Diagnosi", "Anamnesi", "Trattamento"]

risultati = {}

for i, sezione in enumerate(sezioni):
  pattern = rf"{sezione}:"
  match = re.search(pattern, contenuto, re.IGNORECASE)

  if match:
    start = match.end()

    end = (
      re.search(rf"{sezioni[i + 1]}", contenuto, re.IGNORECASE).start()
      if i + 1 < len(sezioni) else len(contenuto)
    )

    risultati[sezione] = contenuto[start:end].strip()

for sezione, test in risultati.items():
  print(f"{sezione}:\n{text}\n")
