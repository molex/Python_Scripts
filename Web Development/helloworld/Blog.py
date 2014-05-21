import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)


class MainPage(Handler):
    def render_front(self, subject="", content="", error=""):
        posts = db.GqlQuery("Select * from Post order by created DESC")
        self.render("front.html", subject=subject, content=content, error = error, posts = posts)

    def get(self):
        self.render_front()


class NewPost(Handler):
    def render_front(self, subject="", content="", error=""):
        posts = db.GqlQuery("Select * from Post order by created DESC")
        self.render("newpost.html", subject=subject, content=content, error = error, posts = posts)

    def get(self):
        self.render_front()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        if subject and content:
            p = Post(subject = subject, content = content)
            p.put()
            last_id = str(p.key().id())
            self.redirect("/blog/post/" + last_id)
        else:
            error = "we need both a subject and some content!" 
            self.render_front(subject,content,error)

class show_single_post(Handler):
    
    def get(self, post_id):
        blog_entry = Post.get_by_id(int(post_id))
        if blog_entry:
            self.render("post.html", blog_entry=blog_entry)
        else:
            self.render("post.html",error="Blog post %s not found!" %post_id)


app = webapp2.WSGIApplication([('/blog', MainPage), 
                              ('/blog/newpost', NewPost),
                              ('/blog/post/(\d+)', show_single_post)],
                              debug=True)
