from sqlalchemy import create_engine, Column, Integer, String, ForeignKey   #importando membros especificos da biblioteca sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker   #importando membros especificos da biblioteca sqlalchemy.orm

URL = "mysql+mysqlconnector://root:123456@localhost:3306/ORM"       #faz a conexão com o banco mysql:// senha e usuario : porta/nome do banco

# $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin
# mysql> CREATE DATABASE ORM;
# mysql> USE ORM;
# mysql> SHOW TABLES;

Base = declarative_base()   #construção de uma classe base para definir classes declarativas

#Criação das classes e seus atributos
class Jogador(Base):
    __tablename__ = "Jogador"
    id_jogador = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)

class Personagem(Base):
    __tablename__ = "Personagem"
    id_personagem = Column(Integer, primary_key=True)
    hp = Column(Integer, nullable=False)
    lv = Column(Integer, nullable=False)
    forca = Column(Integer, nullable=False)
    destreza = Column(Integer, nullable=False)
    classe = Column(String(60), nullable=False)

class Habilidade(Base):
    __tablename__ = "Habilidade"
    id_habilidade = Column(Integer, primary_key=True)
    nomehabilidade = Column(String(60), nullable=False)
    tipo = Column(String(60), nullable=False)

class Inventario(Base):
    __tablename__ = "Inventario"
    id_inventario = Column(Integer, primary_key=True)
    tipo = Column(String(60), nullable=False)

class Item(Base):
    __tablename__ = "Item"
    id_item = Column(Integer, primary_key=True)
    efeito = Column(String(150), nullable=False)
    raridade = Column(Integer, nullable=False)
    requer_forca = Column(Integer, nullable=False)
    requer_destreza = Column(Integer, nullable=False)
    descricao = Column(String(200), nullable=False)

class Arma(Base):
    __tablename__ = "Arma"
    id_arma = Column(Integer, primary_key=True)
    nome_arma = Column(String(60), nullable=False)
    alcance = Column(Integer, nullable=False)
    dano = Column(Integer, nullable=False)

class Armadura(Base):
    __tablename__ = "Armadura"
    id_armadura = Column(Integer, primary_key=True)
    nome_armadura = Column(String(60), nullable=False)
    tipo = Column(String(60), nullable=False)
    defesa = Column(Integer, nullable=False)

class Mapa(Base):
    __tablename__ = "Mapa"
    id_mapa = Column(Integer, primary_key=True)
    nome_mapa = Column(String(60), nullable=False)

class Cenario(Base):
    __tablename__ = "Cenario"
    id_cenario = Column(Integer, primary_key=True)
    descricao = Column(String(200), nullable=False)

class Clima(Base):
    __tablename__ = "Clima"
    id_clima = Column(Integer, primary_key=True)
    descricao = Column(String(200), nullable=False)

class Inimigo(Base):
    __tablename__ = "Inimigo"
    id_inimigo = Column(Integer, primary_key=True)
    nome_inimigo = Column(String(150), nullable=False)
    hp = Column(Integer, nullable=False)
    experiencia = Column(Integer, nullable=False)

class Ranking(Base):
    __tablename__ = "Ranking"
    id_ranking = Column(Integer, primary_key=True)
    pontuacao = Column(Integer, nullable=False)

def main():
    engine = create_engine(url=URL) #cria a conexão com o banco de dados

    Base.metadata.create_all(bind=engine)   #metadados é uma biblioteca que fornece acesso aos metadados do pacote instalado.
                                            #create_all() para criar as tabelas associadas aos seus modelos

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:        #inicia sessão, criação das tabelas
        jogador = Jogador(nome="Gwyn Lord of Cinder")
        id_jogador = jogador.id_jogador
        session.add(jogador)

    with Session.begin() as session:
        personagem = Personagem(hp=100, level=1, forca=10, destreza=11, classe='paladino')
        id_personagem = personagem.id_personagem
        session.add(personagem)

    with Session.begin() as session:
        habilidade = Habilidade(nome='Raio de luz solar', tipo='Milagre')
        id_habilidade = habilidade.id_habilidade
        session.add(habilidade)

    with Session.begin() as session:
        inventario = Inventario(tipo='Utilidade')
        id_inventario = inventario.id_inventario
        session.add(inventario)

    with Session.begin() as session:
        item = Item(efeito='Fogo', raridade=3, requer_forca=10, requer_destrza=11, descricao='espada de fogo')
        id_item = item.id_item
        session.add(item)

    with Session.begin() as session:
        arma = Arma(nome_arma='Espada de Gwyn', alcance=5, dano=20)
        id_arma = arma.id_arma
        session.add(arma)

    with Session.begin() as session:
        armadura = Armadura(nome_armadura='Traje real', tipo='Pesado', defesa=15)
        id_armadura = armadura.id_armadura
        session.add(armadura)

    with Session.begin() as session:
        mapa = Mapa(nome_mapa='Anor Londo')
        id_mapa = mapa.id_mapa
        session.add(mapa)

    with Session.begin() as session:
        cenario = Cenario(descricao='Um lugar belo e iluminado')
        id_cenario = cenario.id_cenario
        session.add(cenario)

    with Session.begin() as session:
        clima = Clima(descricao='Ensolarado')
        id_clima = clima.id_clima
        session.add(clima)

    with Session.begin() as session:
        inimigo = Inimigo(nome_inimigo='Kalameet', hp=250, experiencia=3500)
        id_inimigo = inimigo.id_inimigo
        session.add(inimigo)

    with Session.begin() as session:
        ranking = Ranking(pontuacao=2000)
        id_ranking = ranking.id_ranking
        session.add(ranking)


if __name__ == "__main__":
    main()