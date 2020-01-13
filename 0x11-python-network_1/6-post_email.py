#!/usr/bin/python3
'''displays the body of the response.'''
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    values = {'email': argv[2]}
    result = requests.post(url, data=values)
    print(result.text)
