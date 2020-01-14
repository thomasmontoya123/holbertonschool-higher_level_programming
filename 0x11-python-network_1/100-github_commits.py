#!/usr/bin/python3
'''list 10 commits (from the most recent to oldest)'''
if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/repos/"+argv[2]+"/"+argv[1]+"/commits"
    result = requests.get(url)
    json = result.json()
    for commit in json[:10]:
        author_name = commit.get("commit").get("author").get("name")
        sha = commit.get("sha")
        print("{}: {}".format(sha, author_name))
