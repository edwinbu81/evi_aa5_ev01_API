from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Base de datos para almacenar usuarios
usuarios_db = {
    'monica1': 'contraseña1',
    'monica2': 'contraseña2',
}
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if usuario not in usuarios_db:
            usuarios_db[usuario] = contraseña
            return redirect(url_for('inicio_sesion'))
        else:
            return render_template('registro.html', mensaje='El usuario ya existe.')
    return render_template('registro.html')

@app.route('/inicio_sesion', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if usuario in usuarios_db and usuarios_db[usuario] == contraseña:
            session['usuario'] = usuario
            return redirect(url_for('perfil'))
        else:
            return render_template('inicio_sesion.html', mensaje='Error en la autenticación.')
    return render_template('inicio_sesion.html')

@app.route('/perfil')
def perfil():
    if 'usuario' in session:
        return render_template('perfil.html', usuario=session['usuario'])
    else:
        return redirect(url_for('inicio_sesion'))

@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.pop('usuario', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)