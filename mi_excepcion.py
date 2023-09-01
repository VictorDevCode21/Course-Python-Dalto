class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")