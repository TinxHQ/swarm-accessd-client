# wazo-accessd-client

A python client library to access wazo-accessd

## Usage

### Creating a client

```python
from wazo_accessd_client import Client
client = Client('<accessd hostname>', token='<auth token>')
```

## Config

### Fetching the server config

```python
client.config.get()
```

## Subscriptions

### Listing subscriptions

Possible parameters are : `recurse`, `start_date`, `contract_date`, `status`, `term`, `auto_renew`, `product_sku`

```python
client.subscriptions.list(recurse=True)
```

### Add a new subscription

```python
subscription = {
    'name': 'Some name',
    'start_date': datetime.date.today(),
    'contract_date': datetime.date.today(),
    'term': 3,
    'product_sku': 'a-sku',
}
client.subscriptions.create(subscription)
```

### Get a subscription

```python
client.subscriptions.get(subscription_uuid)
```

### Amend a subscription

Add the uuid of the subscription you want to amend in your subscription data

```python
amend_subscription = {
    'uuid': subscription_uuid,
    'name': 'New name',
    'start_date': datetime.date.today(),
    'contract_date': datetime.date.today(),
    'term': 6,
    'product_sku': 'another-sku',
}
client.subscriptions.amend(amend_subscription)
```

## Debian package

Follow the following steps to build a debian package for wazo-accessd-client manually.

1. Copy the source directory to a machine with all dependencies installed

```sh
rsync -av . <builder-host>:~/wazo-accessd-client
```

2. On the host, increment the changelog

```sh
dch -i
```

3. Build the package

```sh
dpkg-buildpackage -us -uc
```
