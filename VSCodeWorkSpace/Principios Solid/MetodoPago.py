class MetodoPago:
    def procesar_pago():
        pass

class PagoTarjeta(MetodoPago):
    def __init__(self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta

    def procesar_pago(self, cantidad):
        print(f"Procesando pago de {cantidad} usando tarjeta {self.numero_tarjeta}")

class PagoPaypal(MetodoPago):
    def __init__(self, cuenta_paypal):
        self.cuenta_paypal = cuenta_paypal

    def procesar_pago(self, cantidad):
        print(f"Procesando pago de {cantidad} usando cuenta de paypal: {self.cuenta_paypal}")


