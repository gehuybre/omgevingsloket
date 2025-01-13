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

TITLES = {
    "Nieuwbouw (aantal woongelegenheden)": "Vergunningsaanvragen voor nieuwbouw",
    "Verbouwen_or_hergebruik (aantal woongelegenheden)": "Vergunningsaanvragen voor renovatie en hergebruik",
    "Sloop (aantal gebouwen)": "Vergunningsaanvragen voor sloop",
    "Aandeel_meergezinswoning": "Aandeel meergezinswoningen in vergunningsaanvragen"
}

# Placeholder texts for each variable
PLACEHOLDER_TEXTS = {
    "Nieuwbouw (aantal woongelegenheden)": """
        <p>Het aantal vergunningsaanvragen voor nieuwbouw is een voorlopende indicator voor de bouwconjunctuur. Aanvragen voor bouwvergunningen geven een goede indicatie van de bouwactiviteit die we in de komende één tot twee jaar mogen verwachten. De vergunning vervalt immers wannneer niet gestart wordt met de werken binnen 2 jaar na het verlenen van de definitieve vergunning.</p>
        <h3>Evolutie op Jaarbasis</h3>
        <p>Als we de evolutie van het aantal vergunningen voor nieuwbouw woongelegenheden op jaarbasis bekijken, zien we een opvallende trend: Na een piek in 2019 met een stijging van 28% ten opzichte van 2018, zien we een aanhoudende daling in de daaropvolgende jaren. Vooral in 2023 is er met een daling van 15% ten opzichte van 2022 sprake van een significante afname. In 2024 zet de trend zich verder door met een afname van maar liefst 29% tot een historisch dieptepunt van 35057.  Deze aanhoudende negatieve trend wijst op een sterke afkoeling van de bouwconjunctuur.</p>
        <h3>Seizoensinvloeden en kwartaalcijfers</h3>
        <p>Het is een typisch patroon dat in het laatste kwartaal van elk jaar de meeste vergunningen worden aangevraagd. Dit heeft te maken met het feit dat bouwaanvragen die voor het einde van het jaar worden ingediend, vaak nog onder de regelgeving van dat jaar vallen, hetgeen in veel gevallen gunstiger is dan de nieuwe regels die vaak in het daaropvolgende jaar van kracht worden. Dit verklaart de jaarlijkse piek in het vierde kwartaal. Omgekeerd zien we dat het eerste kwartaal van elk jaar doorgaans een stuk minder aanvragen telt.</p>
        <p>De kwartaalcijfers tonen deze trend duidelijk aan. We zien dat Q4 steevast de meeste vergunningen telt.</p>
        <h3>Algemene trend</h3>
        <p>De algemene trend over de gehele periode is dalend, wat wijst op een afkoeling van de bouwconjunctuur in het segment van de nieuwbouw woongelegenheden. In het laatste jaar van de periode (2024) zitten we op een historisch minimum met de waarden van 35057 vergunningen op jaarbasis. Deze cijfers zijn alarmerend en wijzen op een verdere vertraging van de bouwactiviteit in 2025.</p>
          """,
    "Verbouwen_or_hergebruik (aantal woongelegenheden)": """<p>Het aantal vergunningsaanvragen voor verbouwingen of hergebruik van bestaande panden is een indicator voor de renovatiemarkt. Deze cijfers geven een beeld van de investeringen in het energiezuinig maken en het aanpassen van de bestaande woningvoorraad. Niet alle werken zijn vergunningsplichtig. Zo zijn verbouwingen binnen woning vrijgesteld van vergunning wanneer het niet gaat om stabliteitswerken of wijzigingen van het bouwvolume (bijvoorbeeld opsplitsen van slaapkamers, vervangen van een keuken of badkamer, of plaatsen van isolatie).  </p>
<h3>Evolutie op jaarbasis</h3>
<p>De evolutie van het aantal vergunningen voor verbouwingen of hergebruik op jaarbasis toont een wisselend beeld: We zien een aanzienlijke stijging van 20% in 2019 ten opzichte van 2018, gevolgd door een verdere toename in 2020 en 2021. In 2022 is er een daling van -10%, maar in 2023 zien we weer een stijging van 9%. Echter, in 2024 zien we opnieuw een sterke daling van 22%. Deze schommelingen wijzen op een minder stabiele markt in vergelijking met de nieuwbouw.</p>
<h3>Seizoensinvloeden en kwartaalcijfers</h3>
<p>Net als bij nieuwbouw zien we ook bij verbouwingen en hergebruik een seizoenspatroon, hoewel dit minder uitgesproken is. Over het algemeen worden er in het laatste kwartaal van het jaar meer vergunningen aangevraagd.</p>
<p>De kwartaalcijfers tonen dit patroon zien: In de meeste jaren zien we een piek in het vierde kwartaal. Echter, deze piek is minder uitgesproken dan bij nieuwbouw.</p>
<h3>Algemene trend en schommelingen</h3>
<p>De algemene trend over de gehele periode is licht stijgend, maar met aanzienlijke schommelingen van jaar tot jaar. Dit wijst op een minder voorspelbare markt dan die van de nieuwbouw. De markt voor verbouwingen en hergebruik lijkt gevoeliger te zijn voor economische schommelingen en veranderende regelgeving. Het is aannemelijk dat de extreme daling in 2024 hier ook mee te maken heeft.</p>
<h3>Conclusie</h3>"""
   "Sloop (aantal gebouwen)": "Hier komt de uitleg over sloop. Beschrijf de trends en opvallende zaken in de data.",
    "Aandeel_meergezinswoning": "Hier komt de uitleg over het aandeel meergezinswoningen. Beschrijf de trends en opvallende zaken in de data."
}