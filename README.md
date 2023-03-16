# SimplePythonFramework

SimplePythonFramework is a lightweight web framework for Python that aims to make it easy to build web applications quickly and efficiently. It is built on top of Python's built-in `http.server` module and provides a simple API for handling requests, routing URLs, and generating responses.

## Features

- Simple and easy to use API
- Built-in URL routing and view handling
- Support for static files and templates
- Lightweight and fast

## Getting Started

To get started with SimplePythonFramework, you can clone the repository with:

```bat
git clone https://github.com/Sonkoh/SimplePythonFramework
```

Once installed, you can start up the server with:

```python
python3 main.py
```

You can then define your views and URL routes using the `@app.route` decorator in any file in `routes` folder:

```python
@app.route("/")
def Route(data):
    return "Hello, world!"
```
    
Too, you can use the public folder to files without python scripts.
You can render html's that found in the `src` directory and send data to it:

```python
@app.GET('/')
def Route(data):
    # return_code(500)
    return render('example_render', { # render(@file, @data) 
        "title": "Example Render",    # @file: Render file from "/src/..."
        "var_1": "Value 1"            # @data: { 'key': 'value' } 
    })
```

And you can declare 404 function:

```python
@app.DEFAULT_404(404) # RESPONSE CODE
def Route(data):
    return "Error 404"
```

Finaly, you can modify all source code, that is located in `engine/server.py` and in `engine/main.py`

## Contributing
If you would like to contribute to SimplePythonFramework, please feel free to submit a pull request or open an issue. We welcome contributions of all kinds, including bug fixes, new features, documentation improvements, and more.

## License
SimplePythonFramework is released under the MIT License. See the LICENSE file for more information.
