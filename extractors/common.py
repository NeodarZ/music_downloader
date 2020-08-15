import os
from pathlib import Path
from sh import youtube_dl
from utils import read_file, write_file


class Extractor():

    def __init__(self, reg, url):
        self.root = reg.group(1)
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
        write_file(cache_file, self.root)

    def _yt_wrapper(self, url, output):
        for line in youtube_dl(
                url, audio_format="mp3",
                add_metadata=True,
                o=output + self.filename_template,
                _iter=True):
            print(line.strip())

    def download_albums(self, output):
        for album in self._albums:
            print("Parsing " + album + "...")
            self._yt_wrapper(album, output)
