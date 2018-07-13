# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client.command import RESTCommand

from .exceptions import (
    AccessdError,
    AccessdServiceUnavailable,
    InvalidAccessdError,
)


class AccessdCommand(RESTCommand):

    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise AccessdServiceUnavailable(response)

        try:
            raise AccessdError(response)
        except InvalidAccessdError:
            RESTCommand.raise_from_response(response)
