# Bagitup: a command-line tool to back up or sync git-based projects.
#
# Copyright (c) 2026 Institut des Géosciences de l'Environnement, Grenoble.
#
# License: BSD 3-clause "new" or "revised" license (BSD-3-Clause).

import argparse

parser = argparse.ArgumentParser(
    prog="bagitup",
    description="Back up or sync git-based projects.",
    epilog="This programme is released under the BSD-3-Clause license.",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

# Repository of origin

parser.add_argument(
    "--orig-type",
    help="Type of repository of origin.",
    choices=("local", "Github", "Gitlab"),
    required=True,
)
parser.add_argument(
    "--orig-location",
    help=(
        "Repository of origin. Can be /path/to/local/git/repo or "
        "username/reponame (for online-hosted repositories)."
    ),
    required=True,
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "--orig-auth-token",
    help="Authentication token for repository of origin.",
)
group.add_argument(
    "--orig-auth-token-envvar",
    help=(
        "Environmental variable containing authentication token for "
        "repository of origin."
    ),
)
group.add_argument(
    "--orig-auth-login",
    help=(
        "Login name and password for repository of origin (for security "
        "reasons, this authentication method is not recommended)."
    ),
    nargs=2,
)

# Destination repository

parser.add_argument(
    "--dest-type",
    help="Type of destination repository.",
    choices=("local", "Github", "Gitlab"),
    required=True,
)
parser.add_argument(
    "--dest-location",
    help=(
        "Destination repository. Can be /path/to/local/git/repo or "
        "username/reponame (for online-hosted repositories)."
    ),
    required=True,
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "--dest-auth-token",
    help="Authentication token for destination repository.",
)
group.add_argument(
    "--dest-auth-token-envvar",
    help=(
        "Environmental variable containing authentication token for "
        "destination repository."
    ),
)
group.add_argument(
    "--dest-auth-login",
    help=(
        "Login name and password for destination repository (for security "
        "reasons, this authentication method is not recommended)."
    ),
    nargs=2,
)

# Parse the actual command-line arguments

args = parser.parse_args()
