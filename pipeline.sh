# Problema: Arqueología Galáctica: Construir el Diagrama de Hertzsprung-Russell>
# 1. Access the Gaia database, getting the columns

QUERY="SELECT+TOP+7000+*+FROM+%22I/355/gaiadr3%22+WHERE+Plx%3E4"
URL="https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query=${QUERY}"
echo $URL

wget -O gaiaDR3.csv "$URL"

# 2. run the python codes
python constructor_db.py

python analisis_visual.py

# 3. show the result in the systems image viewer
start resultado.png
