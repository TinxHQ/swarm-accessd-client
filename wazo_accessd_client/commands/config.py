# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_accessd_client.command import AccessdCommand


class ConfigCommand(AccessdCommand):

    resource = 'config'
    _headers = {'Accept': 'application/json'}

    def get(self):
        r = self.session.get(self.base_url, headers=self._headers)
        self.raise_from_response(r)
        return r.json()
