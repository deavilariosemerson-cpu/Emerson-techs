from flask import Flask, render_template, request, session, redirect, url_for
from models.ejercicios import Ejercicios
import random

app = Flask(__name__)

# Clave para poder utilizar sesiones
app.secret_key = "clave_secreta_ejercicios"

# Crear objeto de la clase Ejercicios
ejercicios = Ejercicios()


@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado_par_impar = None
    tabla = None
    resultado_adivinanza = None
    intentos = session.get("intentos", 0)

    if request.method == "POST":

        tipo = request.form.get("tipo")

        # ==========================================
        # EJERCICIO 1 - PAR O IMPAR
        # ==========================================

        if tipo == "par_impar":

            numero = int(request.form["numero"])

            resultado_par_impar = ejercicios.par_o_impar(numero)

        # ==========================================
        # EJERCICIO 2 - TABLA DE MULTIPLICAR
        # ==========================================

        elif tipo == "tabla":

            numero = int(request.form["numero_tabla"])

            tabla = ejercicios.tabla_multiplicar(numero)

        # ==========================================
        # EJERCICIO 3 - ADIVINA EL NÚMERO
        # ==========================================

        elif tipo == "adivinar":

            # Si todavía no existe número secreto,
            # creamos uno
            if "numero_secreto" not in session:
                session["numero_secreto"] = random.randint(1, 100)
                session["intentos"] = 0

            numero_secreto = session["numero_secreto"]

            intento = int(request.form["intento"])

            session["intentos"] += 1

            intentos = session["intentos"]

            resultado_adivinanza = ejercicios.adivinar_numero(
                numero_secreto,
                intento
            )

            # Si acertó, eliminamos el número secreto
            if resultado_adivinanza == "¡Correcto! Has adivinado el número.":
                session.pop("numero_secreto", None)

        # ==========================================
        # NUEVO JUEGO
        # ==========================================

        elif tipo == "nuevo_juego":

            session.pop("numero_secreto", None)
            session["intentos"] = 0

            return redirect(url_for("inicio"))

    return render_template(
        "index.html",
        resultado_par_impar=resultado_par_impar,
        tabla=tabla,
        resultado_adivinanza=resultado_adivinanza,
        intentos=intentos
    )


if __name__ == "__main__":
    app.run(debug=True)