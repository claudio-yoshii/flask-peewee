from flask_restful import Resource, reqparse
from hashlib import sha1

class Usuarios(Resource):
    def __init__(self, db):
        self.db = db
        
    def check_senha(self, usuario):
        cur = self.db.connection.cursor()
        cur.execute("SELECT id FROM adm_cad_usuario WHERE login='{}'".format(usuario.usuario))  
        user = cur.fetchall()  
        
        if len(user):
            cur.execute('''SELECT senha FROM adm_lnk_usuario_credencial WHERE usuario_id="{}"'''.format(user[0][0]))  
            senha = cur.fetchall()
            senha = senha[0][0] 
            senha_enviada = sha1(usuario.senha.encode('latin1')).hexdigest()   
            if senha == senha_enviada:          
                return True                             
        else:
            return False
      
        
    def get(self):
        keys = ['id', 'empresa_id', 'grupoSuperior_id', 'nome', 'ativo', 'tipo', 'dados', ]
        objects = []    
        cur = self.db.connection.cursor()
        cur.execute('''SELECT * FROM tlm_cad_grupo''')    
        
        print(cur)
        items = cur.fetchall()    
        for item in items:
            obj_item = {}
            for (index,key) in enumerate(item):
                obj_key = keys[index]
                obj_item[obj_key] = key
                if len(obj_item) == 7:
                    objects.append(obj_item)

        return objects
    
    def post(self):
        args = reqparse.RequestParser()
        args.add_argument('usuario')
        args.add_argument('senha')        
        dados = args.parse_args()        
        print(dados)
        logged = Usuarios.check_senha(self, dados)        
        if logged:
            return {'msg':'ok', 'status':200, 'payload':{}}
        return {'error':'Erro de usuário ou senha', 'status':404}