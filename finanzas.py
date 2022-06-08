import re 



from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def bienvenida():

    return render_template ('bienvenida.html')


@app.route('/binance')

def binance():

    return render_template ('binance.html')

@app.route('/waves')

def waves():

    return render_template ('waves.html')

@app.route('/contacto')

def contacto():

    return render_template ('contacto.html')

@app.route('/enciclopedia')

def enciclopedia():

    return render_template ('enciclopedia.html')


#Modificaciones para activar la parte de simulacion #


if __name__  ==  '__main__' : 
     app.run(debug=True)

