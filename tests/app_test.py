from nose.tools import *
from app import app     # Importing the whole application from the app.py module.
  
app.config['TESTING'] = True
web = app.test_client()   

# flask framework API for processing requests

def test_index():

    # Send a GET request using the get() method.
    rv = web.get('/', follow_redirects=True)
    # see if '/' URL returns "404 Not Found, since it actually doesn't exist." 
    assert_equal(rv.status_code, 404)
    
    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200) # 200 '/hello' page exists
    assert_in(b"Fill Out This Form", rv.data)
    
    data = {'name': 'Ady', 'greet': 'Hola'}
    
    # Send a POST request using the post() method, and then give it the form data as a dict. 
    rv = web.post('/hello', follow_redirects=True, data=data) 
    
    
    assert_in(b"Ady", rv.data)
    assert_in(b"Hola", rv.data)
   
   
   
