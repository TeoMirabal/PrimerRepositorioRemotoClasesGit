
class Persona:

    def __init__(self, name, origen, trabajo):
        self.name = name
        self.origen = origen
        self.trabajo = trabajo

class Morito(Persona):
    
    def __init__(self, name):
        super().__init__(name, "Marruecos", "Amego un segarro? *La penetra sin consentimiento* (si es morito no hay delito)")

class Progre(Persona):

    def __init__(self, name):
        super().__init__(name, "España", "ULTRA DERECHA🤬" )
        

Mohamad = Morito("Mohamad")
print(Mohamad.name + "\n" + Mohamad.origen + "\n" + Mohamad.trabajo)

Charo = Progre("Karen")
print("nombre: " +Charo.name  +  "\n" + "origen: " + Charo.origen  + "\n" + "Trabajo: " + Charo.trabajo)


# para heredar (es uno?)
# para componer (tiene uno?)