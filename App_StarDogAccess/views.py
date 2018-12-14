from django.http import HttpResponse
from SPARQLWrapper import SPARQLWrapper, POST, DIGEST
from rdflib.plugins.stores import sparqlstore
from rdflib import Graph, Literal, URIRef
import rdflib

# Create your views here.
def index(request):

    """write data into sht stardog"""
    # Define the Stardog store
    endpoint = 'http://123.206.66.105:5820/myDB/query'
    store = sparqlstore.SPARQLUpdateStore()
    store.open((endpoint, endpoint))
    store.setCredentials('admin', 'admin')

    # Identify a named graph where we will be adding our instances.
    default_graph = URIRef('http://example.org/default-graph')
    ng = Graph(store, identifier=default_graph)

    g = Graph()
    g.parse('./sample-concepts.ttl', format='turtle')
    # Serialize our named graph to make sure we got what we expect.
    print(g.serialize(format='turtle'))

    ng.update(
        u'INSERT DATA { %s }' % g.serialize(format='nt')
    )


    """read data from stardog"""

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