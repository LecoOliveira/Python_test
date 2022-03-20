import requests

url = 'http://g1.com.br/' #Change the url
file = open('/usr/share/dirb/wordlists/common.txt') #Change to your wordlist path
lines = file.readlines()

try:
    for line in lines:
        response_http = requests.get(url + line)

        if response_http.status_code != 404:
            print url + line + str(response_http.status_code)

except KeyboardInterrupt:
    print 'End program.'