"""Load a previously saved query"""
from mpc_client.query import Query


# This expects that 'examples/save_to_file.json' has already run
q = Query().load_from_file('first_100_asteroids.json')
for asteroid in q:
    print asteroid.name, asteroid.orbit.semimajor_axis
