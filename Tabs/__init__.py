"""Tabs package - makes the Tabs directory importable as a package.
This file is intentionally minimal; it allows `import Tabs` to work for tools
like Pylance and Python import resolution.
"""

# Expose common names for convenience (optional)
from . import home  # noqa: F401
from . import kc    # noqa: F401
from . import diagnosis  # noqa: F401
from . import result  # noqa: F401
from . import talk2doc  # noqa: F401
