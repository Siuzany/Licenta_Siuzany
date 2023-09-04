from flask_login import UserMixin
from . import db

class studentii(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    prenume = db.Column(db.String(255), nullable=False)
    nume = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    parola = db.Column(db.String(255), nullable=False)
    facultate = db.Column(db.String(255), nullable=False)
    anul = db.Column(db.String(255), nullable=False)

class anul1(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    an_studiu = db.Column(db.Integer, nullable=False)
    semestrul = db.Column(db.Integer, nullable=False)

    algoritmi_si_structuri_de_date_I = db.Column(db.Integer, nullable=False)
    programare_I = db.Column(db.Integer, nullable=False)
    logica_computationala = db.Column(db.Integer, nullable=False)
    algebra_si_geometrie_analitica = db.Column(db.Integer, nullable=False)
    arhitectura_calculatoarelor = db.Column(db.Integer, nullable=False)
    joburi_interes = db.Column(db.String(255), nullable=False)

class anul2(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    an_studiu = db.Column(db.Integer, nullable=False)
    semestrul = db.Column(db.Integer, nullable=False)

    algoritmi_si_structuri_de_date_II = db.Column(db.Integer, nullable=False)
    calcul_diferential_si_integral = db.Column(db.Integer, nullable=False)
    programare_II = db.Column(db.Integer, nullable=False)
    limbaje_formale_si_teoria_automatelor = db.Column(db.Integer, nullable=False)

    teoria_grafurilor_si_combinatorica = db.Column(db.Integer, nullable=False)
    sisteme_de_operare_I = db.Column(db.Integer, nullable=False)
    baze_de_date_I = db.Column(db.Integer, nullable=False)
    programare_III = db.Column(db.Integer, nullable=False)
    structuri_de_date_avansate = db.Column(db.Integer, nullable=False)

    joburi_interes = db.Column(db.String(255), nullable=False)

class anul3(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    an_studiu = db.Column(db.Integer, nullable=False)
    semestrul = db.Column(db.Integer, nullable=False)

    inginerie_soft = db.Column(db.Integer, nullable=False)
    probabilitate_si_statistica = db.Column(db.Integer, nullable=False)
    retele_de_calculatoare = db.Column(db.Integer, nullable=False)
    programare_logica_si_functionala = db.Column(db.Integer, nullable=False)
    ecuatii_diferentiale = db.Column(db.Integer, nullable=False)
    inteligenta_artificiala = db.Column(db.Integer, nullable=False)
    joburi_interes = db.Column(db.String(255), nullable=False)

class usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    nume = db.Column(db.String(50))
    prenume = db.Column(db.String(50))
    especializare = db.Column(db.String(50))
    an_studiu = db.Column(db.Integer)
    semestrul = db.Column(db.Integer, nullable=False)
    disciplina_1 = db.Column(db.String(50))
    disciplina_2 = db.Column(db.String(50))
    disciplina_3 = db.Column(db.String(50))
    disciplina_4 = db.Column(db.String(50))