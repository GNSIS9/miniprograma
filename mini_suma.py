# -*- coding: utf-8 -*-
from pymongo import MongoClient

class RepositorioPeliculas:
    
   
    def __init__(self):
        self.peliculas = []
        self.cliente = MongoClient("mongodb://localhost:27017/") # Conexión a MongoDB
        self.db = self.cliente["peliculas_db"]
        self.coleccion = self.db["peliculas"]
        
    def actualizar_peliculas(self):
        query = {"titulo": "Matrix"}  
        documentos = self.coleccion.find(query)

        for documento in documentos:
            documento["director"] = "Lana Wachowski"
        self.coleccion.replace_one({"_id": documento["_id"]}, documento)

        print("Las películas se han actualizado correctamente en la base de datos.")
        self.cliente.close()
        
        x = RepositorioPeliculas()
        x.actualizar_peliculas()
      
      
