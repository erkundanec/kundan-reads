# CSS Missing in Admin
## CSS Missing in Admin


If the CSS is missing when you access the Django admin interface, it may be due to incorrect static files configuration or the development server not serving static files properly. Here are some steps you can take to troubleshoot and fix the issue:

1. **Collect Static Files:**

   Ensure that you have collected static files. Run the following command to gather all static files into the `static` directory:

   ```bash
   python manage.py collectstatic
   ```

   This command copies the static files from your apps and third-party packages into the `STATIC_ROOT` directory specified in your Django settings.

2. **Static Files Configuration:**

   Make sure your Django settings are correctly configured for static files. In your `settings.py`, check the following:

   ```python
   # settings.py

   # Static files (CSS, JavaScript, images)
   STATIC_URL = '/static/'
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   ```

   Ensure that `STATIC_URL` is set to '/static/' and `STATIC_ROOT` points to the directory where the `collectstatic` command collects static files.

3. **Static Files in Development:**

   If you are in development mode, make sure you are running the development server with the `--insecure` option to serve static files:

   ```bash
   python manage.py runserver --insecure
   ```

   The `--insecure` option serves static files even if the `DEBUG` setting is set to `False`.

4. **Check URLs in Browser:**

   Inspect the page source or use your browser's developer tools to check the URLs of the missing CSS files. Ensure that the URLs are correct and point to the static files.

5. **Check Browser Console:**

   Open your browser's console and check for any error messages related to failed requests for CSS files. This can provide insights into what might be going wrong.

6. **Permissions:**

   Ensure that the static files and directories have the correct permissions for the web server to access them.

After checking and adjusting these settings, try accessing the Django admin interface again. If the issue persists, review the console output and error messages for more specific information about the problem.

The error you're encountering is due to the same-origin policy, which prevents web pages from making requests to a different domain than the one that served the web page. This is enforced by web browsers to enhance security.

In your case, you are trying to make a request from 'http://127.0.0.1:5500' to 'http://127.0.0.1:8000', and the server at 'http://127.0.0.1:8000' does not include the necessary CORS headers to allow requests from 'http://127.0.0.1:5500'.

To resolve this issue, you can do the following:

1. **Install Django CORS Headers:**
   - Install the `django-cors-headers` package using pip:

     ```bash
     pip install django-cors-headers
     ```

2. **Configure Django Settings:**
   - Add `'corsheaders'` to your `INSTALLED_APPS` in your Django project's `settings.py`:

     ```python
     # settings.py

     INSTALLED_APPS = [
         # ... other apps ...
         'corsheaders',
     ]
     ```

   - Add `'corsheaders.middleware.CorsMiddleware'` to your `MIDDLEWARE`:

     ```python
     # settings.py

     MIDDLEWARE = [
         # ... other middleware ...
         'corsheaders.middleware.CorsMiddleware',
         # ... other middleware ...
     ]
     ```

   - Add the following setting to allow all origins (you can adjust it based on your needs):

     ```python
     # settings.py

     CORS_ALLOWED_ORIGINS = [
         "http://127.0.0.1:5500",
         # Add other allowed origins as needed
     ]
     ```

3. **Restart Django Development Server:**
   - Restart your Django development server for the changes to take effect.

Now, with `django-cors-headers` installed and configured, your Django server will include the necessary CORS headers in the response, allowing requests from 'http://127.0.0.1:5500' to access resources on 'http://127.0.0.1:8000'.

https://pypi.org/project/django-cors-headers/