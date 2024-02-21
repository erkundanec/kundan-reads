# Publish a Pypi Package

## Publish a Pypi Package
Creating your own Python package enables you to effortlessly share your code with others and simplify its installation process. In this guide, we'll lead you through the steps of crafting, distributing, and releasing a simple Python package.

## Setting Up
To set up your Python environment for publishing your own package, you will need to install setuptools, wheel, and twine.

You can install these tools using pip:

```
pip install setuptools wheel twine
```

Next, you will need to create the project structure for your package. Here is an example structure:

FinFinance/
├── FinFinance/
│   ├── __init__.py
│   └── main.py
├── setup.py
└── README.md

In the project directory, create a file called main.py with the following content:

```
# main.py
def hello():
    print("Hello from Pixegami!")

```

In the same directory, create a file called `__init__.py` with the following content:

```
# __init__.py
from .main import hello
```

The `__init__.py` file in a Python package serves two main roles: it tells Python that the directory should be treated as a package, and it controls what's made available when that package is imported.

By importing the hello function into `__init__.py`, you're allowing users to directly access the function from the package without needing to specify the underlying module.

This provides a cleaner and more straightforward way for users to interact with your package, as they can simply use from pixegami_hello import hello instead of navigating through deeper module structures.

```
from FinRecipes import hello
```

### Configure Setup.py
To write the setup.py file, you will need to include information about your package such as its name, version, and dependencies. Here is an example of how to structure your setup.py file:

```
from setuptools import setup, find_packages

setup(
    name='pixegami-hello',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add dependencies here.
        # e.g. 'numpy>=1.11.1'
    ],
)
```

In this example, replace 'your-package-name' with the actual name of your package. The version field should be set to the desired version number of your package.

Additionally, you can specify any dependencies your package requires in the install_requires list. For example, if your package requires NumPy version 1.11.1 or higher, you can add 'numpy>=1.11.1' to the list.

It is also recommended to create a README.md file where you can describe your package. This file should be written in Markdown format and can provide information about the purpose of your package, how to install it, and any other relevant details.

### Build Your Package
To build your package, you will need to use the setuptools and wheel libraries. These libraries allow you to generate distribution archives that can be installed using pip. You have already installed these from the first step of this tutorial.

You can build your package by running the following command:
```
python setup.py sdist bdist_wheel
```

This command will generate two distribution archives: a source distribution (sdist) and a wheel distribution (bdist_wheel). These archives contain all the necessary files for installing your package.

### Local Testing
Before publishing your Python package, it's crucial to test it locally to ensure it functions correctly. Follow these steps to install and test your package using pip:

1. Open your terminal or command prompt.
2. Navigate to the directory where your package is located.
3. Run the following command to install your package locally.

```
pip install dist/FinRecipes-0.1-py3-none-any.whl
```
Replace the package name with the actual name and version of your package. Once the installation is complete, you can now test your package by importing it in a Python script or interactive session and using its functionality.

```
# In a different file...
from FinRecipes import hello

hello() # Hello from FinRecipes!

```

By testing your package locally, you can identify and fix any issues before publishing it to PyPI.


### Add a CLI Command
If you want to turn this package into a command line interface (or CLI application), you can also do that.

In the setup.py file, you can specify entry points for your package, which lets you a command name to any function inside your package. And running that command will run that function.

```
setup(
    ...
    entry_points={
        "console_scripts": [
            "pixegami-hello = pixegami_hello:hello",
        ],
    },
)
```

### Publish to PyPI
To publish your Python package to PyPI, you can use the twine tool.

```
twine upload dist/*
```

You will be prompted for your PyPI credentials. Once uploaded, anyone can install your package using.

```
pip install FinRecipes
```

