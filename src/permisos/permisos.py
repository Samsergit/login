
import firebase_admin
from firebase_admin import credentials, firestore

class Administrar_permisos():
    def __init__(self, db):
        self.db = db
    
    def obtener_permisos(self, usuario_id):
        documento = self.db.collection('usuarios').document(usuario_id)
        doc = documento.get()
        if doc.exists:
            return doc.to_dict().get('permisos', [])
        else:
            return []
        
    def asignar_permisos(self, usuario_id, nuevos_permisos):
        doc_ref = self.db.collection('usuarios').document(usuario_id)
        doc_ref.update({'permisos': nuevos_permisos})






