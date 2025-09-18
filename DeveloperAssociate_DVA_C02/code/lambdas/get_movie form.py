
form="""
   <html>
   <body>
      <form action="../movies" method="POST">
         <p> Id: <input type="text" name="id"> </p>
         <p> Title: <input type="text" name="title"> </p>

      </form>
   </body>
   </html>
"""

def handler(event, context):
   return {
      "statusCode": 200,
      "body" : form,
      "headers": {
            "Content-Type": "text/html"
      }
   }
