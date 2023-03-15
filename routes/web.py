from engine.view import *

def routes(app):
    # RENDER EXAMPLE
    @app.GET('/')
    def Route():
        # return_code(500)
        return render('example_render', { # render(@file, @data) 
            "title": "Example Render",    # @file: Render file from "/src/..."
            "var_1": "Value 1"            # @data: { 'key': 'value' } 
        })

    # RETURN EXAMPLE
    @app.GET('/home')
    def Route():
        return "Home"

    # 404 DEFAULT PAGE
    @app.DEFAULT_404(404) # RESPONSE CODE
    def Route():
        return "Error 404"