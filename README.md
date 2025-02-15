Simple tool for download all album from an artist

# Install

```
poetry install
```

## Dependencies

- youtube-dl

# Usage

```
poetry run music-dl
```

```
usage: music-dl [-h] [--url URL] [--update] [--file FILE] [--output OUTPUT]

Custom album downloader tool

optional arguments:
  -h, --help       show this help message and exit
  --url URL        link to the file to download
  --update         update all albums from cache
  --file FILE      read url from file
  --output OUTPUT  folder where to put downloaded albums. Default to: <app_installed_folder>/out/
```

# Suported website

- [x] Bandcamp
- [x] Soundcloud
