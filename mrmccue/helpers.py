import functools
import bs4
from htmlmin import minify
#########################################################
# Both of the following functions use BeautifulSoup to  #
# parse html and change the output. In the case of the  #
# first function wrapper, we have BeautifulSoup make    #
# the html returned by the wrapped function look better #
#                                                       #
# The Second wrapper strips whitespace from the html    #
# to make the html smaller                              #
#########################################################
def prettify(route_function):
    @functools.wraps(route_function)
    def wrapped(*args, **kwargs):
        yielded_html = route_function(*args, **kwargs)
        soup = bs4.BeautifulSoup(yielded_html, 'html.parser')
        return soup.prettify()

    return wrapped

def uglify(route_function):
    @functools.wraps(route_function)
    def wrapped(*args, **kwargs):
        yielded_html = route_function(*args, **kwargs)
        minified = minify(yielded_html,
                          remove_comments=True,
                          remove_empty_space=True)
        return str(minified)

    return wrapped
