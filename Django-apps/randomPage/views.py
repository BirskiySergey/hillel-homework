from django.shortcuts import render
import string
import random
from urllib.parse import urlparse, parse_qs


# Create your views here.


def index(request):
    def get_query_key(arguments, key):
        if key in arguments:
            return arguments[key][0]
        return 0

    def is_on_params(param):
        if int(param) == 1:
            return True

        return False

    def get_available_length(number):
        if int(number) > 100:
            return 100
        elif int(number) < 0:
            return 0

        return int(number)

    def get_random_letters(l=0, s=0, d=0):
        new_string = string.ascii_letters
        specials_char = "!@%/()=?+.-"

        if is_on_params(s):
            new_string = new_string + specials_char

        if is_on_params(d):
            new_string = new_string + string.digits

        print(new_string)
        return ''.join(random.choice(new_string) for i in range(get_available_length(l)))

    query_string = request.META['QUERY_STRING']
    fake_url = f'example.com?{query_string}'
    query_params = parse_qs(urlparse(fake_url).query)

    length = get_query_key(query_params, 'length')
    specials = get_query_key(query_params, 'specials')
    digits = get_query_key(query_params, 'digits')

    return render(request, 'random.html', {'data': get_random_letters(length, specials, digits)})
