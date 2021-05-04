# Copyright 2018-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from requests import HTTPError


class AccessdError(HTTPError):
    def __init__(self, response):
        try:
            body = response.json()
        except ValueError:
            raise InvalidAccessdError()

        self.status_code = response.status_code
        try:
            self.message = body['message']
            self.error_id = body['error_id']
            self.details = body['details']
            self.timestamp = body['timestamp']
            if body.get('resource', None):
                self.resource = body['resource']
        except KeyError:
            raise InvalidAccessdError()

        exception_message = '{e.message}: {e.details}'.format(e=self)
        super(AccessdError, self).__init__(exception_message, response=response)


class AccessdServiceUnavailable(AccessdError):
    pass


class InvalidAccessdError(Exception):
    pass
