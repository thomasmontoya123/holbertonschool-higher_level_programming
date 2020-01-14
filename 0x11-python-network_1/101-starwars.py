#!/usr/bin/python3
'''sends a search request to the Star Wars API '''
if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://swapi.co/api/people/"
    values = {'search': argv[1]}
    result = requests.get(url, params=values)
    print("Number of results: {}".format(result.json().get("count")))
    for element in result.json().get("results"):
        print(element.get("name"))

    while result.json().get("next") is not None:
        next_url = result.json().get("next")
        result = requests.get(next_url, params=values)
        for element in result.json().get("results"):
            print(element.get("name"))
