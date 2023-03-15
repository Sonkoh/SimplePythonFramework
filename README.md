# SimplePythonFramework

SimplePythonFramework is a lightweight web framework for Python that aims to make it easy to build web applications quickly and efficiently. It is built on top of Python's built-in `http.server` module and provides a simple API for handling requests, routing URLs, and generating responses.

## Features

- Simple and easy to use API
- Built-in URL routing and view handling
- Support for static files and templates
- Lightweight and fast

## Getting Started

To get started with SimplePythonFramework, you can install it using pip:

pip install simple-python-framework

Once installed, you can create a new application by creating a Python file and importing the `SimplePythonFramework` class:

```python
from simple_python_framework import SimplePythonFramework

app = SimplePythonFramework()
```

You can then define your views and URL routes using the `@app.route` decorator:

```python
@app.route("/")
def index(request):
    return "Hello, world!"
```
    
Finally, you can run your application using the run method:

```pythonif __name__ == "__main__":
    app.run()
```

## Contributing
If you would like to contribute to SimplePythonFramework, please feel free to submit a pull request or open an issue. We welcome contributions of all kinds, including bug fixes, new features, documentation improvements, and more.

## License
SimplePythonFramework is released under the MIT License. See the LICENSE file for more information.
