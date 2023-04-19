from flask_restful import Resource

class Veiculos(Resource):
    def __init__(self, db):
        self.db = db

    def get(self):        
        objects = []
        cur = self.db.connection.cursor()
        keys = ['id', 'placa', 'descricao', 'status']
        cur.execute(
            '''SELECT id, placa, descricao, status FROM tlm_cad_veiculo LEFT JOIN tlm_sts_veiculo ON tlm_cad_veiculo.id = tlm_sts_veiculo.veiculo_id LIMIT 500''')
        items = cur.fetchall()        
        for item in items:
            obj_item = {}
            for (index, key) in enumerate(item):
                obj_key = keys[index]
                obj_item[obj_key] = key
                if len(obj_item) == 3:
                    objects.append(obj_item)

        return objects
