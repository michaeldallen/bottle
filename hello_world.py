from bottle import route, run


import apt
import apt.progress.text

import socket



def h1(doc, msg):
    doc.append('<h1>')
    doc.append(msg)
    doc.append('</h1>')
    return doc

def pre(doc, msg):
    doc.append('<pre>')
    doc.append(msg)
    doc.append('</pre>')

def prel(doc, msg):
    doc.append('<pre>')
    doc.extend('\n'.join(msg))
    doc.append('</pre>')
    




@route('/hello')
def hello():
    doc = []
    h1(doc, 'Hello World!')
    return doc


@route('/dist-upgrade')
def dist_upgrade():
    doc = []
    doc2 = []
    h1(doc, 'dist-upgrade!')

    # First of all, open the cache
    cache = apt.Cache()
    # Now, lets update the package list
    doc2.append(str(cache.update()))
    # We need to re-open the cache because it needs to read the package list
    doc2.append(str(cache.open(None)))
    # Now we can do the same as 'apt-get upgrade' does
    ## cache.upgrade()
    # or we can play 'apt-get dist-upgrade'
    doc2.append(str(cache.upgrade(True)))
    # Q: Why does nothing happen?
    # A: You forgot to call commit()!
    ## cache.commit(apt.progress.TextFetchProgress(), apt.progress.InstallProgress())
    doc2.append(str(cache.commit()))

    prel(doc, doc2)

    return doc


@route('/healthcheck')
def healthcheck():
    rv = []
    h1(rv, 'what could possibly go wrong with {}?'.format(socket.gethostname()))
    pre(rv, 'foo')
    return rv


@route('/')
def default():
    rv = []
    pre(rv, socket.gethostname())
    return rv


run(host='0.0.0.0', port=2112, debug=True)


