from engine.view import *

def routes(app):
    # RENDER EXAMPLE
    @app.GET('/')
    def Route(data):
        return render('example_render', { # render(@file, @data) 
            "title": "Example Render",    # @file: Render file from "/src/..."
            "var_1": "Value 1",           # @data: { 'key': 'value' },
            "data": data                  # Send data from url to render file
        })

    # RETURN EXAMPLE
    @app.GET('/home')
    def Route(data):
        return "Home"

    # 404 DEFAULT PAGE
    @app.DEFAULT_404(404) # RESPONSE CODE
    def Route(data):
        return "Error 404"