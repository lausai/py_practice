import os
import web

class index:
    def GET(self):
        return render.index()

class redirect:
    def GET(self, path):
        print("redirect")
        web.seeother("/" + path)

if __name__ == "__main__":
    template_dir = "templates/bootstrap-3.3.6/docs/examples/theme"
#    os.chdir(template_dir)
#    template_dir = "templates/"
    render = web.template.render(template_dir)
   
    urls = ("/", "index")
#    urls = ("/.*", "index",
#            "/(.*)/", "redirect")

    app = web.application(urls, globals())
    app.run()
