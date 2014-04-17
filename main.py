import os
import jinja2
import webapp2

SERVER_SOFTWARE = os.environ.get('SERVER_SOFTWARE')
DEBUG = True if SERVER_SOFTWARE.startswith('Development') else False

TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), 'templates')
JINJA = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_PATH))

def render(filename, values={}):
    return JINJA.get_template(filename).render(values)

class Main(webapp2.RequestHandler):
    def get(self):
        self.response.write(render('index.html'))

app = webapp2.WSGIApplication([
    ('/', Main),
], debug=DEBUG)

