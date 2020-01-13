#!/usr/bin/python3
'''displays the value of the variable X-Request-Id'''
if __name__ == "__main__":
    import requests
    from sys import argv

    html = requests.get(argv[1])
    print(html.headers.get('X-Request-Id'))
