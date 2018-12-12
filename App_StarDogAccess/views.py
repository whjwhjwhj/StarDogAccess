from django.http import HttpResponse
from SPARQLWrapper import SPARQLWrapper, POST, DIGEST

# Create your views here.
def index(request):

    queryString = "SELECT * WHERE { ?s ?p \"阿胶汤2\". }"
    sp = SPARQLWrapper("http://123.206.66.105:5820/myDB/query")

    #sp.setHTTPAuth(DIGEST)
    sp.setCredentials("admin", "admin")
    sp.setMethod(POST)

    # add a default graph, though that can also be part of the query string
    #sp.addDefaultGraph("http://localhost:5820/myDB/graph-selected")

    sp.setQuery(queryString)
    sp.setReturnFormat("json")
    ret = sp.query()
    for v in ret:
        print(v)

    return HttpResponse("Hello, World!  You're at the polls index.")