#!/usr/bin/env python3
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup
from setuptools import find_packages


setup(
    name='wazo_accessd_client',
    version='0.1',
    description='a simple client library for the wazo accessd HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.io',
    url='http://wazo.io',
    packages=find_packages(),
    entry_points={
        'wazo_accessd_client.commands': [
            'config = wazo_accessd_client.commands.config:ConfigCommand',
            'subscriptions = wazo_accessd_client.commands.subscriptions:SubscriptionsCommand',
            'authorizations = wazo_accessd_client.commands.authorizations:AuthorizationsCommand',
        ],
    }
)
