from openerp import http

class HelloWorld(http.Controller):
    @http.route('/helloworld',auth='public')
    def hello_world(self):
        return('<h1>Hello World</h1>')
