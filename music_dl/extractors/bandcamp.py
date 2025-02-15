import re
import logging
import requests
from bs4 import BeautifulSoup

from music_dl.extractors.common import Extractor

class bandcamp(Extractor):
    pattern = re.compile(r'(http(?:s|):\/\/.*bandcamp.com)')
    filename_template = "%(artist)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s"

    def __init__(self, reg, url):
        super().__init__(reg, url)

    def get_albums(self):
        r = requests.get(self.root)
        soup = BeautifulSoup(r.text, 'html.parser')
        items = soup.select('a[href]')
        for item in items:
            if '/album' in item['href'] and \
                    not item['href'].startswith("http"):
                url = self.root.rstrip('/') + item['href']
                if url not in self._albums:
                    self._albums.append(url)

        if not self._albums:
            logging.warning(f"No albums found at {self.root} ????")
