# /content/drive/MyDrive/Colab Notebooks/Vergunningen/scripts/variables.py
DATA_FILE = "/content/drive/MyDrive/Colab Notebooks/Vergunningen/data/samenvattende_tabel.csv"
TEMPLATE_FILE = "/content/drive/MyDrive/Colab Notebooks/Vergunningen/template/template.html"
OUTPUT_FILE = "/content/drive/MyDrive/Colab Notebooks/Vergunningen/index.html"
STATIC_DIR = "/content/drive/MyDrive/Colab Notebooks/Vergunningen/static"

GRAPH_VARIABLES = [
    "Nieuwbouw (aantal woongelegenheden)",
    "Verbouwen_or_hergebruik (aantal woongelegenheden)",
    "Sloop (aantal gebouwen)",
    "Aandeel_meergezinswoning"
]

TABLE_VARIABLES = [
    "Nieuwbouw (aantal woongelegenheden)",
    "Verbouwen_or_hergebruik (aantal woongelegenheden)",
    "Sloop (aantal gebouwen)",
    "Aandeel_meergezinswoning"
]

# Placeholder texts for each variable
PLACEHOLDER_TEXTS = {
    "Nieuwbouw (aantal woongelegenheden)": "Hier komt de uitleg over nieuwbouw. Beschrijf de trends en opvallende zaken in de data.",
    "Verbouwen_or_hergebruik (aantal woongelegenheden)": "Hier komt de uitleg over verbouwen of hergebruik. Beschrijf de trends en opvallende zaken in de data.",
    "Sloop (aantal gebouwen)": "Hier komt de uitleg over sloop. Beschrijf de trends en opvallende zaken in de data.",
    "Aandeel_meergezinswoning": "Hier komt de uitleg over het aandeel meergezinswoningen. Beschrijf de trends en opvallende zaken in de data."
}