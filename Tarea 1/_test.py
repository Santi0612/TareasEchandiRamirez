import pytest
from tarea1prog1 import StringWork
import string

tarea=StringWork()

def test_1(): #revisa que todos los caracteres de a a z de minuscula a mayuscula los puede cambiar 
    pinvert=string.ascii_uppercase+string.ascii_lowercase #todos los caracteres en mayuscula y luego en minuscula
    assert tarea.string_work(string.ascii_letters)==pinvert

def test_2(): #revis si se le da un numero como entrada responde el caracter correcto
    assert tarea.string_work(1)== 1
    
def test_3(): #revis si se le da un numero en str como entrada responde el caracter correcto
    assert tarea.string_work("1")== 2

def test_4():
    dic={0:"cero",
1:"uno",
2:"dos",
3:"tres",
4:"cuatro",
5:"cinco",
6:"seis",
7:"siete",
8:"ocho",
9:"nueve",
10:"diez",
11:"once",
12:"doce",
13:"trece",
14:"catorce",
15:"quince",
16:"dieciseis",
17:"diecisiete",
18:"dieciocho",
19:"diecinueve",
20:"veinte",
21:"ventiuno",
22:"ventidos",
23:"ventitres",
24:"venticuatro",
25:"venticinco",
26:"ventiseis",
27:"ventisiete",
28:"ventiocho",
29:"ventinueve",
30:"treinta",
31:"treinta_y_uno",
32:"treinta_y_dos",
33:"treinta_y_tres",
34:"treinta_y_cuatro",
35:"treinta_y_cinco",
36:"treinta_y_seis",
37:"treinta_y_siete",
38:"treinta_y_ocho",
39:"treinta_y_nueve",
40:"cuarenta",
41:"cuarenta_y_uno",
42:"cuarenta_y_dos",
43:"cuarenta_y_tres",
44:"cuarenta_y_cuatro",
45:"cuarenta_y_cinco",
46:"cuarenta_y_seis",
47:"cuarenta_y_siete",
48:"cuarenta_y_ocho",
49:"cuarenta_y_nueve",
50:"cincuenta",
51:"cincuenta_y_uno",
52:"cincuenta_y_dos",
53:"cincuenta_y_tres",
54:"cincuenta_y_cuatro",
55:"cincuenta_y_cinco",
56:"cincuenta_y_seis",
57:"cincuenta_y_siete",
58:"cincuenta_y_ocho",
59:"cincuenta_y_nueve",
60:"sesenta",
61:"sesenta_y_uno",
62:"sesenta_y_dos",
63:"sesenta_y_tres",
64:"sesenta_y_cuatro",
65:"sesenta_y_cinco",
66:"sesenta_y_seis",
67:"sesenta_y_siete",
68:"sesenta_y_ocho",
69:"sesenta_y_nueve",
70:"setenta",
71:"setenta_y_uno",
72:"setenta_y_dos",
73:"setenta_y_tres",
74:"setenta_y_cuatro",
75:"setenta_y_cinco",
76:"setenta_y_seis",
77:"setenta_y_siete",
78:"setenta_y_ocho",
79:"setenta_y_nueve",
80:"ochenta",
81:"ochenta_y_uno",
82:"ochenta_y_dos",
83:"ochenta_y_tres",
84:"ochenta_y_cuatro",
85:"ochenta_y_cinco",
86:"ochenta_y_seis",
87:"ochenta_y_siete",
88:"ochenta_y_ocho",
89:"ochenta_y_nueve",
90:"noventa",
91:"noventa_y_uno",
92:"noventa_y_dos",
93:"noventa_y_tres",
94:"noventa_y_cuatro",
95:"noventa_y_cinco",
96:"noventa_y_seis",
97:"noventa_y_siete",
98:"noventa_y_ocho",
99:"noventa_y_nueve"} # Diccionario con todos los nombres de los numeros
    for i in range(0,100):
        assert tarea.num_to_str(i)==dic[i]# se compara el nombe del diccionario con el del metodo

def test_5():
    assert tarea.num_to_str("hola")==4 #string en num_to string error debe ser 4

    
def test_6():
    assert tarea.num_to_str(45.0)==3 #se ingresa error de decimal
    assert tarea.num_to_str(-5)==3  #se ingresa error de negativo
    assert tarea.num_to_str(100)==3 #se ingresa error de num mayor a 99

#test_1()
#test_2()
#test_3()
#test_4()
#test_5()
