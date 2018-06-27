import webbrowser

BASE_IMAGE_SEARCH_URL = 'https://www.google.com/search?tbm=isch&as_q={}&tbs=isz:lt,islt:4mp,sur:fmc'


def google_image_search(search_term):
    webbrowser.open(BASE_IMAGE_SEARCH_URL.format(search_term), new=0, autoraise=True)
