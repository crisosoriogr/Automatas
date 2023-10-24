class Automata:
    def __init__(self):
        self.estados = set()
        self.alfabeto = set()
        self.transiciones = {}
        self.estado_inicial = None
        self.estados_finales = set()

    def agregar_estado(self, estado, aceptador=False):
        self.estados.add(estado)
        if aceptador:
            self.estados_finales.add(estado)

    def agregar_transicion(self, estado_origen, estado_destino, simbolo):
        if estado_origen not in self.transiciones:
            self.transiciones[estado_origen] = {}
        if estado_destino not in self.transiciones[estado_origen]:
            self.transiciones[estado_origen][estado_destino] = []
        self.transiciones[estado_origen][estado_destino].append(simbolo)
