from bottle import route, run
import subprocess


#import apt
#import apt.progress.text
#
# after much trial and error, I have concluded that python-apt is:
# * little used, based on available examples
# * not interested in providing me with terse output
# * too little bang for my investment bucks
# * unlikely to provide long-term leverage due to self-described "unstable" interface
#
# mallen - 2017.07.18


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

def prel2(doc, msg):
    doc.append('<pre>')
    doc.extend(msg)
    doc.append('</pre>')
    




@route('/hello')
def hello():
    doc = []
    h1(doc, 'Hello World!')
    return doc

@route('/lsb_release')
def lsb_release():
    doc = []
    h1(doc, 'lsb_release -a')
    try:
        out = subprocess.check_output(['/usr/bin/lsb_release', '-a'], stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        out = e.output
    prel2(doc, out)
    return doc



@route('/dist-upgrade')
def dist_upgrade():
    doc = []
    h1(doc, 'dist-upgrade!')

    try:
        out = subprocess.check_output(['/usr/bin/apt-get', 'dist-upgrade', '--assume-yes'], stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        out = e.output
    prel2(doc, out)
    return doc


@route('/check-upgrades')
def healthcheck():
    rv = []
    cmd='/usr/bin/apt-get --simulate dist-upgrade'
    h1(rv, cmd)
    try:
        out = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        out = e.output
    prel2(rv, out)
    return rv


@route('/healthcheck')
def healthcheck():
    rv = []
    h1(rv, 'healthcheck')
    pre(rv, 'what could possibly go wrong with {}?'.format(socket.gethostname()))

    return rv


@route('/')
def default():
    rv = []
    pre(rv, socket.gethostname())
    return rv


run(host='0.0.0.0', port=2112, debug=True)


