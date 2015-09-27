# mpc-client: A python client for consuming the MPC (Minor Planet Center) web service.

## Install
Currently, the only way to use this client is to download this git repo manually. Eventually I'll add this to pypi.

    git clone git@github.com:qdonnellan/mpc-client.git

## Usage
I'm still working out the details on usage, but in general this is how you would query the MPC web service:

    from mps_client.query import Query

    q = Query()
    q.filter(eccentricity_max=0.95)
    q.limit(10)

    for asteroid in q:
        print asteroid.name, asteroid.orbit.semimajor_axis

