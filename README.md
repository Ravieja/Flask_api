# Flask_api
An API built using flask which has GET, POST, DELETE methods

Once you run the python file Flask_api.py, you will get a local host address running on port 5000,
something that looks like - http://127.0.0.1:5000 .  You can configure it to run on any port you want

Then we can use an API platform to send and recieve requests, I used postman.

You can use the get,post,delete methods using the below url's.
1.For get data - http://127.0.0.1:5000/data
2.For post data - http://127.0.0.1:5000/add with a 
          json payload (you have to give this data in body in postman):
          {
              "id":76675,
              "name":"ravi"
          }
3.For delete data - http://127.0.0.1:5000/del/<id>  . Example - http://127.0.0.1:5000/del/76675
