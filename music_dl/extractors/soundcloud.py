import re
import logging
import requests
from bs4 import BeautifulSoup

from music_dl.common import Extractor

class soundcloud(Extractor):
    pattern = re.compile(r'(http(?:s|):\/\/.*soundcloud.com)(.*)')
    filename_template = "%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s"

    def __init__(self, reg, url):
        super().__init__(reg, url)

    def get_albums(self):
        # We directly use youtube-dl soudcloud albums management
        # (It download all songs by an artist
        self._albums.append(self.root + self.path)
