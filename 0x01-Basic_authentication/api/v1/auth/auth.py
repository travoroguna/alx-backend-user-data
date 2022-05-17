#!/usr/bin/env python3
""" Autheication module
"""

from typing import List, TypeVar

from flask import request


class Auth:
    """
    authorization class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if the request is authenticated or not
        """
        if path is None or excluded_paths in [None, []]:
            return True

        if not path.endswith("/"):
            path += "/"

        if path not in [
            (lambda x: x if x.endswith("/") else f"{x}/")(x) for x in excluded_paths
        ]:
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
