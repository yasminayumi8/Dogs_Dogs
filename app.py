from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, select

from models import Veterinario, db_session, Consulta, Cliente, Animal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def home():
    return render_template('templates.html')


@app.route('/cadastro/cliente', methods=['GET', 'POST'])
def cadastro_cliente():
    if request.method == 'POST':
        # verifica os campos obrigatorios
        if not request.form["form_Nome1"] or not request.form["form_CPF"] or not request.form[
            "form_telefone" or not request.form["form_profissao"] or not request.form["form_area"]]:
            flash("preencher todos os campos", "error")
        else:

            # coletar os dados digitados pelo usuario
            nome = request.form["form_Nome1"]
            CPF = request.form["form_CPF"]
            telefone = request.form["form_telefone"]
            profissao = request.form["form_profissao"]
            area = request.form["form_area"]

            # procure no banco de dados se ja existe o cpf digitado
            user_CPF = select(Cliente).where(Cliente.CPF == CPF)
            user_CPF = db_session.execute(user_CPF).scalars().first()

            # verefique se ja existe o cpf
            if not user_CPF:
                # popular a classe usuario com os dados coletados
                user = Cliente(Nome1=nome, CPF=CPF, telefone=telefone, profissao=profissao, area=area)
                print(user)

                # salvar no banco
                user.save()
                db_session.close()
                flash("Cadastro realizado com sucesso!", "success")
                return redirect(url_for('lista_cliente'))
            else:
                flash("O CPF ja existe")
    return render_template('cadastro_cliente.html')


@app.route('/cadastro/consulta', methods=['GET', 'POST'])
def cadastro_consulta():
    if request.method == 'POST':
        if not request.form["form_motivo_id2"] or not request.form["form_hora"] or not request.form[
            "form_minuto"] or not request.form["form_data1"] or not request.form["form_idVeterinario"] or not \
        request.form["form_idAnimal2"]:
            flash("preencher todos os campos", "error")
        else:
            motivo = request.form["form_motivo_id2"]
            hora = request.form["form_hora"]
            minuto = request.form["form_minuto"]
            data = request.form["form_data1"]
            idVeterinario = request.form["form_idVeterinario"]
            idAnimal = request.form["form_idAnimal2"]

            consulta = Consulta(motivo_id2=motivo, hora=hora, minuto=minuto, data1=data, idVeterinario=idVeterinario, idAnimal2=idAnimal)
            print(consulta)

            # salvar no banco
            consulta.save()
            db_session.close()
            flash("Cadastro realizado com sucesso!", "success")
            return redirect(url_for('lista_consulta'))
    return render_template('cadastro_consulta.html')


@app.route('/cadastro/animal', methods=['GET', 'POST'])
def cadastro_animal():
    if request.method == 'POST':
        if not request.form["form_nome_animal"] or not request.form["form_raca1"] or not request.form["form_anoNasci"] or not request.form["form_idCliente3"]:
            flash("preencher todos os campos", "error")
        else:
            nome_animal = request.form["form_nome_animal"]
            raca1 = request.form["form_raca1"]
            anoNasci = request.form["form_anoNasci"]
            idCliente = request.form["form_idCliente3"]

            animal = Animal(nome_animal=nome_animal, raca1=raca1, anoNasci=anoNasci, idCliente=idCliente)
            print(animal)

            # salvar no banco
            animal.save()
            db_session.close()
            flash("Cadastro realizado com sucesso!", "success")
            return redirect(url_for('lista_animal'))
    return render_template('cadastro_animal.html')


@app.route('/cadastro/veterinario', methods=['GET', 'POST'])
def cadastro_veterinario():
    if request.method == 'POST':
        if not request.form["form_nomeVet"] or not request.form["form_salario2"] or not request.form["form_crmv"] or not \
        request.form["form_v_consulta1"]:
            flash("preencher todos os campos", "error")
        else:
            nomeVet = request.form["form_nomeVet"]
            salario2 = request.form["form_salario2"]
            crmv = request.form["form_crmv"]
            v_consulta1 = request.form["form_v_consulta1"]

            veterinario = Veterinario(nomeVet=nomeVet, salario2=salario2, crmv=crmv, v_consulta1=v_consulta1)
            print(veterinario)

            # salvar no banco
            veterinario.save()
            db_session.close()
            flash("Cadastro realizado com sucesso!", "success")
            return redirect(url_for('lista_veterinario'))
    return render_template('cadastro_veterinario.html')


@app.route('/lista/consulta')
def lista_consulta():
        sql_consulta = select(Consulta)
        resultado_consulta = db_session.execute(sql_consulta).scalars()
        lista_consulta = []
        for n in resultado_consulta:
            (lista_consulta.append(n.serialize_consulta()))
            print(lista_consulta[-1])
        return render_template('lista_consulta.html',
                               lista_consulta=lista_consulta)




@app.route('/lista/cliente')
def lista_cliente():
        sql_cliente = select(Cliente)
        resultado_cliente = db_session.execute(sql_cliente).scalars()
        lista_cliente = []
        for n in resultado_cliente:
            (lista_cliente.append(n.serialize_cliente()))
            print(lista_cliente[-1])
        return render_template('lista_cliente.html',
                               lista_cliente=lista_cliente)


@app.route('/lista/animal')
def lista_animal():
    sql_animal = select(Animal)
    resultado_animal = db_session.execute(sql_animal).scalars()
    lista_animal = []
    for n in resultado_animal:
        (lista_animal.append(n.serialize_animal()))
        print(lista_animal[-1])
    return render_template('lista_animal.html', lista_animal=lista_animal)


@app.route('/lista/veterinario')
def lista_veterinario():
        sql_veterinario = select(Animal)
        resultado_veterinario = db_session.execute(sql_veterinario).scalars()
        lista_veterinario = []
        for n in resultado_veterinario:
            (lista_veterinario.append(n.serialize_veterinario()))
            print(lista_veterinario[-1])
        return render_template('lista_veterinario.html',
                               lista_veterinario=lista_veterinario)


if __name__ == '__main__':
    app.run(debug=True)
