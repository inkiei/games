from flask import Flask, render_template
import requests

app = Flask(__name__)

# URL van de API waar de JSON data staat
API_URL = "https://my-json-server.typicode.com/inkiei/games/games"

@app.route('/')
def index():
    # Haal de data op van de API
    response = requests.get(API_URL)
    games = response.json()  # Zet de JSON-data om naar een Python object
    
    return render_template('index.html', games=games)

app.run(host='0.0.0.0', port=5000)
