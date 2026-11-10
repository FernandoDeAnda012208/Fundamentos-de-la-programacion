
![[Pasted image 20261109202924.png]]

class crea una clase 

def sirve para definir una funcion 

__init__  significa initialize, sirve para crear un objeto y darle sus valores iniciales

self representa el objeto que estas creando

en este caso nombre, promedio son parametros 

self.nombre y self.promedio son atributos, los cuales usaremos para crear nuestras funciones 

Ahora vamos a definir 2 funciones:

def saludar(self) y def enojo() son las funciones que vamos a crear 
tenemos que agregarle la funcion que va a hacer, para agergar los datos que los objetos van a aportar hay que escribir los atributos que antes creamos (self.nombre y self.promedio)

![[Pasted image 20261109204936.png]]


Ahora definimos los objetos, solo tenemos que crear una variable, en esta llamar a la clase que creamos y asignar los respectivos datos a los atributos que creamos (self.nombre es un String y self.promedio un float)

![[Pasted image 20261109205723.png]]

Para utilizar nuestras funciones con nuestros respectivos objetos tenemos que escribir el nombre del objeto y llamar al atributo que queremos usar (objeto.funcion())

De esta forma se pueden utilizar los mismos datos y darles diferentes propositos  o usos 

![[Pasted image 20261109210020.png]]

la abstracion se trata de transformar algo que podria ser muy complejo en algo mucho mas sencillo