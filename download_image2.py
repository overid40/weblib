from html.parser import HTMLParser
from http.client import HTTPConnection
import base64


class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return

        if not hasattr(self, 'result'):
            self.result = []

        for name, value in attrs:
            if name == 'src':
                self.result.append(value)


def main():
    conn = HTTPConnection('www.google.co.kr')
    conn.request('GET', '/')
    response = conn.getresponse()

    url = 'http://www.google.co.kr'

    charset = response.headers.get_content_charset()
    data = response.read().decode(charset)
    response.close()

    print("\n>>>>>>>>>> Fetch Image from", url)
    parser = ImageParser()
    parser.feed(data)
    datasets = set(x for x in parser.result)
    print('\n'.join(sorted(datasets)))

    for dataset in datasets:
        a = url+dataset
        print(a)
        conn.request('GET', dataset)
        response = conn.getresponse()
        binary = response.read()
        response.close()

        print(response.status, response.reason)

        with open("사진.png", mode="bw") as w:
            w.write(binary)
            print("파일이 저장되었습니다.")


if __name__ == '__main__':
    main()