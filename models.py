#importar biblioteca.
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float

#importar session e sessionmaker.
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, relationship

#configurar a conexão de banco.
engine = create_engine('sqlite:///base_vet_analise_1.sqlite3')

#gerenciar sessao com banco de dados.
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Veterinario(Base):
    __tablename__ = 'TAB_VETERINARIO'
    id_vet = Column(Integer, primary_key=True)
    salario2 = Column(Float, nullable=False, index=True)
    nomeVet = Column(String(40), nullable=False, index=True)
    crmv = Column(Integer, nullable=False, index=True)
    v_consulta1 = Column(Float, nullable=False, index=True)

    def __repr__(self):
        return '<veterinario: {} {}>'.format(self.id_vet, self.salario2, self.nomeVet, self.crmv, self.v_consulta1)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_veterinario(self):
        dados_veterinario = {
            'id_vet': self.id_vet,
            'salario': self.salario2,
            'nome_vet': self.nomeVet,
            'crmv': self.crmv,
            'valor_consulta': self.v_consulta1
        }
        return dados_veterinario


class Consulta(Base):
    __tablename__ = 'TAB_CONSULTA'
    idConsulta = Column(Integer, primary_key=True)
    motivo_id2 = Column(String(40), nullable=False, index=True)
    hora = Column(String(40), nullable=False, index=True)
    minuto = Column(String(40), nullable=False, index=True)
    data1 = Column(Float, nullable=False, index=True)
    idVeterinario = Column(Integer, ForeignKey('TAB_VETERINARIO.id_vet'))
    idAnimal2 = Column(Integer, ForeignKey('TAB_ANIMAL.id_animal'))
    animal_relacao = relationship("Animal")
    veterinario_relacao = relationship("Veterinario")

    def __repr__(self):
        return '<consulta: {} {}>'.format(self.idConsulta, self.motivo_id2, self.hora, self.data1, self.idVeterinario, self.idAnimal2, self.minuto)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_consulta(self):
        dados_consulta = {
            'idVeterinario': self.idVeterinario,
            'motivo_id2': self.motivo_id2,
            'hora': self.hora,
            'minuto': self.minuto,
            'data1': self.data1,
            'idAnimal2': self.idAnimal2,
            'idConsulta': self.idConsulta
        }
        return dados_consulta


class Animal(Base):
    __tablename__ = 'TAB_ANIMAL'
    id_animal = Column(Integer , primary_key=True)
    nome_animal = Column(String(40), nullable=False, index=True)
    raca1 = Column(String(11), nullable=False, index=True, unique=True)
    anoNasci = Column(Integer, nullable=False, index=True)
    idCliente3 = Column(Integer, ForeignKey('TAB_CLIENTE.id_cliente'))
    cliente_relacao = relationship("Cliente")

    def __repr__(self):
        return '<Animal: {} {}>'.format(self.nome_animal, self.idCliente3, self.anoNasci, self.raca1, self.anoNasci)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_funcionario(self):
        dados_funcionario = {
            'id_animal': self.id_animal,
            'nome_animal': self.nome_animal,
            'raca1': self.raca1,
            'anoNasci': self.anoNasci,
            'idCliente3': self.idCliente3,
        }
        return dados_funcionario


class Cliente(Base):
    __tablename__ = 'TAB_CLIENTE'
    id_cliente = Column(Integer, primary_key=True)
    CPF = Column(String(11), nullable=False, index=True, unique=True)
    Nome1 = Column(String(40), nullable=False, index=True)
    telefone = Column(String(11), nullable=False, index=True)
    profissao = Column(String(40), nullable=False, index=True)
    area = Column(String(40), nullable=False, index=True)

    def __repr__(self):
        return '<cliente: {} {}>'.format(self.id_cliente, self.CPF, self.Nome1, self.profissao, self.area, self.telefone)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_movimentacao(self):
        dados_movimentacao = {
            'id_cliente': self.id_cliente,
            'CPF': self.CPF,
            'Nome1': self.Nome1,
            'telefone': self.telefone,
            'profissao': self.profissao,
            'area': self.area,
        }
        return dados_movimentacao


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()