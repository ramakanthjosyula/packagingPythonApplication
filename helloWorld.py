import re
import requests

URL = 'https://en.wikipedia.org/wiki/"Hello,_World!"_program'


def do_hello(url):
    result = requests.get(url)
    return re.findall("<title>(.*?)</title>", result.text)[0]


if __name__ == "__main__":
    print(do_hello(URL))
