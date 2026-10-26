from flask import Flask, render_template, request, json

app = Flask(__name__)

#Global variables
name = "Darius Pasoch"
age = 20
activeUser = False

variable1 = "<div><h1>The User seems to be active, um... Yes</h1></div>"
variable2 = "<div><h1>The User seems to be not active, um... No, PLS go to <a href='/form'>FORM</a></h1></div>"

#vars for routes, for each the hub
varRoute1 = "<div><a href = '/form'>Form</a></div>"
varRoute2 = "<div><a href = '/Detes'>Personal Details</a></div>"
varRoute3 = "<div><a href = '/API/products'>Table Products From api.json</a></div>"

#Global functions
def personalInfoDetails(name, age, activeUser):
    return {
        "name": name,
        "age": age,
        "activeUser": activeUser
    }

#Global routes
@app.route('/')
def hub():
    return render_template('hub.html', varRoute1 = varRoute1, varRoute2 = varRoute2, varRoute3 = varRoute3)

@app.route('/Detes', methods = ['GET'])
def manage_form():
    personalInfo = personalInfoDetails(name, age, activeUser)
    return render_template('PersonalDetails.html', personalInfo = personalInfo, variable1 = variable1, varRoute1 = varRoute1, variable2 = variable2)

@app.route('/form', methods = ['GET'])
def form():
    titulo_pagina = "TotallyNotNigerianPrince.com"
    message = None
    return render_template('form.html', titulo = titulo_pagina, resultado = message)

@app.route('/send', methods = ['GET', 'POST'])
def response_form():
    nombre_usuario = request.form.get('nombre')
    correo_usuario = request.form.get('correo')
    titulo_pagina = "TotalyNotNigerianPrince.com"

    return render_template('response.html', titulo = titulo_pagina, nombre_usuario = nombre_usuario, correo_usuario = correo_usuario)

@app.route('/API/products', methods=['GET'])
def show_table():

    with open("api.json", "r", encoding="utf-8") as f:
        data_json = json.load(f)
    
    #Convertimos la cadena JSON a una lista de Python (lista de diccionarios)
    elements = data_json.items()

    #Pasamos la lista a una plantilla HTML
    return render_template('API/table.html', products=elements)

if __name__ == '__main__':
    app.run(debug=True)