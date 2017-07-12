from bottle import route, run

@route('/hello')
def hello():
    return "<h1>Hello World!</h1>"

@route('/healthcheck')
def healthcheck():
    return "what could possibly go wrong?"

run(host='0.0.0.0', port=2112, debug=True)


