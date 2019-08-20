# AZLyrics scraper

[![HitCount](http://hits.dwyl.io/AlbertSuarez/azlyrics-scraper.svg)](http://hits.dwyl.io/AlbertSuarez/azlyrics-scraper)
[![GitHub stars](https://img.shields.io/github/stars/AlbertSuarez/azlyrics-scraper.svg)](https://GitHub.com/AlbertSuarez/azlyrics-scraper/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/AlbertSuarez/azlyrics-scraper.svg)](https://GitHub.com/AlbertSuarez/azlyrics-scraper/network/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/AlbertSuarez/azlyrics-scraper.svg)](https://github.com/AlbertSuarez/azlyrics-scraper)
[![GitHub contributors](https://img.shields.io/github/contributors/AlbertSuarez/azlyrics-scraper.svg)](https://GitHub.com/AlbertSuarez/azlyrics-scraper/graphs/contributors/)
[![GitHub license](https://img.shields.io/github/license/AlbertSuarez/azlyrics-scraper.svg)](https://github.com/AlbertSuarez/azlyrics-scraper/blob/master/LICENSE)

[Box folder URL](https://app.box.com/s/vats4n6slxtknuaxz58mxlo6ry8v04pd) | [Static repo website](https://asuarez.dev/azlyrics-scraper/)

🎵 AZLyrics scraper for getting all the song lyrics and publishing to Box.

## Python requirements

This project is using Python3. All these requirements have been specified in the `requirements.lock` file.

1. [Requests](https://2.python-requests.org/en/master/): used for retrieving the HTML content of a website.
2. [BeautifulSoup](https://pypi.org/project/beautifulsoup4/): used for scraping an HTML content.
3. [Tor](https://2019.www.torproject.org/docs/debian.html.en): used for making requests anonymous using other IPs.
4. [Stem](https://stem.torproject.org/): used for authentificating every request with a different IP.
5. [Fake User-Agent](https://pypi.org/project/fake-useragent/): used for using random User-Agent's for every request.
6. [Unidecode](https://pypi.org/project/Unidecode/): used for cleaning strings from weird characters.
7. [Box SDK](https://github.com/box/box-python-sdk): used for uploading/downloading files to/from Box Cloud Storage.

## Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage

To run this script, please execute the following from the root directory:

1. Setup virutal environment

2. Install dependencies

  ```bash
  pip3 install -r requirements.lock
  ```

3. Move [JWT configuration](#jwt-configuration) file from Box API

4. Install [Tor browser](https://2019.www.torproject.org/docs/debian.html.en)

5. Configure Tor IP renewal editting `/etc/tor/torrc` file

   ```
   ControlPort 9051
   CookieAuthentication 1
   ```

6. Restart Tor browser

  ```bash
  sudo service tor restart
  ```

7. Run the script

  ```bash
  python3 -m src
  ```

## JWT configuration

In order to use Box Cloud Storage API in a secure way, this project is configured for using their service with the JWT authentication. After following the [tutorial](https://developer.box.com/docs/construct-jwt-claim-manually), we will obtain a configuration file which will have to be located under `data` folder with the name of `jwt_config.json` as the `__init__.py` configuration file says:

```python
# Box integration
BOX_CONFIG_FILE_PATH = 'data/jwt_config.json'
```

## Authors

- [Albert Suàrez](https://github.com/AlbertSuarez)

## License

MIT © AZLyrics scraper
