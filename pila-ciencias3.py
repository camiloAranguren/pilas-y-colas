class Pelicula:
  def __init__(self):
# datos sobre la pelicula (pelicula, protagonista)
   self.a = ["Terminator","arnold"]
   self.b = ["Lucy","scarlet"]
   self.c = ["Depredador","arnold"]
   self.d = ["Junior","arnold"]
   self.e = ["Ghost in the shell","scarlet"]
   self.f = ["Multiple","john"]
   self.g = ["X-men","john"]
       
class Pila:
    def __init__(self):
        # secrean dos listas vacias para apliar las peliculas
        self.peliculas=[]
        self.seleccion = []
    def apilar(self,x):
        # funcion para agregar un elemento a la pila
        self.peliculas.append(x)
        print "se apilo correctmente"
    def desapilar(self):
       # funcion para eliminar un elemento de la pila
       if (self.peliculas != []):
#       print "se desapilo"
        return self.peliculas.pop()
       else: 
        return "Lista vacia"
    def buscar(self,protago):
      # funcion para buscar la peliculas segun el protagonista
       while (self.peliculas != []):
         if (protago == self.peliculas[len(self.peliculas)-1][1]):
              self.seleccion.append(self.peliculas[len(self.peliculas)-1])
              Pila.desapilar()
         else:
              Pila.desapilar()
         if (self.peliculas == []):
             for i in self.seleccion:
                print i
           
Pelicula = Pelicula()
Pila = Pila()

Pila.apilar(Pelicula.a)
Pila.apilar(Pelicula.b)
Pila.apilar(Pelicula.c)
Pila.apilar(Pelicula.d)
Pila.apilar(Pelicula.e)
Pila.apilar(Pelicula.f)
Pila.apilar(Pelicula.g)

print "_____________________________________________________"
print " 'arnold'"
print " 'scarlet'"
print " 'john'"

protagonista = input("Escriba el nombre entre comillas('') del actor/actris que desea: ")

Pila.buscar(protagonista)


