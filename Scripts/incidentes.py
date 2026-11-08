from flask import Flask, render_template
from generador_logs import leer_logs_bloqueados

app = Flask(__name__)

@app.route('/')
def mostrar_incidentes():
    logs_bloqueados = leer_logs_bloqueados()
    return render_template('HTML/views/incidentes.html', incidentes=logs_bloqueados)

if __name__ == '__main__':
    app.run(debug=True)
