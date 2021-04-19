#!/usr/bin/env python

#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("""
            <!DOCTYPE html>
<html lang="en">
<head>
    <script  src="/templates/validator.js"></script>
    <meta charset="UTF-8">
    <title>ECO</title>
</head>
<body>

<form id="frmConsumo" action="/do" method="POST">
    <label for="edkm">Introduzca los kilometros</label>
    <input type="text" id="edkm" name="edkm"/>
    
    <label for="edtiempo">Introduzca el tiempo</label>
    <input type="text" id="edtiempo" name="edtiempo"/>
    
    
    <label for="edconsumo">Introduzca el consumo</label>
    <input type="text" id="edconsumo" name="edconsumo"/>
    
    <input type="submit" value="To Consumo">

</form>


</body>
</html>

            """)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
