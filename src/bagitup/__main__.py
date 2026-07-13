# Bagitup: a command-line tool to back up or sync git-based projects.
#
# Copyright (c) 2026 Institut des Géosciences de l'Environnement, Grenoble.
#
# License: BSD 3-clause "new" or "revised" license (BSD-3-Clause).

from ._cmdargs import args
from ._interface import GithubRepo

if args.from_type == "Github":
    origin = GithubRepo(args, "from")
