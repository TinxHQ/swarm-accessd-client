# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class StatusCommand(BaseCommand):

    resource = 'status'

    def check(self):
        r = self.session.head(self.base_url, headers=self._ro_headers)
        self.raise_from_response(r)
