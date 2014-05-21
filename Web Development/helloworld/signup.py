import webapp2
import cgi
import re

form="""
<html>
     <head>
       <title>Sign Up</title>
       <style type="text/css">
         .label {text-align: right}
         .error {color: red}
       </style>
   
     </head>
   
     <body>
     
       <h2>Signup</h2>
<form method="post">
        <table>
                <tr>
                        <td class="label">Username</td>
                <td><input type="text" name="username" value=""%(username)s"></input></td>
                <td class="error">%(error_username)s</td>
            </tr>
                <tr>
                        <td class="label">Password</td>
                <td><input type="password" name="password" value="%(password)s"></input></td>
                <td class="error">%(error_password)s</td>
            </tr>
                <tr>
                <td class="label">Verify Password</td>
                <td><input type="password" name="verify" value="%(verify)s"></input></td>
                <td class="error">%(error_verify)s</td>
            </tr>
            <tr>
                <td class="label">Email (optional)</td>
                <td><input type="text" name="email" value="%(email)s""></input></td>
                <td class="error">%(error_email)s</td>
            </tr>
        </table>
           
        <input type="submit" value="Submit">
</form>
</body>
</html>
"""
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
PASSWORD_RE = re.compile(r"^.{3,20}$")

def valid_user_name(user):
    return USER_RE.match(user)

def valid_email(email):
    if email == '':
        return True
    else:
        return EMAIL_RE.match(email)
        
def valid_password(password):
    return PASSWORD_RE.match(password)

def escape_html(s):
  return cgi.escape(s, quote=True)

errors = ["Invalid Username","Invalid Password","Passwords do not match","Invalid Email"]
    
class MainPage(webapp2.RequestHandler):
    def write_form(self, error_username="", error_password="", error_verify="", error_email="", username="", password="", verify="", email=""):
        self.response.out.write(form % {"error_username":error_username,
                                        "error_password":error_password,
                                        "error_verify":error_verify,
                                        "error_email":error_email,
                                        "username":escape_html(username),
                                        "password":escape_html(password),
                                        "verify":escape_html(verify),
                                        "email":escape_html(email)})
        
    def get(self):
        self.write_form()

    def post(self):
        user_username = self.request.get('username')
        user_password = self.request.get('password')
        user_verify = self.request.get('verify')
        user_email = self.request.get('email')

        username = valid_user_name(user_username)
        password = valid_password(user_password)
        verify = valid_password(user_verify)
        email = valid_email(user_email)

        if not(username):
            self.write_form(errors[0],"","","",user_username,user_password,user_verify,user_email)
        elif not password:
            self.write_form("",errors[1],"","",user_username,user_password,user_verify,user_email)
        elif user_password != user_verify:
            self.write_form("","",errors[2],"",user_username,user_password,user_verify,user_email)
        elif not email:
            self.write_form("","","",errors[3],user_username,user_password,user_verify,user_email)
            
        else:
            self.redirect('/welcome?username='+ user_username)  
            
      

class ThanksHandler(webapp2.RequestHandler):
  def get(self):
      username =  self.request.get('username')
      self.response.out.write("Thanks for signing up! Welcome to Awesomeland,%s!" % username)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/welcome', ThanksHandler)],debug=True)
                             
