# urlparse

from urllib.parse import urlparse, urlsplit, urljoin, parse_qs

url = "http://www.python.org:80/guido/python.html;philosophy?a=10&b=20#here"

result = urlparse(url)
print(result)