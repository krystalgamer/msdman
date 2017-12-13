import requests
from html.parser import HTMLParser


class MSDNConverter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.foundMainSection = False
        self.foundParameters = False
        return

    def handle_starttag(self, tag, attr):
        if tag == 'div':
            for name, value in attr:
                #first find the main section
                if not self.foundMainSection:
                    if name == 'id' and value == 'mainSection':
                        self.foundMainSection = True
                        print('Found the mainSection')

    def handle_endtag(self, tag):
        return

    def handle_data(self, data):
        return

def main():

    #Get the page as with the chrome user agent
    resp = requests.get("https://msdn.microsoft.com/en-us/library/windows/desktop/aa363858(v=vs.85).aspx", headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

    converter = MSDNConverter()
    converter.feed(resp.text)

    return

if __name__ == "__main__":
    main()
