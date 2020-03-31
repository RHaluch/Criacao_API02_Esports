from my_app import db

class Esports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    nick = db.Column(db.String(100))
    time = db.Column(db.String(100))
    posicao = db.Column(db.String(100))
    abatimentos = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    mortes = db.Column(db.Integer)
    partidas = db.Column(db.Integer)
    vitorias = db.Column(db.Integer)
    propKDA = db.Column(db.Float(precision=3.2, asdecimal=False))
    porcentVitorias = db.Column(db.Float(precision=3.2, asdecimal=False))

    def calcularProporcao(self):
        if (self.mortes != 0):
            self.propKDA = round((self.assists + self.abatimentos) / self.mortes,2)
        else:
            self.propKDA = round(self.assists + self.abatimentos,2)

        self.porcentVitorias = round((self.vitorias / self.partidas) * 100, 2)

    def __init__(self, nome, nick, time, posicao, abatimentos, assists, mortes, partidas, vitorias):
        self.nome = nome
        self.nick = nick
        self.time = time
        self.posicao = posicao
        self.abatimentos = abatimentos
        self.assists = assists
        self.mortes = mortes
        self.partidas = partidas
        self.vitorias = vitorias
        self.calcularProporcao()

    def __repr__(self):
        return'Jogador: {0}'.format(self.id)
