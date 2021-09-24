class Url(object):
    scheme = "https"
    authority = 'example.com'
    path = None
    query = None
    fragment = None

    def __init__(self, **kwargs):
        self.data = kwargs

    def __str__(self):

        return self.get_link()

    def __eq__(self, other):

        return self.get_link() == str(other)

    def get_link(self):
        scheme = self.get_scheme_str()
        authority = self.data.get('authority') or self.authority
        path = self.get_path_str()
        query = self.get_query_str()
        fragment = self.get_fragment_str()

        return f'{scheme}://{authority}{path}{query}{fragment}'

    def get_scheme_str(self):
        scheme = self.data.get('scheme')
        if scheme == 'http' or scheme == 'https':
            return scheme

        return self.scheme

    def get_query_str(self):
        query_dict = self.data.get('query')
        query_str = ''

        if query_dict is not None:
            for key, value in query_dict.items():
                if key == 'q':
                    query_str = query_str + f'?q={value}'
                elif key == 'result':
                    query_str = query_str + f'&result={value}'

        print(query_str)

        return query_str

    def get_path_str(self):
        path_list = self.data.get('path')
        path_str = ''

        if path_list is not None:
            for path in path_list:
                path_str = path_str + f'/{path}'

        return path_str

    def get_fragment_str(self):
        fragment = self.data.get('fragment')
        if fragment is not None:
            return f'#{fragment}'

        return ''

    pass


class HttpUrl(Url):
    scheme = "http"
    pass


class HttpsUrl(Url):
    scheme = "https"
    pass


class GoogleUrl(HttpsUrl):
    authority = "google.com"
    pass


class WikiUrl(HttpsUrl):
    authority = "wikipedia.org"
    pass


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
