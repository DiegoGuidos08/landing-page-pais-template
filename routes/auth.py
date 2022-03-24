from pyexpat.errors import messages
from flask import Blueprint, redirect, render_template, redirect, url_for
from forms.Registerform import RegisterForm
from utils.db import db
from models.user import Contacto

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET", "POST"])
def home():
    form = RegisterForm()
    nombre = form.nombre.data
    apellido = form.apellido.data
    correo = form.correo.data
    mensaje = form.mensaje.data
    newComent = Contacto(nombre,apellido,correo, mensaje)
    db.session.add(newComent)
    db.session.commit()
    return render_template("home.html", form=form)
