# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

"""
oauthlib.oauth2
~~~~~~~~~~~~~~

This module is a wrapper for the most recent implementation of OAuth 2.0 Client
and Server classes.
"""

from .draft25 import Client, Server
from .draft25 import AuthorizationEndpoint, TokenEndpoint, ResourceEndpoint
from .draft25 import WebApplicationServer, MobileApplicationServer
from .draft25 import LegacyApplicationServer, BackendApplicationServer
from .draft25.grant_types import RequestValidator
