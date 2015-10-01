"""An example query using the Query class"""
from .query import Query
from astropy import units as u


ceres = Query().filter(name='Ceres').limit(1).first()
print ceres.orbit.semimajor_axis
print ceres.orbit.semimajor_axis + (1000 * u.km)