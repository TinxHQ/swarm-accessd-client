# Copyright 2018-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class SubscriptionsCommand(BaseCommand):

    resource = 'subscriptions'

    def list(self, **params):
        headers = self._get_headers(**params)
        r = self.session.get(self.base_url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()

    def create(self, subscription, **kwargs):
        headers = self._get_headers(**kwargs)
        r = self.session.post(self.base_url, json=subscription, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, subscription_uuid, tenant_uuid=None):
        url = f'{self.base_url}/{subscription_uuid}'
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def update(self, subscription_uuid, update_args={}, tenant_uuid=None):
        url = f'{self.base_url}/{subscription_uuid}'
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.put(url, json=update_args, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, subscription_uuid, tenant_uuid=None):
        url = f'{self.base_url}/{subscription_uuid}'
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)

    def get_default(self, tenant_uuid=None):
        url = f'{self.base_url}/default'
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()
