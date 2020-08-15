import logging
import re
import importlib
import sys

from utils import NoExtractorException

extrs = [
    'bandcamp'
]


class DlJob():

    def __init__(self, url, output, extractor=None):
        if extractor in extrs:
            cls = self._get_class(extractor)
            self.extr = cls(reg=None, url=url)
        else:
            self.extr = self._find(url)
        self.output = output
        self._albums = []
        if not self.extr:
            raise NoExtractorException("No extractor found for " + url + ".")

    def _find(self, url):
        for cls in self._list_extractors():
            match = cls.pattern.match(url)
            if match:
                return cls(match, url)

    def _list_extractors(self):
        for extr in iter(extrs):
            module = importlib.import_module('.'+extr, __package__)
            yield from self._add_module(module)

    def _add_module(self, module):
        classes = self._get_classes(module)
        for cls in classes:
            cls.pattern = re.compile(cls.pattern)
        return classes

    def _get_classes(self, module):
        return [
            cls for cls in module.__dict__.values() if (
                hasattr(cls, "pattern") and cls.__module__ == module.__name__
            )
        ]

    def _get_class(self, extractor):
        module = importlib.import_module('.' + extractor, __package__)
        classes = self._get_classes(module)
        for cls in classes:
            if cls.__name__ == extractor:
                return cls

    def run(self):
        self.extr.get_albums()
        self.extr.download_albums(self.output)
