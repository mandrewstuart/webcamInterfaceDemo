from bottle import *

@get('/.well-known/pki-validation/0A4EF452B8F55C4CA1D53E7DE53FF315.txt')
def index():
  return(template('secret.csr'))


@get('/')
def index():
  return(template('index.html'))


@get('/images/<s>')
def index(s):
  return(static_file(s,'./images'))



run(host='0.0.0.0', port=81, server='paste')
