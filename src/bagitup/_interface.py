# Bagitup: a command-line tool to back up or sync git-based projects.
#
# Copyright (c) 2026 Institut des Géosciences de l'Environnement, Grenoble.
#
# License: BSD 3-clause "new" or "revised" license (BSD-3-Clause).

from abc import ABC, abstractmethod
import github
from . _exceptions import InternalError

class Repo(ABC):
    """A git repository."""

    @abstractmethod
    def __init__(self, args, which):
        """Initialize instance.

        Parameters
        ----------
        args: Namespace
            User-provided command-line arguments.
        which: "from" | "to"
            Whether we are connecting to the origin or the desination repo.

        """
        pass

class GithubRepo(Repo):
    """A Github repository."""

    def __init__(self, args, which):
        """Cf. Repo.__init__."""
        if getattr(args, f"{which}_type") != "Github":
            msg = "Bad type of repository."
            raise InternalError(msg)

        token = getattr(args, f"{which}_auth_token")
        token_env = getattr(args, f"{which}_auth_token_envvar")
        login = getattr(args, f"{which}_auth_login")

        if sum(i is not None for i in [token, token_env, login]) > 1:
            msg = "Cannot determine authentication method."
            raise InternalError(msg)

        if token is not None:
            auth = github.Auth.Token(token)
        elif token_env is not None:
            auth = github.Auth.Token(os.environ[token_env])
        elif login is not None:
            user, pwd = login
            auth = github.Auth.Login(user, pwd)
        else:
            auth = None

        self._conn_server = github.Github(auth)
        repo = getattr(args, f"{which}_location")
        self._repo = self._conn_server.get_repo(repo)
