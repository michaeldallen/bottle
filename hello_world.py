from bottle import route, run


import apt
import apt.progress.text

import socket


@route('/hello')
def hello():
    return "<h1>Hello World!</h1>"

@route('/dist-upgrade')
def hello():

    # First of all, open the cache
    cache = apt.Cache()
    # Now, lets update the package list
    cache.update()
    # We need to re-open the cache because it needs to read the package list
    cache.open(None)
    # Now we can do the same as 'apt-get upgrade' does
    ## cache.upgrade()
    # or we can play 'apt-get dist-upgrade'
    cache.upgrade(True)
    # Q: Why does nothing happen?
    # A: You forgot to call commit()!
    ## cache.commit(apt.progress.TextFetchProgress(), apt.progress.InstallProgress())
    cache.commit()


    return "<h1>dist-upgrade!</h1>"

@route('/healthcheck')
def healthcheck():
    cache = apt.Cache()
    cache.update()
    cache.get_changes()
    cache.commit()

    return "what could possibly go wrong with {}?".format(socket.gethostname())

run(host='0.0.0.0', port=2112, debug=True)


