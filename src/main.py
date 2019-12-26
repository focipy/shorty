""""
Shorty

Shorty is a simple url shortener program to shorten and customise urls.
"""

from api import app

__author__ = "Aaron Frank"
__copyright__ = "Copyright 2019 FociPy"
__credits__ = ["Aaron Frank"]

__license__ = "MIT"
__version__ = "0.0.1"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
