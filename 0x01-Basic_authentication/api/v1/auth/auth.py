#!/usr/bin/env python3
""" Autheication module
"""

from typing import List, Optional, TypeVar

from flask import request


class Auth:
    """
    authorization class
    """

    def norm_path(self, path: str) -> Optional[str]:
        """
        Normalize the path
        """
        if path is None:
            return None

        if not path.endswith("/"):
            path += "/"

        return path

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if the request is authenticated or not
        """
        if path is None or excluded_paths in [None, []]:
            return True

        path = self.norm_path(path)

        if path not in [self.norm_path(x) for x in excluded_paths]:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """
        Get the authorization header from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Get the current user from the request
        """
        return None
