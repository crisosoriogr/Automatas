import tkinter as tk
from tkinter import filedialog
import json
import networkx as nx
import matplotlib.pyplot as plt


from modelo.Automata import Automata
from modelo.Operaciones import OperacionesAutomatas


class AutomataApp:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.configure(bg="#000080")  # Fondo de color
        self.ventana_principal.title("Operaciones entre 2 Autómatas")
        self.ventana_principal.geometry("800x400+400+200")  # Tamaño de la ventana más pequeño
        

        self.canvas_frame = tk.Frame(self.ventana_principal)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)  # Expande para ocupar todo el espacio
        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.pack(fill=tk.BOTH, expand=True)  # Expande para ocupar todo el espacio

        self.automata1 = Automata()
        self.automata2 = Automata()
        self.resultado_automata = None

        self.menu = tk.Menu(self.ventana_principal)
        self.ventana_principal.config(menu=self.menu)

        self.menu_archivo = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.menu_archivo)
        self.menu_archivo.add_command(label="Cargar Autómata 1", command=self.cargar_automata1)
        self.menu_archivo.add_command(label="Cargar Autómata 2", command=self.cargar_automata2)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.ventana_principal.quit)

        self.menu_operaciones = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Operaciones", menu=self.menu_operaciones)
        self.menu_operaciones.add_command(label="Unión", command=self.union)
        self.menu_operaciones.add_command(label="Intersección", command=self.interseccion)
        self.menu_operaciones.add_command(label="Complemento del 1 Automata ", command=self.complemento1)
        self.menu_operaciones.add_command(label="Complemento del 2 Automata", command=self.complemento2)
        self.menu_operaciones.add_command(label="Reverso 1", command=self.Reverso1)
        self.menu_operaciones.add_command(label="Reverso 2 ", command=self.Reverso2)

        self.boton_cargar1 = tk.Button(self.canvas_frame, text="Cargar Autómata 1", command=self.cargar_automata1)
        self.boton_cargar2 = tk.Button(self.canvas_frame, text="Cargar Autómata 2", command=self.cargar_automata2)
        self.boton_union = tk.Button(self.canvas_frame, text="Operación de Unión", command=self.union)
        self.boton_interseccion = tk.Button(self.canvas_frame, text="Operación de Intersección", command=self.interseccion)
        self.boton_complemento1 = tk.Button(self.canvas_frame, text="Operación de Complemento del 1 Automata", command=self.complemento1)
        self.boton_complemento2 = tk.Button(self.canvas_frame, text="Operación de Complemento del 2 Automata", command=self.complemento2)
        self.boton_reverso1 = tk.Button(self.canvas_frame, text="Operación de Reverso1", command=self.Reverso1)
        self.boton_reverso2 = tk.Button(self.canvas_frame, text="Operación de Reverso2", command=self.Reverso2)

        self.boton_cargar1.pack()
        self.boton_cargar2.pack()
        self.boton_union.pack()
        self.boton_interseccion.pack()
        self.boton_complemento1.pack()
        self.boton_complemento2.pack()
        self.boton_reverso1.pack()
        self.boton_reverso2.pack()


    def cargar_automata(self, num_automata):
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        if ruta_archivo:
            with open(ruta_archivo, 'r') as archivo:
                datos_automata = json.load(archivo)
                automata = self.crear_automata_desde_datos(datos_automata)
                if num_automata == 1:
                    self.automata1 = automata
                else:
                    self.automata2 = automata
                self.dibujar_automata(automata)

    def cargar_automata1(self):
        self.cargar_automata(1)

    def cargar_automata2(self):
        self.cargar_automata(2)

    def dibujar_automata(self, automata):
        self.canvas.delete("all")

        G = nx.DiGraph()

        for estado in automata.estados:
            G.add_node(estado)

        for origen, destinos in automata.transiciones.items():
            for destino, simbolos in destinos.items():
                for simbolo in simbolos:
                    G.add_edge(origen, destino, label=simbolo)

        pos = nx.spring_layout(G, seed=42)

        labels = {edge: G.edges[edge]["label"] for edge in G.edges}
        colores_nodos = {estado: 'skyblue' for estado in automata.estados}
        
        nx.draw_networkx_nodes(G, pos, nodelist=colores_nodos.keys(), node_size=300, node_color=list(colores_nodos.values()))
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

        plt.axis("off")
        plt.show()

    def crear_automata_desde_datos(self, datos_automata):
        automata = Automata()

        # Agregar estados
        automata.agregar_estado(datos_automata["estado_inicial"])
        for estado_final in datos_automata["estados_finales"]:
            automata.agregar_estado(estado_final,aceptador=True)

        # Agregar transiciones
        for transicion in datos_automata["transiciones"]:
            automata.agregar_transicion(transicion["estadoActual"], transicion["estadoSiguiente"], transicion["simbolo"])
       

        return automata

    def guardar_resultado_en_json(self, automata_resultante, nombre_archivo):
        datos_automata = {
            "estado_inicial": automata_resultante.estado_inicial,
            "estados_finales": list(automata_resultante.estados_finales),
            "transiciones": []
        }

        for origen, destinos in automata_resultante.transiciones.items():
            for destino, simbolos in destinos.items():
                for simbolo in simbolos:
                    datos_transicion = {
                        "estadoActual": origen,
                        "estadoSiguiente": destino,
                        "simbolo": simbolo
                    }
                    datos_automata["transiciones"].append(datos_transicion)

        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos_automata, archivo, indent=4)

    def guardar_resultado(self, automata_resultante, nombre_archivo):
        self.guardar_automata_en_json(automata_resultante, nombre_archivo + ".json")
        self.dibujar_automata(automata_resultante, nombre_archivo + ".png")

    def union(self):
        if self.automata1 and self.automata2:
            self.resultado_automata = OperacionesAutomatas.union(self.automata1, self.automata2)
            self.dibujar_automata(self.resultado_automata)
            self.guardar_resultado_en_json(self.resultado_automata, "resultado_union.json")
           

    def interseccion(self):
        if self.automata1 and self.automata2:
            self.resultado_automata = OperacionesAutomatas.interseccion(self.automata1, self.automata2)
            self.dibujar_automata(self.resultado_automata)
            self.guardar_resultado_en_json(self.resultado_automata, "resultado_interseccion.json")

    def complemento1(self):
        if self.automata1:
            self.resultado_automata = OperacionesAutomatas.complemento1(self.automata1)
            self.dibujar_automata(self.resultado_automata)
            self.guardar_resultado_en_json(self.resultado_automata, "resultado_complemento1.json")
    def complemento2(self):
        if self.automata2:
            self.resultado_automata = OperacionesAutomatas.complemento2(self.automata2)
            self.dibujar_automata(self.resultado_automata)
            self.guardar_resultado_en_json(self.resultado_automata, "resultado_complemento2.json")

    def Reverso1(self):
        if self.automata1:
            self.resultado_automata = OperacionesAutomatas.reverso1(self.automata1)
            self.dibujar_automata(self.resultado_automata)
            self.guardar_resultado_en_json(self.resultado_automata, "resultado_reverso1.json")
    def Reverso2(self):
        if self.automata1:
            self.resultado_automata = OperacionesAutomatas.reverso2(self.automata2)
            self.dibujar_automata(self.resultado_automata)
            self.guardar_resultado_en_json(self.resultado_automata, "resultado_reverso2.json")