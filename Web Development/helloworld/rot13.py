import webapp2
import cgi


form="""

 <h2> Enter some text to ROT13</h2>
  <br>
<form method="post">
<textarea name="text" style="height: 100px; width: 400px;">%(text)s</textarea>
<br>
<input type="submit"name=submit>
</form>
"""

def escape_html(s):
  return cgi.escape(s, quote=True)

def encrypt(s):
    return s.encode("rot13")

class MainPage(webapp2.RequestHandler):
  def write_form(self,text=""):
      self.response.out.write(form % {"text": text})
    
  def get(self):
      self.write_form()

  def post(self):
    user_text = self.request.get("text")
    text = encrypt(user_text)
    self.write_form(text)
    
    
app = webapp2.WSGIApplication([('/', MainPage)],debug=True)
