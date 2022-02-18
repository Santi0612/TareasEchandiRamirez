
class StringWork:
    def __init__(self):
        self.resultado=0
        self.decnorm={0:"",1:"dieci", 2:"venti",
                      3:"treinta",4:"cuarenta",
                      5:"cincuenta", 6:"sesenta",
                      7: "setenta", 8: "ochenta",
                      9: "noventa"} #diccionario con el nombre de la mayoria de las decenas
        self.decexcep={10:"diez",11:"once",12:"doce",13: "trece",
                       14:"catorce",15:"quince", 20:"veinte"}
        self.uni={0:"",1:"uno", 2:"dos",
                      3:"tres",4:"cuatro",
                      5:"cinco", 6:"seis",
                      7: "siete", 8: "ocho",
                      9: "nueve"} 
                  
    def string_work(self, palabra):
        Tipo=isinstance(palabra,str)# esta funcion revisa si lo que se ingrado es un string
        if not(Tipo):
            #print (1)
            return 1 #Error 1 coresponde a error por tipo 
        AaZ=palabra.isalpha()#esta funcion revisa si es un caracter alfabetico
        if not(AaZ):
            #print (2)
            return 2 #Error 2 coresponde a error por caracter no alfabetico 
        self.resultado=palabra.swapcase()# esta funcion le da vuelta a las palabras de mayuscula a minuscula
        print(self.resultado)
        return self.resultado
        
    def num_to_str(self, num):
        EsFloat=isinstance(num,float)# revisa si es una vriable float
        EsInt=isinstance(num,int)# revis si es una variable int
        if EsFloat: #error si no es un numero entero
            #print(3)
            return(3)
        elif EsInt:
            if num>99 or num <0:#error si no se encuentra entre 0 y 99 
                #print(3)
                return 3
            else:
                dec=num//10
                if num in self.decexcep:#arma el nombre de excepciones
                    self.resutlado = self.decexcep[num]
                    #print (self.resutlado)
                    return self.resutlado
                else:
                    self.resultado=self.decnorm[dec]
                    uni=num-(dec*10)
                    if dec>2:#si es mayor a 30 se arma el nombre normalmente
                        if uni==0:
                            self.resultado+=(self.uni[uni])# se usa para decenas enteras
                        else:
                            self.resultado+=("_y_"+ self.uni[uni])
                        #print(self.resultado)
                        return self.resultado
                    elif (num==0):#si el numero es 0
                        self.resultado = "cero"
                        #print(self.resultado)
                        return self.resultado
                    else:
                        self.resultado+=self.uni[uni]# si en numero es junto ejemplo veintiuno
                        #print(self.resultado)
                        return self.resultado   
        else:
            #print(4) #error si no es un numero
            return 4
        
        
            
        
        
        
        




