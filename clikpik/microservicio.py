from flask import Flask
from os import environ
import json
from flask_sqlalchemy import SQLAlchemy
app = Flask('clikpik')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['TESTING'] = True
db = SQLAlchemy(app)


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    ubicacion = db.Column(db.String(120), unique=True, nullable=False)

#    def __repr__(self):
#        return '<Producto %r>' % self.nombre


@app.route('/nuevoproducto/<nombre>/<ubicacion>', methods=['POST'])
def nuevousuario(nombre,ubicacion):
    producto = Producto(nombre=nombre, ubicacion=ubicacion)
    db.session.add(producto)
    db.session.commit()
    return "nuevousuario"


@app.route("/update", methods=["POST"])
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    book = Book.query.filter_by(title=oldtitle).first()
    book.title = newtitle
    db.session.commit()
    return redirect("/")


@app.route('/')
def raiz():
    return json.dumps({
   "status": "OK",
   "ejemplo": { "ruta": "/producto1/37.204970,-3.602659",
                "valor": [{"nombre": "producto1", "posicion": "37.204970,-3.602659"}]
              }
})


@app.route('/productos')
def productos():
    todo= Producto.query.all()
    resultado = []
    for item in todo:
        temp = item.__dict__
        del temp["_sa_instance_state"]
        resultado.append(temp)
    return json.dumps(resultado)


@app.route('/initdb')
def initdb():
    db.create_all()
    return "Base de datos iniciada"

