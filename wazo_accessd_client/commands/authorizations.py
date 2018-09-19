# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from .helpers.base import BaseCommand


class AuthorizationsCommand(BaseCommand):

    resource = 'authorizations'

    def list(self, **params):
        headers = self._get_headers(**params)
        r = self.session.get(self.base_url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()

    def create(self, authorization, subscription_uuid=None, **kwargs):
        headers = self._get_headers(write=True, **kwargs)
        if subscription_uuid:
            url = '{base}/subscriptions/{subscription_uuid}/{resource}'.format(
                base=self._client.url(),
                subscription_uuid=subscription_uuid,
                resource=self.resource,
            )
        else:
            url = self.base_url
        r = self.session.post(url, json=authorization, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, authorization_uuid, tenant_uuid=None, **params):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=authorization_uuid)
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def revoke(self, authorization_uuid, body, **kwargs):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=authorization_uuid)
        headers = self._get_headers(write=True, **kwargs)
        r = self.session.put(url, json=body, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def issue_token(self, authorizations_uuids, **kwargs):
        url = '{base}/token'.format(base=self.base_url)
        headers = self._get_headers(write=True, **kwargs)
        r = self.session.post(url, json=authorizations_uuids, headers=headers)
        self.raise_from_response(r)
        return r.json()
