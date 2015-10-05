"""Save a query to a local file for use later"""
from mpc_client.query import Query


q = Query()
q.limit(100)
q.save_to_file('first_100_asteroids.json')
