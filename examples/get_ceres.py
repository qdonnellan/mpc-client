"""Get Ceres and print out some of its data"""
from mpc_client.query import Query



ceres = Query().filter(name='Ceres').limit(1).first()

print ceres.orbit.semimajor_axis
print ceres.diameter
