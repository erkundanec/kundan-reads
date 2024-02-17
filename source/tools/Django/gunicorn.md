# Gunicorn
## Use "gunicorn apipy.wsgi:application" instead of "manage.py runserver"
sidebar_position: 1
---

Yes, you can use Gunicorn to serve your Django application instead of the built-in development server (`manage.py runserver`). Gunicorn (Green Unicorn) is a popular production-ready WSGI server for running Python web applications.

To use Gunicorn, follow these steps:

1. **Install Gunicorn:**
   ```bash
   pip install gunicorn
   ```

2. **Navigate to your Django project directory:**
   ```bash
   cd /path/to/your/django/project
   ```

3. **Run Gunicorn:**
   ```bash
   gunicorn apipy.wsgi:application
   ```

   - `apipy.wsgi:application` refers to the WSGI application object in your `wsgi.py` file.

4. **Specify the number of workers (optional):**
   You can use the `-w` option to specify the number of worker processes. For example, to run 4 worker processes:
   ```bash
   gunicorn -w 4 apipy.wsgi:application
   ```

   Adjust the number of workers based on your server's resources and the expected traffic to your application.

5. **Specify the host and port (optional):**
   If you want Gunicorn to listen on a specific host and port, you can use the `-b` option. For example, to listen on `127.0.0.1:8000`:
   ```bash
   gunicorn -b 127.0.0.1:8000 apipy.wsgi:application
   ```

   If not specified, Gunicorn will default to `127.0.0.1:8000`.

6. **Verify:**
   Visit your Django application in a web browser or use a tool like `curl` to verify that it's working with Gunicorn.

Using Gunicorn is a common practice for deploying Django applications in production. It provides better performance and reliability compared to the development server. Additionally, you might use Gunicorn in conjunction with a reverse proxy like Nginx or Apache for better security and additional features.