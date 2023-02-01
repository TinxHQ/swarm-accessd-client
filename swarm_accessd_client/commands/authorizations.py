# Copyright 2018-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class AuthorizationsCommand(BaseCommand):
    resource = 'authorizations'

    def _get_list_url(self, subscription_uuid=None):
        if subscription_uuid:
            base = self._client.url()
            return f'{base}/subscriptions/{subscription_uuid}/{self.resource}'
        return self.base_url

    def list(self, subscription_uuid=None, **params):
        headers = self._get_headers(**params)
        url = self._get_list_url(subscription_uuid=subscription_uuid)
        r = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()

    def create(self, authorization, subscription_uuid='', **kwargs):
        headers = self._get_headers(**kwargs)
        url = self._get_list_url(subscription_uuid=subscription_uuid)
        r = self.session.post(url, json=authorization, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, authorization_uuid, tenant_uuid=None):
        url = f'{self.base_url}/{authorization_uuid}'
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def update(
        self, authorization_uuid, update_args, subscription_uuid='', tenant_uuid=None
    ):
        if subscription_uuid:
            base = self._client.url()
            url = f'{base}/subscriptions/{subscription_uuid}/authorizations/{authorization_uuid}'
        else:
            url = f'{self.base_url}/{authorization_uuid}'
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.put(url, json=update_args, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, authorization_uuid, subscription_uuid=None, **kwargs):
        if subscription_uuid:
            base = self._client.url()
            url = f'{base}/subscriptions/{subscription_uuid}/authorizations/{authorization_uuid}'
        else:
            url = f'{self.base_url}/{authorization_uuid}'
        headers = self._get_headers(**kwargs)
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)

    def issue_token(self, authorization_uuids=[], **kwargs):
        url = f'{self.base_url}/token'
        headers = self._get_headers(**kwargs)
        json = {'authorization_uuids': authorization_uuids}
        r = self.session.post(url, json=json, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def issue_subscription_token(self, **kwargs):
        base = self._client.url()
        url = f'{base}/subscriptions/token'
        headers = self._get_headers(**kwargs)
        r = self.session.post(url, headers=headers)
        self.raise_from_response(r)
        if r.status_code == 204:
            return
        return r.json()

    def seats(self, **params):
        url = f'{self.base_url}/seats'
        headers = self._get_headers(**params)
        r = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()
