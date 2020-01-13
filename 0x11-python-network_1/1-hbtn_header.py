#!/usr/bin/python3
'''Displays the value of the X-Request-Id'''

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as response:
        html = response.info()
        print(html['X-Request-Id'])
