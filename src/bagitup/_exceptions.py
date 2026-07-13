# Bagitup: a command-line tool to back up or sync git-based projects.
#
# Copyright (c) 2026 Institut des Géosciences de l'Environnement, Grenoble.
#
# License: BSD 3-clause "new" or "revised" license (BSD-3-Clause).

class InternalError(Exception):
    """Signal an internal exception.

    By internal exception, we mean an exception that should never be raised
    (it should not be attainable not matter what the user inputs are), but that
    is triggered by a safety check.

    """
    pass
