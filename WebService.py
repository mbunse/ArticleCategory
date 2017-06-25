from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from GetArticleCategory import getArticleCategoriesFromEbay

URL_MAP = Map([
    Rule('/', endpoint='index'),
    Rule('/getArtCat', endpoint='getArtCat'),
])

def application(environ,start_response):
    request = Request(environ)
    urls = URL_MAP.bind_to_environ(request.environ)
    endpoint, values = urls.match()
    if endpoint == "index":
        with open("index.html", "r") as index:
            response = Response(index.read(),
                                mimetype='application/xhtml+xml')
            return response(environ, start_response)
    elif endpoint == "getArtCat":
        response = Response(', '.join(getArticleCategoriesFromEbay(request.args['article'])),
                            mimetype='text/plain'
                           )
        return response(environ, start_response)

if __name__ == '__main__':
    
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
