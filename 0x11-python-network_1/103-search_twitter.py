#!/usr/bin/python3
'''twitter api consult
    tutorial =
    http://benalexkeen.com/interacting-with-the-twitter-api-using-python/ '''
if __name__ == "__main__":
    import base64
    from sys import argv
    import requests
    '''in 1'''
    client_key = argv[1]
    client_secret = argv[2]
    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')
    '''in 2'''
    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    auth_data = {
        'grant_type': 'client_credentials'
    }
    '''in 3'''
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    access_token = auth_resp.json()['access_token']

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    search_params = {
        'q': argv[3],
        'result_type': 'recent',
        'count': 5
    }

    search_url = '{}1.1/search/tweets.json'.format(base_url)
    search_resp = requests.get(search_url, headers=search_headers,
                               params=search_params).json()

    for twit in search_resp.get("statuses"):
        print("[{}] {} by {}".format(twit.get("id"),
                                     twit.get("text"),
                                     twit.get("user").get("name")))
