print("base imported")
from .base import *

from .production import *

try:
    from .local import *
    print("Local mode imported")
except:
    print("Local mode is not imported")
    pass
