import json

class Pedido:
    def __init__(self, id):
        self.id = id # atributos de instância
       #self.descricao = descricao
    def __str__(self):
        return f"{self.id}"



class Pedidos:
    objetos = [] # atributo de classe
    @classmethod
    def inserir(cls, obj):
        # abre a lista do arquivo
        cls.abrir()

        
        # insere o objeto na lista
        cls.objetos.append(obj)
        # salva a lista no arquivo
        cls.salvar()
    @classmethod
    def listar(cls):
        # abre a lista do arquivo
        cls.abrir()
        # retorna a lista para a UI
        return cls.objetos[:]
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        # percorre a lista procurando o id    
        for x in cls.objetos:
            if x.id == id: return x
        return None
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()        
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()        
    @classmethod
    def salvar(cls):
        with open("pedidos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("pedidos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)

                for obj in objetos_json:
                    c = Pedido(obj["id"])
                  
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass