# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client.client import BaseClient


class AccessdClient(BaseClient):

    namespace = 'wazo_accessd_client.commands'

    def __init__(self, host, port=9486, version='1.0', **kwargs):
        super(AccessdClient, self).__init__(host=host, port=port, version=version, **kwargs)
