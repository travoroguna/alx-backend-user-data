from typing import List, TypeVar

from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if the request is authenticated or not
        """
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
