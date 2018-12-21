from SPARQLWrapper import SPARQLWrapper, POST, DIGEST
from rdflib.plugins.stores import sparqlstore
from rdflib import Graph, Literal, URIRef
from django.http import HttpResponse
import rdflib

queryString = "INSERT DATA { <http://example/book1>  <http://purl.org/dc/elements/1.1/subject>  \"WeiHaiJunbook\". }"
sp = SPARQLWrapper("http://123.206.66.105:5820/TestDB/query")

#sp.setHTTPAuth(DIGEST)
sp.setCredentials("admin", "admin")
sp.setMethod(POST)

# add a default graph, though that can also be part of the query string
#sp.addDefaultGraph("http://localhost:5820/myDB/graph-selected")

sp.setQuery(queryString)


