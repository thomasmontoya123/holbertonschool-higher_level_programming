#!/usr/bin/python3
'''displays the body of the response.'''
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    from sys import argv

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
