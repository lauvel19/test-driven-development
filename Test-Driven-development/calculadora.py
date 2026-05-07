class Calculadora:
    """
    Calculadora básica con operaciones aritméticas.
    """

    @staticmethod
    def sumar(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def restar(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiplicar(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def dividir(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("No se puede dividir entre cero")

        return a / b