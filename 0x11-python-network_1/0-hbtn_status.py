#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status.'''

if __name__ == "__main__":
    import urllib.request as urlib

    with urlib.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("    - type: {}".format(type(html)))
        print("    - content: {}".format(html))
        print("    - utf8 content: {}".format(html.decode('utf-8')))
