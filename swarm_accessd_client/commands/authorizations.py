# Copyright 2018-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class AuthorizationsCommand(BaseCommand):

    resource = 'authorizations'

    def _get_list_url(self, subscription_uuid=None):
        if subscription_uuid:
            return '{base}/subscriptions/{subscription_uuid}/{resource}'.format(
                base=self._client.url(),
                subscription_uuid=subscription_uuid,
                resource=self.resource,
            )
        return self.base_url

    def list(self, subscription_uuid=None, **params):
        headers = self._get_headers(**params)
        url = self._get_list_url(subscription_uuid=subscription_uuid)
        r = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()

    def create(self, authorization, subscription_uuid='', **kwargs):
        headers = self._get_headers(write=True, **kwargs)
        url = self._get_list_url(subscription_uuid=subscription_uuid)
        r = self.session.post(url, json=authorization, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, authorization_uuid, tenant_uuid=None, **params):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=authorization_uuid)
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
            url = '{base}/{uuid}'.format(base=self.base_url, uuid=authorization_uuid)
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.put(url, json=update_args, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, authorization_uuid, subscription_uuid=None, **kwargs):
        if subscription_uuid:
            base = self._client.url()
            url = f'{base}/subscriptions/{subscription_uuid}/authorizations/{authorization_uuid}'
        else:
            url = '{base}/{uuid}'.format(base=self.base_url, uuid=authorization_uuid)
        headers = self._get_headers(**kwargs)
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)

    def issue_token(self, authorization_uuids=[], **kwargs):
        url = '{base}/token'.format(base=self.base_url)
        headers = self._get_headers(write=True, **kwargs)
        json = {'authorization_uuids': authorization_uuids}
        r = self.session.post(url, json=json, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def issue_subscription_token(self, **kwargs):
        url = '{base}/subscriptions/token'.format(base=self._client.url())
        headers = self._get_headers(write=False, **kwargs)
        r = self.session.post(url, headers=headers)
        self.raise_from_response(r)
        if r.status_code == 204:
            return
        return r.json()

    def seats(self, **params):
        url = '{base}/seats'.format(base=self.base_url)
        headers = self._get_headers(write=False, **params)
        r = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()
