from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .models import studentii, anul1, anul2, anul3, usuarios
from flask_login import login_required, login_user, logout_user, current_user


# import smtplib
from flask_mail import Mail, Message
from flask import current_app
# from config import emal, senha


auth = Blueprint('auth', __name__)
mail = Mail()
# ......................................

@auth.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = studentii.query.filter_by(email=email).first()
    if request.method == 'POST':
        if user:
            if check_password_hash(user.parola, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash1 = 'Password incorrect!!'
        else:
            flash1 = 'Email does not exist!!'
    return render_template('login.html', user=current_user)

#
# @auth.route('/home')
# def home():
#     return render_template("home.html")

@auth.route('/formular', methods=['GET', 'POST'])
def formular():
    if request.method == 'POST':
        an = request.form['an']
        if an == '1':
            return redirect(url_for('auth.an1'))
        elif an == '2':
            return redirect(url_for('auth.an2'))
        elif an == '3':
            return redirect(url_for('auth.an3'))

    # # Obter o ID do usuário atualmente logado (substitua 'current_user.id' pelo atributo correto do objeto de usuário logado)
    # user_id = current_user.id
    #
    # # Consultar o banco de dados para obter as informações do usuário
    # user= studentii.query.get(user_id)
    #
    # anul = user.anul


    # especializare - "IR"
    return render_template("formular.html", user=current_user)



@auth.route('/an1')
def an1():

     return render_template("an1.html", user=current_user)

@auth.route('/submit_form1', methods=['POST'])
def submit_form1():
    an_studiu = request.form.get('an')
    semestrul = request.form.get('sem')
    algoritmi_si_structuri_de_date_I = request.form.get('1')
    programare_I = request.form.get('2')
    logica_computationala = request.form.get('3')
    algebra_si_geometrie_analitica=request.form.get('4')
    arhitectura_calculatoarelor=request.form.get('5')
    joburi_interes = ', '.join(request.form.getlist('job'))
    user_id = current_user.id  # Get the ID of the authenticated user

    new_data1 = anul1(user_id=user_id, an_studiu=an_studiu, semestrul=semestrul,
                       algoritmi_si_structuri_de_date_I =algoritmi_si_structuri_de_date_I,
                       programare_I=programare_I,
                       logica_computationala=logica_computationala, algebra_si_geometrie_analitica=algebra_si_geometrie_analitica,
                       joburi_interes=joburi_interes)

    db.session.add(new_data1)
    db.session.commit()

    disciplinas_recomendadas= []

    if joburi_interes == 'Frontend Engineer':
        disciplinas_recomendadas.append('Elemente de web design')
    if joburi_interes == 'Tester':
        disciplinas_recomendadas.append('Management Proiect Informatice')

    return render_template('recomandare.html', disciplinas=disciplinas_recomendadas, user=current_user)


@auth.route('/an2')
def an2():
    return render_template("an2.html", user=current_user)

@auth.route('/submit_form2', methods=['POST'])
def submit_form2():
    an_studiu = request.form.get('an')
    semestrul = request.form.get('sem')

    algoritmi_si_structuri_de_date_II = request.form.get('1')
    calcul_diferential_si_integral = request.form.get('2')
    programare_II = request.form.get('3')
    limbaje_formale_si_teoria_automatelor = request.form.get('4')
    teoria_grafurilor_si_combinatorica = request.form.get('5')
    sisteme_de_operare_I = request.form.get('6')
    baze_de_date_I = request.form.get('7')
    programare_III = request.form.get('8')
    structuri_de_date_avansate = request.form.get('9')

    joburi_interes = ', '.join(request.form.getlist('job'))
    user_id = current_user.id
    new_data2 = anul2(user_id=user_id, an_studiu=an_studiu, algoritmi_si_structuri_de_date_II=algoritmi_si_structuri_de_date_II,
                       calcul_diferential_si_integral = calcul_diferential_si_integral,
                       programare_II=programare_II,
                       limbaje_formale_si_teoria_automatelor=limbaje_formale_si_teoria_automatelor, teoria_grafurilor_si_combinatorica=teoria_grafurilor_si_combinatorica,
                      sisteme_de_operare_I=sisteme_de_operare_I,
                      baze_de_date_I=baze_de_date_I, programare_III=programare_III,
                      structuri_de_date_avansate=structuri_de_date_avansate,
                      joburi_interes=joburi_interes)

    db.session.add(new_data2)
    db.session.commit()

    # if semestrul == 2 and int(algoritmi_si_structuri_de_date_I) == 5:
    #     disciplinas_recomendadas.append('Structuri de date Avansate')
    return render_template('alege.html', user=current_user)


@auth.route('/an3')
def an3():
    return render_template("an3.html", user=current_user)

# Rota para lidar com o envio do formulário

@auth.route('/submit_form3', methods=['POST'])
def submit_form3():
    an_studiu = request.form.get('an')
    semestrul = request.form.get('sem')
    inginerie_soft = request.form.get('1')
    probabilitate_si_statistica = request.form.get('2')
    retele_de_calculatoare = request.form.get('3')
    programare_logica_si_functionala = request.form.get('4')

    ecuatii_diferentiale = request.form.get('5')
    inteligenta_artificiala = request.form.get('6')
    joburi_interes = ', '.join(request.form.getlist('job'))
    user_id = current_user.id
    new_data = anul3(user_id=user_id,an_studiu=an_studiu, semestrul=semestrul,inginerie_soft=inginerie_soft,probabilitate_si_statistica= probabilitate_si_statistica,
                     retele_de_calculatoare=retele_de_calculatoare,programare_logica_si_functionala=programare_logica_si_functionala,
                      ecuatii_diferentiale=ecuatii_diferentiale,inteligenta_artificiala=inteligenta_artificiala,
                      #, baze_de_date=baze_de_date,
                     # metode_numerice=metode_numerice, sisteme_inteligente=sisteme_inteligente,
                     joburi_interes=joburi_interes)

    db.session.add(new_data)
    db.session.commit()

    disciplinas_recomendadas = []

    if semestrul == '1' and int(retele_de_calculatoare) >= 5:
        disciplinas_recomendadas.append('Programare concurentă și distribuită')
    if semestrul == '1' and int(retele_de_calculatoare) >= 6:
        disciplinas_recomendadas.append('Administrarea Retelelor')
    if semestrul == '2' and int(inteligenta_artificiala) >= 7:
        disciplinas_recomendadas.append('Sisteme inteligente si Invatare Automata')
    if joburi_interes == 'Tehnician de securitate':
        disciplinas_recomendadas.append('Securitate și criptografie')
    if joburi_interes == 'Desenvolvedor Software' or int(inginerie_soft) >= 6:
        disciplinas_recomendadas.append('Programare concurentă și distribuită')
    if joburi_interes == 'Desenvolvedor Software' or int(inginerie_soft) >= 6:
        disciplinas_recomendadas.append('Testarea sistemelor software')
    if joburi_interes == 'Webdesigner':
        disciplinas_recomendadas.append('Dezvoltarea de aplicații pe platforma .NET')

    return  render_template('recomandare.html', disciplinas=disciplinas_recomendadas, user=current_user)


    # print(disciplinas_recomendadas)
    # return render_template('alege.html', user=current_user)


@auth.route('/alege')
def alege():
    return render_template("alege.html", user=current_user)

@auth.route('/alegerea', methods=['POST'])
def alegerea():
    if request.method == 'POST':
        nume = request.form.get('nume')
        prenume = request.form.get('prenume')
        especializare = request.form.get('especializare')
        an_studiu = request.form.get('an')
        semestrul = request.form.get('sem')
        disciplina_1 = request.form.get('disciplina1')
        disciplina_2 = request.form.get('disciplina2')
        disciplina_3 = request.form.get('disciplina3')
        disciplina_4 = request.form.get('disciplina4')
        user_id = current_user.id
        usuario = usuarios(user_id=user_id, nume=nume, prenume=prenume, especializare=especializare, an_studiu= an_studiu, semestrul=semestrul, disciplina_1=disciplina_1, disciplina_2=disciplina_2, disciplina_3=disciplina_3, disciplina_4=disciplina_4)

        # print("Valor de current_user.id:", user_id)
        db.session.add(usuario)
        db.session.commit()

        # mostra  mensagem de email
        subject = 'Alegerea disciplina optional'
        body = 'Salut, Va Informam ca ati trimis urmatoare Datele:\n\n' + \
               f'Prima Disciplina pentru semestrul 1: {request.form.get("disciplina1")}\n' + \
               f'Al doilea Disciplina pentru semestrul 1: {request.form.get("disciplina2")}\n' + \
               f'Prima Disciplina pentru semestrul 2: {request.form.get("disciplina3")}\n' + \
               f'Al doilea Disciplina pentru semestrul 2: {request.form.get("disciplina4")}\n'
        # Enviar o email
        try:
            msg = Message(subject=subject,
                          sender=current_app.config['MAIL_USERNAME'],
                          recipients=['siuzany.tome00@e-uvt.ro'])
            # Email do usuário como destinatário
            msg.body = body
            mail.send(msg)
            return 'Datele salvate și e-mailurile trimise cu succes!'
        except Exception as e:
            return 'A apărut o eroare la trimiterea e-mailului: ' + str(e)

        return 'Datele salvate cu succes în baza de date!'


@auth.route('/discipline')
def discipline():
    return render_template("discipline.html", user=current_user)

@auth.route('/recomandare')
def recomandare():
    return render_template("recomandare.html", user=current_user)

@auth.route('/contact')
def contact():
    current_page = 'contact'
    return render_template("contact.html", user=current_user, current_page=current_page)

@auth.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Aqui você pode processar os dados como quiser, incluindo enviar um email para você
        # Envie o email
        msg = Message(f'{name} te-a trimis un mensaj  ', sender='MAIL_USERNAME', recipients=['fmiuvt5@gmail.com'])
        msg.body = f'''{name}\n cu email: {email}\n te-a trimis urmatoare mensaj: {message}'''
        mail.send(msg)
        return 'Form submitted successfully'

@auth.route('/about')
def about():
    current_page = 'about'
    return render_template("about.html", user=current_user, current_page=current_page)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# @auth.route('/admin')
# def admin():
#     return render_template("admin.html",user=current_user)


@auth.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        prenume = request.form['prenume']
        nume = request.form['nume']
        email = request.form['email']
        parola = request.form.get('parola')
        facultate = request.form['facultate']
        anul = request.form['anul']
        hash_pass = generate_password_hash(parola, method='sha256')
        new_student = studentii(prenume=prenume, nume=nume, email=email, parola=hash_pass, facultate=facultate, anul=anul)
        db.session.add(new_student)
        db.session.commit()
        flash('Student Added successfully')
        return redirect(url_for('auth.admin'))

@auth.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    from . import db
    from .models import studentii
    new_student = studentii.query.filter_by(id=id).first()
    student_to_update = studentii.query.get_or_404(id)
    if request.method == "POST":
        student_to_update.prenume = request.form.get('prenume')

        student_to_update.numee = request.form.get('nume')
        student_to_update.email = request.form.get('email')
        student_to_update.parola = request.form.get('parola')
        student_to_update.facultate = request.form.get('facultate')
        student_to_update.anul = request.form.get('anul')

        db.session.commit()
        return redirect(url_for('auth.admin'))
    return render_template('edit.html', studentii=new_student)

@auth.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    new_student = studentii.query.get_or_404(id)
    db.session.delete(new_student)
    db.session.commit()
    flash('Employee Removed Successfully')
    return redirect(url_for('auth.admin'))

@auth.route('/admin')
def admin():
    data = studentii.query.all()
    return render_template('admin.html', studentii=data, user=current_user)
