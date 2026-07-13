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
    "--from-type",
    help="Type of repository of origin (local, Github, or GitLab).",
    required=True,
)
parser.add_argument(
    "--from-location",
    help=(
        "Repository of origin. Can be "
        "/path/to/local/git/repo, or "
        "username/reponame (for online-hosted repositories)."
    ),
    required=False,
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "--from-auth-token",
    help="Authentication token.",
)
group.add_argument(
    "--from-auth-token-envvar",
    help="Environmental variable containing authentication token.",
)
group.add_argument(
    "--from-auth-login",
    help=("Login name and password (for security reasons, this "
          "authentication method is not recommended)."),
    nargs=2,
)

args = parser.parse_args()
