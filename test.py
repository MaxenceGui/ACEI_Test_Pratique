import urllib.request
import urllib.parse
import json

from random import randint

IP_ADDRESS = "127.0.0.1"
PORT = "5000"




def test_add_player():
    json_data =json.dumps(
        [["Sylvain Charlebois", 25, 3, 15, 18, 76, -3],
         ["Robert Charlebois", 35, 43, 67, 43+67, 20, 11],
         ["Maxime Charlebois", 78, 90, 5, 95, 12, -27],
         ["Gishlain Charlebois", 267, 57, 98, 57+98, 110, 49],
         ["Martin Charlebois", 90, 12, 6, 18, 2, 30]])
    data = json_data.encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    request = urllib.request.Request(f"http://{IP_ADDRESS}:{PORT}/add_players", data=data, headers=headers)
    response = urllib.request.urlopen(request)
    variable = json.loads(response.read())
    print(variable)

def test_fetch_player():
    json_data = json.dumps("something")
    data = json_data.encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    request = urllib.request.Request(f"http://{IP_ADDRESS}:{PORT}/fetch_players", data=data, headers=headers)
    response = urllib.request.urlopen(request)
    variable = json.loads(response.read())
    print(variable)

def test_delete():
    request = urllib.request.Request(f"http://{IP_ADDRESS}:{PORT}/delete_list")
    response = urllib.request.urlopen(request)
    variable = json.loads(response.read())
    print(variable)

def test_main():
    #test_add_player()
    #test_fetch_player()
    test_delete()


if __name__ == "__main__":
    quit(test_main())