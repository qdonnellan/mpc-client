# mpc-client
A python client for consuming the MPC (Minor Planet Center) web service. This project is not affiliated with the Minor Planet Center in any way, I just thought their web service was super cool, and I wanted to provide a useful python client for other people interested. Please visit the MPC for more details about this web service: [http://minorplanetcenter.net/web_service][1]

## Install
Currently, the only way to use this client is to download this git repo manually. Eventually I'll add this to pypi.

    git clone git@github.com:qdonnellan/mpc-client.git

## Usage
I'm still working out the details on usage, but in general this is how you would query the MPC web service:

```
from mpc_client.query import Query

q = Query()
q.filter(eccentricity_max=0.95)
q.limit(10)

for asteroid in q:
    print asteroid.name, asteroid.orbit.semimajor_axis
```

### Filters
Filters can be applied all at once...

```
q = Query()
q.filter(eccentricity_max=0.95, eccentricity_min=0.1, orbit_min=100)
```

one at a time...

```
q = Query()
q.filter(eccentricity_max=0.95)
q.filter(eccentricity_min=0.1)
q.filter(orbit_min=100)
```

or chained together...

```
q = Query()
q.filter(eccentricity_max=0.95).filter(eccentricity_min=0.1).filter(orbit_min=100)
```

### Query only runs when needed

The query of the actual mpc_service is only run when you access the query. You can either run the query explicitly:

```
q = Query()
q.filter(eccentricity_max=0.95)
results = q.run()
```

In the above example, the query is executed when you call `q.run()`. 

Alternatively, you build a query and then implicitly force it to run when you attempt to iterate through the results. For example:

```
q = Query()
q.filter(eccentricity_max=0.95)
for result in q:
    # do something
```

This query is actually run when you call `for result in q` since the results are needed to iterate through the for loop. 

### Resulting Quantities are unit-aware




[1]: http://minorplanetcenter.net/web_service