from bs4 import BeautifulSoup


class RightmoveParser:
    def get_flats(self, raw_page):
        soup = BeautifulSoup(raw_page, 'html.parser')
        print('Parsing ' + soup.title.string)
        return [i.get('id') for i in soup.find_all('div', {'class': 'is-list'})]
