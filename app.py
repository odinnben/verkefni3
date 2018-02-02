import os
from bottle import route,run,template,static_file,error

frettir = [
    {
        'Header': 'Fréttir 1',
        'Content': 'Irma hefur rústað allt í florida þetta er sá stærsti sem við höfum séð',
        'Image': 'Irma.png',
        'Reporter':'odinn@frettir.com'

    },
    {
        'Header': 'Fréttir 2',
        'Content': 'Þessi fiksur er svakalega stór '
                   'hann var veiddur kl 6 í morgunn af þessum herramönnum '
                   'ég var svo heppin að fá mynd af þeim með þessum fisk',
        'Image': 'fisk.png',
        'Reporter':'odinn@frettir.com'
    },
    {
        'Header': 'Fréttir 3',
        'Content': 'ísland verður að rifa sig í gang í körfubolta ég er að meina að Finnland vann okkur Finnland',
        'Image': 'base.png',
        'Reporter':'odinn@frettir.com'

    },
    {
        'Header': 'Fréttir 4',
        'Content': 'Hún ólöf okkar er að slátra í golfinu hún er bæði flott og ljóshærð ',
        'Image': 'olof.png',
        'Reporter':'odinn@frettir.com'
    }

]
@route('/')
def index():
    return template('verk3')

@route('/b')
def lidurb():
    return template('index', frettir=frettir)

@route('/frett/<n>')
def frett(n):
    return template('frett',frettir[int(n)])
###################################
@route('/a')
def lidura():
    return template('lidura')

@route('/kt/<kennitala>')
def kt(kennitala):
    return template('kt', kennitala=kennitala)

@error(404)
def error404(error):
    return '<h1>Síðan sem þú baðst um er ekki til...</h1>'

@route('/myndir/<filename>')
def server_static(filename):
    return static_file(filename,root='./myndir' )

@route('/css/<filename>')
def server_static(filename):
    return static_file(filename,root='./css' )

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
