# swarm-accessd-client

A python client library to access swarm-accessd

## Usage

### Creating a client

```python
from swarm_accessd_client import Client
client = Client('<accessd hostname>', token='<auth token>')
```

## Config

### Fetching the server config

```python
client.config.get()
```

## Status

```python
client.status.check()
```

## Subscriptions

### Listing subscriptions

Possible parameters are : `recurse`, `from`, `until`, `contract_date`, `status`, `term`, `auto_renew`, `product_sku`

```python
client.subscriptions.list(recurse=True)
```

### Add a new subscription

```python
subscription = {
    'name': 'Some name',
    'start_date': datetime.date.today().isoformat(),
    'contract_date': datetime.date.today().isoformat(),
    'term': 3,
    'product_sku': 'a-sku',
}
client.subscriptions.create(subscription)
```

### Get a subscription

```python
client.subscriptions.get(subscription_uuid)
```

### Update a subscription

```python
update_args = {
    'name': 'New name',
    'start_date': datetime.date.today().isoformat(),
    'contract_date': datetime.date.today().isoformat(),
    'term': 6,
    'product_sku': 'another-sku',
}
client.subscriptions.update(subscription_uuid, update_args)
```

### Delete a subscription

```python
client.subscriptions.delete(subscription_uuid)
```

## Authorizations

### Listing authorizations

Possible parameters are : `from`, `until`, `status`, `term`, `auto_renew`, `service_remote_uuid`

#### Main authorizations

Main authorizations are filtered by subscriptions

```python
client.authorizations.list(subscription_uuid=subscription_uuid)
```

#### Sub-authorizations

```python
client.authorizations.list()
```

### Add a new authorization

#### Main authorization

```python
authorization = {
    'start_date': datetime.date.today().isoformat(),
    'term': 3,
    'rules': [
        {'name': rule_name, 'options': rule_options}
    ],
}
client.authorizations.create(authorization, subscription_uuid=subscription_uuid)
```

#### Sub-authorization

```python
authorization = {
    'start_date': datetime.date.today().isoformat(),
    'term': 3,
    'rules': [
        {'name': rule_name, 'options': rule_options}
    ],
    "service": {
        'remote_uuid': instance_uuid,
        'ip_address': instance_ip,
        'mac_address':instance_mac_address,
        'service_id': 1
    }
}
client.authorizations.create(authorization)
```

### Get an authorization

```python
client.authorizations.get(authorization_uuid)
```

### Delete an authorization

#### Main authorization

```python
client.authorizations.delete(authorization_uuid, subscription_uuid=subscription_uuid)
```

#### Sub authorization

```python
client.authorizations.delete(authorization_uuid)
```

### Issue a token

#### For given authorizations

```python
client.subscriptions.issue_token([authorization_uuid_1, authorization_uuid_2])
```

#### For all authorizations of all subscriptions

```python
client.subscriptions.issue_subscription_token()
```

## Debian package

Follow the following steps to build a debian package for swarm-accessd-client manually.

1. Copy the source directory to a machine with all dependencies installed

```sh
rsync -av . <builder-host>:~/swarm-accessd-client
```

2. On the host, increment the changelog

```sh
dch -i
```

3. Build the package

```sh
dpkg-buildpackage -us -uc
```
