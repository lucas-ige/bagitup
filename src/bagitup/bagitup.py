# Bagitup: a command-line tool to back up or sync git-based projects.
#
# Copyright (c) 2026 Institut des Géosciences de l'Environnement, Grenoble.
#
# License: BSD 3-clause "new" or "revised" license (BSD-3-Clause).

import argparse

parser = argparse.ArgumentParser(
    prog="bagitup",
    description="Back up or sync git-based projects",
    epilog="This programme is released under the BSD-3-Clause license.",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

args = parser.parse_args()
