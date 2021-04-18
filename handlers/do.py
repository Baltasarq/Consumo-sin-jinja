import webapp2

class DoHandler(webapp2.RequestHandler):
    def post(self):
        kilometros = int(self.request.get("edkm", "ERROR"))
        tiempo = int(self.request.get("edtiempo", "ERROR"))
        consumo = int(self.request.get("edconsumo", "ERROR"))

        self.response.write("La velocidad media es "+ str(kilometros/tiempo)+ " y el consumo total es "+ str(consumo*tiempo))

app = webapp2.WSGIApplication([
    ('/do', DoHandler)
], debug=True)