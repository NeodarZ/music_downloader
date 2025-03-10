#!/bin/python

import os
import argparse
import logging
from pathlib import Path
from music_dl.extractors.job import DlJob
from music_dl.utils import read_file

from music_dl.utils import NoExtractorException


def run():
    module_path = os.path.abspath(__file__)
    ROOT = Path(module_path).parent

    parser = argparse.ArgumentParser(description="Custom album downloader tool")
    parser.add_argument('--url', help="link to the file to download")
    parser.add_argument(
        '--update', help='update all albums from cache', action="store_true")
    parser.add_argument('--file', help="read url from file")
    parser.add_argument(
        '--output',
        help="folder where to put downloaded albums. "
        "Default to: " + str(ROOT) + "/out/",
        default=str(ROOT) + "/out/"
    )
    parser.add_argument('--extractor', help="name of the extractor")

    args = parser.parse_args()

    if not args.output.endswith("/"):
        args.output = args.output + "/"

    if args.update:
        print('Updating from cache...')


        cache_file = Path(ROOT, '.urls_cache.txt')

        urls_cache = read_file(cache_file)

        urls_failed = []

        for url in urls_cache:
            try:
                args.extractor = url.split(',')[1]
            except IndexError:
                pass
            try:
                dl_job = DlJob(url, args.output, args.extractor)
                dl_job.run()
            except NoExtractorException as exc:
                logging.error(exc)

        if urls_failed:
            print("There was no extractors for the following urls:")
            for url_failed in urls_failed:
                print(url_failed)

    if args.url:
        print('Downloading from url...')
        try:
            dl_job = DlJob(args.url, args.output, args.extractor)
            dl_job.run()
        except NoExtractorException as exc:
            logging.error(exc)

    if args.file:
        print("Downloading from file...")

        urls = read_file(args.file)

        urls_failed = []

        for url in urls:
            if url:
                try:
                    dl_job = DlJob(url, args.output, args.extractor)
                    dl_job.run()
                except NoExtractorException as exc:
                    logging.error(exc)
                    urls_failed.append(exc)

        if urls_failed:
            print("There was no extractors for the following urls:")
            for url_failed in urls_failed:
                print(url_failed)

    if not args.url and not args.update and not args.file:
        parser.print_help()
