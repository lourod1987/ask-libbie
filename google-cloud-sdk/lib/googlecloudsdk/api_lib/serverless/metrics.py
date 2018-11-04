# -*- coding: utf-8 -*- #
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Serverless CSI metric names and metric collection methods."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import contextlib
from googlecloudsdk.core import metrics


# Metric names for client side instruments(CSI).

# Reserved CSI metric prefix for serverless
_SERVERLESS_PREFIX = 'serverless_'

# "Start" suffix
START = '_start'

# Time to list services
LIST_SERVICES = _SERVERLESS_PREFIX + 'list_services'

# Time to list revisions
LIST_REVISIONS = _SERVERLESS_PREFIX + 'list_revisions'

# Time to list services
LIST_CONFIGURATIONS = _SERVERLESS_PREFIX + 'list_configurations'

# Time to get a revision
GET_REVISION = _SERVERLESS_PREFIX + 'get_revision'

# Time to delete a revision
DELETE_REVISION = _SERVERLESS_PREFIX + 'delete_revision'

# Time to get a route
GET_ROUTE = _SERVERLESS_PREFIX + 'get_route'

# Time to get a service
GET_SERVICE = _SERVERLESS_PREFIX + 'get_service'

# Time to delete a service
DELETE_SERVICE = _SERVERLESS_PREFIX + 'delete_service'

# Time to create a route
CREATE_ROUTE = _SERVERLESS_PREFIX + 'create_route'

# Time to get a configuration
GET_CONFIGURATION = _SERVERLESS_PREFIX + 'get_configuration'

# Time to create a configuration
CREATE_CONFIGURATION = _SERVERLESS_PREFIX + 'create_configuration'

# Time to update a configuration
UPDATE_CONFIGURATION = _SERVERLESS_PREFIX + 'update_configuration'

# Time to create a service
CREATE_SERVICE = _SERVERLESS_PREFIX + 'create_service'

# Time to update a service
UPDATE_SERVICE = _SERVERLESS_PREFIX + 'update_service'


@contextlib.contextmanager
def record_duration(method_name):
  """Record duration of a serverless API method call.

  Two timestamps will be sent, and the duration in between will be considered as
  the client side latency of this method call.

  Args:
    method_name: str, The name of the method to time.

  Yields:
    None
  """
  metrics.CustomTimedEvent(method_name + START)
  yield
  metrics.CustomTimedEvent(method_name)
