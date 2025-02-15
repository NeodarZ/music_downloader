import os
import re
from pathlib import Path
from sh import youtube_dl, ErrorReturnCode_1
from music_dl.utils import read_file, write_file


class Extractor():

    def __init__(self, reg, url):
        self.root = None
        self.path = None
        if not reg:
            r = re.search(r'(^http(?:s|):(?:\/\/.*?\/|\/\/.*))', url)
            if r:
                self.root = r.group(1)
                try:
                    self.path = r.group(2)
                except IndexError:
                    pass
        if not self.root:
            self.root = reg.group(1)
            try:
                self.path = reg.group(2)
            except IndexError:
                pass
        self._albums = []
        self.root_path = self._root_path()
        self._update_cache(self.root)

    def _root_path(self):
        file_path = os.path.abspath(__file__)
        folder_path = Path(file_path).parent
        root_path = Path(folder_path).parent
        return root_path

    def _update_cache(self, url):
        urls_cache = []
        cache_file = Path(self.root_path, '.urls_cache.txt')
        urls_cache = read_file(cache_file)

        for url in urls_cache:
            if url.startswith(self.root):
                return
        write_file(cache_file, self.root + "," + self.__class__.__name__)

    def _yt_wrapper(self, url, output):
        try:
            for line in youtube_dl(
                    url, audio_format="mp3",
                    add_metadata=True,
                    o=output + self.filename_template,
                    ignore_errors=True,
                    _iter=True):
                print(line.strip())
        except ErrorReturnCode_1:
            pass

    def download_albums(self, output):
        for album in self._albums:
            print("Parsing " + album + "...")
            self._yt_wrapper(album, output)
