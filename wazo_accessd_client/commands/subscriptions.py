# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_accessd_client.command import AccessdCommand


class SubscriptionsCommand(AccessdCommand):

    resource = 'subscriptions'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def list(self, **params):
        headers = self._get_headers(**params)
        r = self.session.get(self.base_url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()

    def get(self, subscription_uuid, tenant_uuid=None, **params):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=subscription_uuid, **params)
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def create(self, subscription, **kwargs):
        return self._post(subscription, **kwargs)

    def amend(self, subscription, **kwargs):
        return self._post(subscription, **kwargs)

    def _post(self, subscription, **kwargs):
        headers = self._get_headers(write=True, **kwargs)
        r = self.session.post(self.base_url, json=subscription, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def _get_headers(self, write=False, **kwargs):
        headers = dict(self._rw_headers) if write else dict(self._ro_headers)
        tenant_uuid = kwargs.pop('tenant_uuid', self._client.tenant())
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        return headers
