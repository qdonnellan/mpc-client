"""An example query using the Query class"""
from query import Query


q = Query()
q.limit(10)
for x in q:
    print x.name, x.orbit.updated
