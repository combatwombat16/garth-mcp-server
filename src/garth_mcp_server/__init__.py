from .app import server
from . import tools  # noqa: F401
from .cli import main

__version__ = "0.0.9"

if __name__ == "__main__":
    main()
