# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from .helpers.base import BaseCommand


class AuthorizationsCommand(BaseCommand):

    resource = 'authorizations'

    def create(self, authorization, **kwargs):
        headers = self._get_headers(write=True, **kwargs)
        r = self.session.post(self.base_url, json=authorization, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def issue_token(self, authorizations_uuids, **kwargs):
        url = '{base}/token'.format(base=self.base_url)
        headers = self._get_headers(write=True, **kwargs)
        r = self.session.post(url, json=authorizations_uuids, headers=headers)
        self.raise_from_response(r)
        return r.json()
