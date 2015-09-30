"""An example query using the Query class"""
from .query import Query


q = Query()
q.limit(1)
a = q.run()[0]

print a.name
print a.diameter
