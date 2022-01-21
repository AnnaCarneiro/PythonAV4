from config import *

class Pessoa(db.Model): # 1 classe
    id =db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    sobreNome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    
    #Método para imprimir em texto
    def __str__(self):
        return f'Id {self.id}) Nome: {self.nome} ' +\
               f'{self.sobreNome}, Email: {self.email}.'
    
    #Método de expressão da classe em Json
    def json(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "Sobrenome ": self.sobreNome,
            "Email": self.email,
        }
        
class Relacao(db.Model): # 2 classe
    id = db.Column(db.Integer, primary_key=True)
    nome =  db.Column(db.String(254))
    tipo =  db.Column(db.String(254))    
    
    def __str__(self):
        return f'relacao({self.id}): {self.nome}, ' +\
               f'tipo: {self.tipo}.'    
    
    def json(self):
        return{
            "id": self.id,
            "Nome:": self.nome,
            "Tipo:": self.tipo,
           
        }
        
class Caracteristicas(db.Model): # 3 classe
    id = db.Column(db.Integer, primary_key=True)
    nome =  db.Column(db.String(254))
    corOlhos = db.Column(db.String(254))
    corCabelo = db.Column(db.String(254))    
     
    def __str__(self):
        return f'Tipo({self.id}): {self.nome}, ' +\
               f'corOlhos: {self.corOlhos}, corCabelo: {self.corCabelo}'
        
    def json(self):
        return{
            "id": self.id,
            "Nome:": self.nome,
            "Cor dos Olhos:": self.corOlhos,
            "Cor do Cabelo": self.corCabelo
           
        }
        
class Brincadeira(db.Model): # 4 classe
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    descricao = db.Column(db.String(254))    
    
    def __str__(self):
        return f'Brincadeira({self.id}): {self.nome}, ' +\
               f'Descrição: {self.descricao}.'
        
    def json(self):
        return{
            "id": self.id,
            "Brincadeira:": self.nome,
            "Descrição:": self.descricao           
        }
        
class Especialidade(db.Model): # 5 classe
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    descricao = db.Column(db.String(254))    
    
    def __str__(self):
        return f'Especialidade({self.id}): {self.nome}, ' +\
               f'Descrição: {self.descricao}.'    
    
    def json(self):
        return{
            "id": self.id,
            "Especialidade:": self.nome,
            "Descrição:": self.descricao           
        }
class Pet(db.Model): # 6 classe
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    descricao = db.Column(db.String(254))
    
    #Método para imprimir em texto
    def __str__(self):
        return f'Pet({self.id}): {self.nome}, ' +\
               f'Descrição: {self.descricao}.'
    
    #Método de expressão da classe em Json
    def json(self):
        return{
            "id": self.id,
            "Pet:": self.nome,
            "Descrição:": self.descricao           
        }
        
class Pai(db.Model): # 7 classe
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    descricao = db.Column(db.String(254))    
    
    def __str__(self):
        return f'Habilidade({self.id}): {self.nome}, ' +\
               f'Descrição: {self.descricao}.'    
    
    def json(self):
        return{
            "id": self.id,
            "Pai:": self.nome,
            "Descrição:": self.descricao           
        }
class Mae(db.Model): # 8 classe
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    descricao = db.Column(db.String(254))
        
    def __str__(self):
        return f'Mae({self.id}): {self.nome}, ' +\
               f'Descrição: {self.descricao}.'    
    
    def json(self):
        return{
            "id": self.id,
            "Mae:": self.nome,
            "Descrição:": self.descricao           
        }
        
class Vestimenta(db.Model): # 9 classe
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    vestimenta = db.Column(db.String(254))
    
    #Método para imprimir em texto
    def __str__(self):
        return f'Vestimenta({self.id}): {self.nome}, ' +\
               f'Vestimenta: {self.vestimenta}.'
    
    #Método de expressão da classe em Json
    def json(self):
        return{
            "id": self.id,
            "Nome:": self.nome,
            "Vestimenta:": self.vestimenta      
        }
        
class Personagem(db.Model): # 10 classe
    # atributos dos Personagens
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    idade = db.Column(db.String(254))
    altura = db.Column(db.String(254))
    especialidade_id = db.Column(db.Integer, db.ForeignKey(Especialidade.id), nullable=False)
    especialidade = db.relationship("Especialidade")
      

    # método para mostrar em formato de texto
    def __str__(self):
        return f'Id {self.id}) {self.nome}, ' +\
                self.idade + ", " + self.altura + f'Especialidade: {self.especialidade} '    
            
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "altura": self.altura,
            "especialidade": self.especialidade                       
        }
        


# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    #Especialidade
    e1 = Especialidade(nome = "Cebolinha", descricao = "Planos infalíveis")
    e2 = Especialidade(nome = "Cascão", descricao = "Escapar da água") 
    e3 = Especialidade(nome = "Mônica", descricao = "Dar coelhadas")
    e4 = Especialidade(nome = "Magali", descricao = "Comer")
    e5 = Especialidade(nome = "Franjinha", descricao = "Cientista")

    # teste da classe Personagem
    t1 = Personagem(nome = "Cebolinha", idade = "7", 
        altura = "1,23", especialidade=e1)
    t2 = Personagem(nome = "Cascão", idade = "7", 
        altura = "1,20", especialidade=e2)   
    t3 = Personagem(nome = "Mônica", idade = "7", 
        altura = "1,10", especialidade=e3)     
    t4 = Personagem(nome = "Magali", idade = "7", 
        altura = "1,20", especialidade=e4)
    t5 = Personagem(nome = "Franjinha", idade = "9", 
        altura = "1,30", especialidade=e5)
    
    # testes demais classes 
    r1 = Relacao(nome = "Cascão", tipo = "Melhor amigo do Cebolinha")
    r2 = Relacao(nome = "Cebolinha", tipo = "Melhor amigo do Cascão")   
    r3 = Relacao(nome = "Magali", tipo = "Melhor amiga da Mônica")     
    r4 = Relacao(nome = "Mônica", tipo = "Melhor amiga da Magali")
    r5 = Relacao(nome = "Franjinha", tipo = "Namorado da Magali")
    
    c1 = Caracteristicas(nome = "Cascão", corOlhos = "Preto", corCabelo = "Preto")
    c2 = Caracteristicas(nome = "Cebolinha", corOlhos = "Preto", corCabelo = "Preto")   
    c3 = Caracteristicas(nome = "Magali", corOlhos = "Preto", corCabelo = "Preto")   
    c4 = Caracteristicas(nome = "Mônica", corOlhos = "Preto", corCabelo = "Preto")
    
    p1 = Pet(nome = "Chovinista", descricao = "Porquinho do Cascão")
    p2 = Pet(nome = "Floquinho", descricao = "Cachorro do Cebolinha")
    p3 = Pet(nome = "Mingau", descricao = "Gato da Magali")
    p4 = Pet(nome = "Mônicão", descricao = "Cachorro da Mônica")
    
    pai1 = Pai(nome = "Antenor Cordeiro de Araújo", descricao = "Pai do Cascão, muito companheiro do filho.")
    pai2 = Pai(nome = "Seu Cebola", descricao = "Pai do Cebolinha, trabalha em um escritório e é atencioso.")
    pai3 = Pai(nome = "Paulo Lima (Seu Paulinho)", descricao = "Pai da Magali, é funcionário de uma construtora e alégico ao Mingau.")
    pai4 = Pai(nome = "Luis Rodolfo Castro de Sousa (Seu Sousa)", descricao = "Pai da Mônica, trabalha em uma companhia de negócios.")
    
    mae1 = Mae(nome = "Maria de Lurdes Pereira Marques (Lurdinha)", descricao = "Mãe do Cascão")
    mae2 = Mae(nome = "Dona Cebola", descricao = "Mãe do Cebolinha")
    mae3 = Mae(nome = "Lidia Lima (Dona Lili)", descricao = "Mãe da Magali")
    mae4 = Mae(nome = "Luisa Moreira de Sousa (Dona Luisa)", descricao = "Mãe da Mônica")
    
    v1 = Vestimenta(nome = "Cascão", vestimenta = "Sua roupa é amarela com um short de suspensório vermelho xadrez")
    v2 = Vestimenta(nome = "Cebolinha", vestimenta = "Sua roupa é camisa verde, shorts pretos e sapatos marrons")
    v3 = Vestimenta(nome = "Magali", vestimenta = "Sua roupa é um vestido amarelo")
    v4 = Vestimenta(nome = "Mônica", vestimenta = "Sua roupa é um vestido vermelho")
    
    # persistir
    db.session.add(t1)
    db.session.add(t2)
    db.session.add(t3)
    db.session.add(t4)
    db.session.add(t5)
    db.session.add(r1)
    db.session.add(r2)
    db.session.add(r3)
    db.session.add(r4)
    db.session.add(r5)
    db.session.add(c1)
    db.session.add(c2)
    db.session.add(c3)
    db.session.add(c4)
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(pai1)
    db.session.add(pai2)
    db.session.add(pai3)
    db.session.add(pai4)
    db.session.add(mae1)
    db.session.add(mae2)
    db.session.add(mae3)
    db.session.add(mae4)
    db.session.add(v1)
    db.session.add(v2)
    db.session.add(v3)
    db.session.add(v4)
    db.session.commit()
    
    # exibir 
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(pai1)
    print(pai2)
    print(pai3)
    print(pai4)
    print(mae1)
    print(mae2)
    print(mae3)
    print(mae4)
    print(v1)
    print(v2)
    print(v3)
    print(v4)
    
    #exibir json
    print(t1.json())
    print(t2.json())
    print(t3.json())
    print(t4.json())
    print(t5.json())