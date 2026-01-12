"""
Modulo per la gestione dei clienti
"""

import re


class Cliente:
    """Rappresenta un cliente del cinema"""

    def __init__(self, id_cliente: str, nome: str, email: str, telefono: str = None):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email
        self.telefono = telefono

    def validazione_email(self) -> bool:
        """Verifica se l'email è formalmente valida"""
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, self.email) is not None

    def __str__(self):
        return f"{self.nome} ({self.email})"
