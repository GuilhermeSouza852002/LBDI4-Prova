from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

URL = "mysql+mysqlconnector://root:123456@localhost:3306/ORM"

Base = declarative_base()


class Jogador(Base):
    __tablename__ = "Jogador"
    id_jogador = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    personagem_id = Column(Integer, ForeignKey("Personagem.id"), nullable=False)
    pontuacao_id = Column(Integer, ForeignKey("Ranking.id"), nullable=False)

class Personagem(Base):
    __tablename__ = "Personagem"
    id_personagem = Column(Integer, primary_key=True)
    hp = Column(Integer, nullable=False)
    lv = Column(Integer, nullable=False)
    forca = Column(Integer, nullable=False)
    destreza = Column(Integer, nullable=False)
    classe = Column(String(60), nullable=False)
    inventario_id = Column(Integer, ForeignKey("Inventario.id"), nullable=False)
    habilidade_id = Column(Integer, ForeignKey("Habilidade.id"), nullable=False)

class Habilidade(Base):
    __tablename__ = "Habilidade"
    id_habilidade = Column(Integer, primary_key=True)
    nomehabilidade = Column(String(60), nullable=False)
    tipo = Column(String(60), nullable=False)

class Inventario(Base):
    __tablename__ = "Inventario"
    id_inventario = Column(Integer, primary_key=True)
    tipo = Column(String(60), nullable=False)
    item_id = Column(Integer, ForeignKey("Item.id"), nullable=False)

class Item(Base):
    __tablename__ = "Item"
    id_item = Column(Integer, primary_key=True)
    efeito = Column(String(150), nullable=False)
    raridade = Column(Integer, nullable=False)
    requer_forca = Column(Integer, nullable=False)
    requer_destreza = Column(Integer, nullable=False)
    arma_id = Column(Integer, ForeignKey("Arma.id"), nullable=False)
    armadura_id = Column(Integer, ForeignKey("Armadura.id"), nullable=False)
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
    cenario_id = Column(Integer, ForeignKey("Cenario.id"), nullable=False)
    clima_id = Column(Integer, ForeignKey("Clima.id"), nullable=False)
    inimigo_id = Column(Integer, ForeignKey("Inimigo.id"), nullable=False)

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
    habilidade_id = Column(Integer, ForeignKey("Habilidade.id"), nullable=False)

class Ranking(Base):
    __tablename__ = "Ranking"
    id_ranking = Column(Integer, primary_key=True)
    pontuacao = Column(Integer, nullable=False)
def main():
    engine = create_engine(url=URL)

    Base.metadata.create_all(bind=engine)


    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        jogador = Jogador(nome="Gwyn")
        id_jogador = jogador.id_jogador
        session.add(jogador)

    with Session.begin() as session:
        jogador.nome = "Gwyn, Lord of Cinder"
        id_jogador = jogador.id_jogador
        session.add(jogador)



if __name__ == "__main__":
    main()