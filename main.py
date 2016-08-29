import webapp2
from caesar import encrypt

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px Arial;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">%(text)s</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>
"""

class Index(webapp2.RequestHandler):
    def get(self):
        response = (form % {"text":""})
        self.response.write(response)

    def post(self):
        text = self.request.get('text')
        rot = self.request.get('rot')
        rot = int(rot)
        rot13 = encrypt(text, rot)
        response = (form % {"text": rot13})
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
