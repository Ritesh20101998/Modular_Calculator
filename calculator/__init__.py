"""
Calculator package: exposes all main calculator modules for import.

Modules:
- basic:      Basic arithmetic operations
- finance:    Financial calculations (interest, risk, etc.)
- graphical:  Plotting and visualization
- planning:   Financial planning tools (SIP, Lumpsum, TVM)
- scientific: Scientific and advanced math functions
"""
__all__ = ["basic", "finance", "graphical", "planning", "scientific"]
from . import basic
from . import finance
from . import graphical
from . import planning
from . import scientific
