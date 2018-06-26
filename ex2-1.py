# urlparse

from urllib.parse import urlparse, urlsplit, urljoin, parse_qs

url = "http://www.python.org:80/guido/python.html;philosophy?a=10&b=20#here"

result = urlparse(url)
result1 = urlsplit(url)
result2 = urljoin('', url)
result3 = parse_qs(url)

print(result)
print(result1)
print(result2)
print(result3)