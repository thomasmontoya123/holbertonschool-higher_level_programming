#!/usr/bin/python3
'''displays the body of the response.'''
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    try:
        result = requests.get(url)
        result.raise_for_status()
        print(result.text)
    except requests.exceptions.RequestException as e:
        print("Error code: {}".format(e.response.status_code))
