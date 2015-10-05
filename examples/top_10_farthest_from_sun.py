"""Return the top 10 asteroids farthest from the Sun"""
from mpc_client.query import Query

q = Query()
q.limit(10)
q.filter(aphelion_distance='is_not_null')
q.order('aphelion_distance', desc=True)

for asteroid in q:
    print asteroid.designation, asteroid.orbit.aphelion_distance
