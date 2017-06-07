import argparser

#interpolacion
#otra_cadena = 'hola{}'.format('un valor')
variable_cuatro = 'hola {0} {1}'
var = 'hola {variable1} {variable2}'

def mi_function(val):
    print(variable_cuatro)
    print(var)

if __name__ == '__main__':
    parser=argparse.ArgumentParse()
	parser.add_argument('nombre')
	parser.add_argument('apellido')
	args=parser.parse_args()
	
	print(args.nombre)
	print(args.apellido)
	print(variable_cuatro.format(args.nombre, args.apellido))