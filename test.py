import urllib.request
import urllib.parse
import json

IP_ADDRESS = "127.0.0.1"
PORT = "5000"

def test_add_player():
    json_data =json.dumps(["Sylvain Charlebois", 25, 3, 15, 18, 76, -3])
    data = json_data.encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    request = urllib.request.Request(f"http://{IP_ADDRESS}:{PORT}/add_players", data=data, headers=headers)
    response = urllib.request.urlopen(request)
    variable = json.loads(response.read())
    print(variable)

def test_fetch_player():
    pass

def test_main():
    test_add_player()


if __name__ == "__main__":
    quit(test_main())