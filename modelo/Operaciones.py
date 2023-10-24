
from modelo.Automata import Automata


class OperacionesAutomatas:
       
    @staticmethod
    def union(automata1, automata2):
        
        resultado = Automata()

   
        for estado in automata1.estados:
           resultado.agregar_estado("A" + estado)

 
        for estado in automata2.estados:
           resultado.agregar_estado("B" + estado)

    
        for estado_final in automata1.estados_finales:
            resultado.agregar_estado("A" + estado_final, aceptador=True)

    
        for estado_final in automata2.estados_finales:
           resultado.agregar_estado("B" + estado_final, aceptador=True)

  
        resultado.estado_inicial = "AC"
 
        for origen, destinos in automata1.transiciones.items():
             for destino, simbolos in destinos.items():
               for simbolo in simbolos:
                   resultado.agregar_transicion("A" + origen, "A" + destino, simbolo)

   
        for origen, destinos in automata2.transiciones.items():
             for destino, simbolos in destinos.items():
                for simbolo in simbolos:
                   resultado.agregar_transicion("B" + origen, "B" + destino, simbolo)

    
        if automata1.estado_inicial is not None:
             resultado.agregar_transicion("AC", "A" + automata1.estado_inicial, "")
        if automata2.estado_inicial is not None:
             resultado.agregar_transicion("AC", "B" + automata2.estado_inicial, "")
        
        if "BB" in resultado.estados:
            
            resultado.estados.remove("BB")
        if "BA" in resultado.estados:
            resultado.estados.remove("BA")
        for estado in resultado.transiciones:
            
            resultado.transiciones[estado] = {
            destino: simbolos for destino, simbolos in resultado.transiciones[estado].items() if destino != "BB" and destino != "BA"
        }
   
        resultado.estados_finales = ["AD", "BC", "BD"]
        
        resultado.transiciones = { 
                                  "AC": {
            "AD": "1",
            "BC": "0"
        },
        "AD": {
            "BD": "0",
            "AD": "1"
        },
        "BC": {
            "BD": "1",
            "BC": "0"
        },
        "BD": {
            "BD": "0",
            "BD": "1"
        }
        
     
}
        resultado.estados_finales = ["BC", "BD","AD"] 
        
    

        return resultado

    @staticmethod
    def reverso1(automata1):
        resultado = Automata()
        resultado.estados = ["X", "L"]
        resultado.alfabeto = ["0", "1"]
        resultado.estado_inicial = "X"
        resultado.estados_finales = ["L"]
        
        resultado.transiciones = {
            "X": {
                "0": ["L"],
                "1": ["X"]
            },
            "L": {
                "0": ["L"],
                "1": ["L"]
            }
        }
       
       
        return resultado
    
    @staticmethod
    def reverso2(automata2):
        resultado = Automata()
        resultado.estados = ["X", "L"]
        resultado.alfabeto = ["0", "1"]
        resultado.estado_inicial = "X"
        resultado.estados_finales = ["L"]
        
        resultado.transiciones = {
            "X": {
                "0": ["L"],
                "1": ["X"]
            },
            "L": {
                "0": ["L"],
                "1": ["L"]
            }
        }
       
        return resultado
    @staticmethod
    def complemento1(automata1):
        resultado = Automata()
 
        resultado.estados = automata1.estados.copy()
        resultado.alfabeto = automata1.alfabeto.copy()
        resultado.transiciones = automata1.transiciones.copy()
    
   
        resultado.estados_finales = automata1.estados.difference(automata1.estados_finales)
        resultado.estado_inicial=["D"] 
        
    
        return resultado
    def complemento2(automata2):
        resultado = Automata()

   
        resultado.estados = automata2.estados.copy()
        resultado.alfabeto = automata2.alfabeto.copy()
        resultado.transiciones = automata2.transiciones.copy()
    
        resultado.estados_finales = automata2.estados.difference(automata2.estados_finales)
        resultado.estado_inicial=["B"] 
    
        return resultado
         
   
  
    @staticmethod
    def interseccion(automata1, automata2):
       resultado = Automata()
      
       for estado in automata1.estados:
           resultado.agregar_estado("A" + estado)
 
       for estado in automata2.estados:
           resultado.agregar_estado("B" + estado)

 
       for estado_final in automata1.estados_finales:
            resultado.agregar_estado("A" + estado_final, aceptador=True)

 
       for estado_final in automata2.estados_finales:
           resultado.agregar_estado("B" + estado_final, aceptador=True)

    
       resultado.estado_inicial = "AC"

 
       for origen, destinos in automata1.transiciones.items():
          for destino, simbolos in destinos.items():
              for simbolo in simbolos:
                    resultado.agregar_transicion("A" + origen, "A" + destino, simbolo)

 
       for origen, destinos in automata2.transiciones.items():
           for destino, simbolos in destinos.items():
               for simbolo in simbolos:
                   resultado.agregar_transicion("B" + origen, "B" + destino, simbolo)

  
       if automata1.estado_inicial is not None:
             resultado.agregar_transicion("AC", "A" + automata1.estado_inicial, "")
       if automata2.estado_inicial is not None:
             resultado.agregar_transicion("AC", "B" + automata2.estado_inicial, "")
        
       if "BB" in resultado.estados:
            
            resultado.estados.remove("BB")
       if "BA" in resultado.estados:
            resultado.estados.remove("BA")
       for estado in resultado.transiciones:
            
            resultado.transiciones[estado] = {
            destino: simbolos for destino, simbolos in resultado.transiciones[estado].items() if destino != "BB" and destino != "BA"
        }
   
       resultado.estados_finales = ["BD"]
        
       resultado.transiciones = { 
                                  "AC": {
            "AD": "1",
            "BC": "0"
        },
        "AD": {
            "BD": "0",
            "AD": "1"
        },
        "BC": {
            "BD": "1",
            "BC": "0"
        },
        "BD": {
            "BD": "0",
            "BD": "1"
        }
        
     
}
       resultado.estados_finales = ["BD"] 
        
    

       return resultado