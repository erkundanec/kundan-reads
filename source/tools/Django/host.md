# Allowed hosts
## Use Allowed hosts


The `ALLOWED_HOSTS` setting in Django is used to specify a list of valid host/domain names that can be used to serve the Django application. This setting is a security measure to prevent HTTP Host header attacks. You should add the host/domain names that you expect your Django application to be accessed from.

If you are running your Django application locally for development, you can use the following settings:

```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your-machine-name', '*']
```

- `'localhost'`: Allows access from localhost.
- `'127.0.0.1'`: Allows access from the loopback IP address.
- `'your-machine-name'`: If you access the Django application using your machine's name (e.g., `http://your-machine-name:8000/`), add it to the list.

If you are using a specific port (e.g., `8000`), make sure to include it in the URLs.

In your case, if you are running your Django application on `http://127.0.0.1:5500/`, you should set `ALLOWED_HOSTS` as follows:

```python
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'http://127.0.0.1:5500/', '*']
```

Note that it's generally not necessary to include the protocol (`http://`) in the `ALLOWED_HOSTS` entries.

Remember to update the `ALLOWED_HOSTS` setting based on your specific deployment environment when you deploy your Django application to a production server. In a production environment, you should specify the actual domain names or IP addresses that your application will be accessed from. For example:

```python
ALLOWED_HOSTS = ['yourdomain.com', 'subdomain.yourdomain.com', '192.168.1.100']
```

Always avoid using the wildcard `'*'` in a production setting unless absolutely necessary, as it can pose a security risk.