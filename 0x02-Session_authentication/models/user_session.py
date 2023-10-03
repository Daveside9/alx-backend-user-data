#!/usr/bin/env python3
""" User_session_module
"""
from models.base import Base


class UserSession(Base):
    """User_Session_Class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """Constructor_Method"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')