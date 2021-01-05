import re
import requests

URL = "https://en.wikipedia.org/wiki/%22Hello,_World!%22_program"

def do_hello(url):
    result = requests.get(url)
    print(re.findall("<titile>(.*?)<title>",result.text)[0])

if __name__ == "__main__" :
    do_hello(URL)
