#!/usr/bin/env python3
# Copyright 2018-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import find_packages, setup

setup(
    name='swarm_accessd_client',
    version='0.1',
    description='a simple client library for the swarm accessd HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.io',
    url='http://wazo.io',
    packages=find_packages(),
    entry_points={
        'swarm_accessd_client.commands': [
            'authorizations = swarm_accessd_client.commands.authorizations:AuthorizationsCommand',
            'config = swarm_accessd_client.commands.config:ConfigCommand',
            'status = swarm_accessd_client.commands.status:StatusCommand',
            'subscriptions = swarm_accessd_client.commands.subscriptions:SubscriptionsCommand',
        ],
    },
)
