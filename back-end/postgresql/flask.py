import flask as f
import json

app = f.Flask(__name__)

app.secret_key = "ACEI_TEST"

def start_flask():
    app.run(debug=True, host="10.10.10.10", port="5000")

@app.route('/add_players', methods=['POST'])
def add_player_to_database():
    try:
        if f.request.method == 'POST':
            info = f.request.get_json()
            result = add_player_to_database(info)
            return json.dumps(result)
    except Exception as e:
        return f.jsonify({'error': str(e)})
    
@app.route('/fetch_players', methods=['POST'])
def fetch_player_from_database():
    try:
        if f.request.method == 'POST':
            result = fetch_player_from_database()
            return json.dumps(result)
    except Exception as e:
        return f.jsonify({'error': str(e)})

def add_player_to_database():
    print("Get ready to receive player")