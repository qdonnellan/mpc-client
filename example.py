"""An example query using the Query class"""
from query import Query


q = Query()
q.limit(100)
for x in q:
    print x.orbit.orbit_type

