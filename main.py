#!/bin/python

import os
import argparse
from pathlib import Path
from extractors.job import DlJob
from utils import read_file

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
    default=str(ROOT) + "/out/")

args = parser.parse_args()

if not args.output.endswith("/"):
    args.output = args.output + "/"

if args.update:
    print('Updating from cache...')


    cache_file = Path(ROOT, '.urls_cache.txt')

    urls_cache = read_file(cache_file)

    for url in urls_cache:
        dl_job = DlJob(url, args.output)
        dl_job.run()

if args.url:
    print('Downloading from url...')
    dl_job = DlJob(args.url, args.output)
    dl_job.run()

if args.file:
    print("Downloading from file...")

    urls = read_file(args.file)

    for url in urls:
        if url:
            dl_job = DlJob(url, args.output)
            dl_job.run()

if not args.url and not args.update and not args.file:
    parser.print_help()
