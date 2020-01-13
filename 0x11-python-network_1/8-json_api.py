#!/usr/bin/python3
'''sends a POST request with the letter as a parameter.'''
if __name__ == "__main__":
    import requests
    from sys import argv
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 2:
        values = {'q': argv[1]}
        result = requests.post(url, data=values)
        try:
            json = result.json()
            if json:
                print("[{}] {}".format(json.get("id"), json.get("name")))
            else:
                print("No result")
        except Exception:
            print("Not a valid JSON")
    else:
        print("No result")
