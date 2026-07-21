# Bagitup: a command-line tool to back up or sync git-based projects.
#
# Copyright (c) 2026 Institut des Géosciences de l'Environnement, Grenoble.
#
# License: BSD 3-clause "new" or "revised" license (BSD-3-Clause).

from ._cmdargs import args
from ._interface import GithubRepo

if args.orig_type == "Github":
    origin = GithubRepo(args, "orig")
else:
    msg = f"Origin repository type: {args.orig_type}"
    raise NotImplementedError(msg)

if args.from_type == "local":
    pass
else:
    msg = f"Destination repository type: {args.dest_type}"
    raise NotImplementedError(msg)
