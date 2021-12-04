from urllib.request import urlopen
from urllib.error import HTTPError

def download(url):
    print("Downloading:",url)
    try:
        html = urllib.urlopen(url).read()
    except HTTPError as e:
        print("Download error:",e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                #recursively retry 5xx HTTP errors
                return download(url, num_retries -1)
    return html

download('http://httpstat.us/500')
