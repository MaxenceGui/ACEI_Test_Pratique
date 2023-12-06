import flask as f
import json
import traceback

from back_end.CommunicationBD import CommunicationBD

app = f.Flask(__name__)

app.secret_key = "ACEI_TEST"

def start_flask():
    app.run(debug=True, host="127.0.0.1", port="5000")

@app.route('/add_players', methods=['POST'])
def add_player_to_database():
    try:
        if f.request.method == 'POST':
            info = f.request.get_json()
            result = add_player_to_database(info)
            return json.dumps(result)
    except Exception as e:
        print(traceback.format_exception(e))
        return f.jsonify({'error': str(e)})
    
@app.route('/fetch_players', methods=['POST'])
def fetch_player_from_database():
    try:
        if f.request.method == 'POST':
            result = fetch_player_from_database()
            return json.dumps(result)
    except Exception as e:
        return f.jsonify({'error': str(e)})
    
@app.route('/delete_list', methods=['POST'])
def delete_list():
    try:
        if f.request.method == 'POST':
            result = delete_list()
            return json.dumps(result)
    except Exception as e:
        return f.jsonify({'error': str(e)})
    
def add_player_to_database(info: str) -> str:
    try:
        print(info)
        bd = CommunicationBD()
        bd.connection_bd()
        bd.insert(info)
    except Exception as e:
        print(traceback.format_exception(e))
        return (traceback.format_exception(e))
    finally:
        bd.close_db()

    return "Success"

def fetch_player_from_database() -> str:
    try:
        bd = CommunicationBD()
        bd.connection_bd()
        return bd.select()
    except Exception as e:
        return (traceback.format_exception(e))
    finally:
        bd.close_db()

def delete_list() -> str:
    try:
        bd = CommunicationBD()
        bd.connection_bd()
        bd.delete()
    except Exception as e:
        return (traceback.format_exception(e))
    finally:
        bd.close_db()