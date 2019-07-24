from urllib.parse import urlencode

domain = 'https://www.ensembl.org/'


class RequestsBase:
    def url(self):
        pass

    def params(self, *args):
        pass

    def headers(self):
        return {
            'User-Agent': 'Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        }


class SearchRequests(RequestsBase):
    def __init__(self, key):
        self.path = 'Multi/Ajax/search?'
        self.key = key

    def url(self):
        return domain + self.path + urlencode(self.params())

    def params(self):
        return {
            'q': '({key}^316 AND species:\"CrossSpecies\") OR ({key}^190'
            ' AND species:\"Human\" ) OR ( {key}^80 AND species:\"Mouse\" )'
            ' OR ({key} AND species:\"Zebrafish\")'.format(key=self.key),
            'fq': '((species:\"CrossSpecies\" AND (reference_strain:1))'
            ' OR (species:\"Human\" AND (reference_strain:1))'
            ' OR (species:\"Mouse\" AND (reference_strain:1))'
            ' OR (species:\"Zebrafish\" AND (reference_strain:1)))',
            'hl': 'true',
            'hl.fl': ['_hr', 'content', 'description'],
            'hl.fragsize': 500,
            'start': 0,
            'rows': 10,
        }


class TranscriptRequests(RequestsBase):
    def __init__(self, url=None):
        self._url = url

    def url(self):
        if self._url:
            return self._url
        return None
