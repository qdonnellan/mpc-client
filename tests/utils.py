import os

def local_cassette(filename):
    """return the path for the xml fixture"""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, 'cassettes', filename)