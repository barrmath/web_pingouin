#import bibliotheque flask et création application flask
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

#si bessoin ajouter les bibliotheque ici
app.config.from_object('config')
from .form import Form_ia_pingouin
from .util import ia_result

#routage des pages web
@app.route('/', methods = ['GET','POST'])
@app.route('/index/', methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/cv/', methods = ['GET','POST'])
def cv():
    return render_template('CV.html')

@app.route('/determination_pingouin/', methods = ['GET','POST'])
def form_ia_pingouin():
    form = Form_ia_pingouin()
    return render_template('form_ia_penguin.html',form=form)

@app.route('/resultat_pingouin/', methods = ['POST'])
def resultat_pingouin():
    specie = request.form['specie']
    bill_length_mm = request.form['bill_length_mm']
    bill_depth_mm =  request.form['bill_depth_mm']
    flipper_length_mm = request.form['flipper_length_mm']
    body_mass_g = request.form['body_mass_g']
    sex_prediction,sex_score = ia_result(specie,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g)
    sex_score = round(sex_score*100,2)
    
    return render_template('resultat_pingouin.html'
                            ,specie=specie
                            ,bill_length_mm = bill_length_mm
                            ,bill_depth_mm = bill_depth_mm
                            ,flipper_length_mm = flipper_length_mm
                            ,body_mass_g = body_mass_g
                            ,sex_prediction = sex_prediction
                            ,sex_score = sex_score
                            )

@app.route('/description_IA_pingouin/', methods = ['GET','POST'])
def description_ia_pingouin():
    return render_template('description_ia_penguin.html')