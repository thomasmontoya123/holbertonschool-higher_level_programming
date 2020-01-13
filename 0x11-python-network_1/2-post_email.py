#!/usr/bin/python3
'''displays the body of the response.'''
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    from sys import argv

    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
