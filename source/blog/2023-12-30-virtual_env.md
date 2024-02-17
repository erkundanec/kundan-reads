# 2023-12-30
## Virtual env

Creating a virtual environment in a specific folder allows you to isolate the dependencies of a project from the system-wide Python installation. Here's a general guide on how to create a virtual environment in a folder:

### Using `venv` 
(built-in module in Python 3.3 and later):

1. **Navigate to the desired folder:**
    
    ```bash
    cd path/to/your/project/folder
    ```
    
2. **Create a virtual environment:**
    
    ```bash
    python -m venv venv
    ```
    
    This command will create a virtual environment named **`venv`** in the current directory.
    
3. **Activate the virtual environment:**
    - On Windows:
        
        ```bash
        .\venv\Scripts\activate
        ```
        
    - On Unix or MacOS:
    
        ```bash
        source venv/bin/activate
        ```
        
    
    After activation, your command prompt or terminal prompt should change to indicate that you are now working within the virtual environment.
    
4. **Install dependencies:**
Once the virtual environment is activated, you can use **`pip`** to install the required packages for your project:
    
    ```bash
    pip install package_name
    ```
    
5. **Deactivate the virtual environment:**
    
    ```bash
    deactivate
    ```
    
    This command will return you to the global Python environment.
    

### **Using `virtualenv`:**

If you are using an older version of Python or prefer to use **`virtualenv`**, you can follow these steps:

1. **Install `virtualenv` (if not already installed):**
    
    ```bash
    pip install virtualenv
    ```
    
2. **Navigate to the desired folder:**
    
    ```bash
    cd path/to/your/project/folder
    ```
    
3. **Create a virtual environment:**
    
    ```bash
    virtualenv venv
    ```
    
4. **Activate the virtual environment:**
    - On Windows:
        
        ```bash
        .\venv\Scripts\activate
        ```
        
    - On Unix or MacOS:
        
        ```bash
        source venv/bin/activate
        ```
        
5. **Install dependencies:**
Once the virtual environment is activated, you can use **`pip`** to install the required packages for your project:
    
    ```bash
    pip install package_name
    ```
    
6. **Deactivate the virtual environment:**
    
    ```bash
    deactivate
    ```
    
Choose the method that best suits your needs or the one you are more comfortable with. Virtual environments are an excellent practice to keep project dependencies isolated and manageable.