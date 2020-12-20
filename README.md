Simple tool for download all album from an artist

# Install

```
pip install -r requirements.txt
```

## Dependencies

- youtube-dl

# Usage

```
usage: main.py [-h] [--url URL] [--update] [--file FILE] [--output OUTPUT]

Custom album downloader tool

optional arguments:
  -h, --help       show this help message and exit
  --url URL        link to the file to download
  --update         update all albums from cache
  --file FILE      read url from file
  --output OUTPUT  folder where to put downloaded albums. Default to: <app_installed_folder>/out/
```

# Suuported website

- [x] Bandcamp
- [x] Soundcloud
