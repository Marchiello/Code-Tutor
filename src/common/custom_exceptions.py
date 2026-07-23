"""Classe responsável por definir exceções personalizadas para a aplicação"""

# Documentação analisada
# https://www.geeksforgeeks.org/python/define-custom-exceptions-in-python/

class LLMException(Exception):
    """Exceção disparada para casos de erros relacionados à LLM"""

    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"[{self.error_code}] - Erro relacionado à LLM:\n{self.message}"
    
class DatabaseException(Exception):
    """Exceção disparada para erros relacionados ao Banco de Dados"""

    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"[{self.error_code}] - Erro relacionado à LLM:\n{self.message}"
    