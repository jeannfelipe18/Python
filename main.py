#number_int = 10 # numero inteiro
#number_float = 10.5 # numero flutuante
#name_str = "Hello, World!" #string texto
#is_bool = True # booleano False / True

#print(number_int)
#print(number_float)
#print(name_str)
#print(is_bool)

#course_name = "Python Programming"

#print(len(course_name)) # len(): retorna o tamanho da string
#print(course_name[0]) # []: acessa o caractere na posição 0
#print(course_name[-1]) # []acessa o caractere na posição -1
#print(course_name[0:3]) # [:]: acessa um intervalo de caracteres
#print(course_name[3:]) # [:] : acessa um intervalo de caracteres

#first = "Jeann"
#last = "Moreira"
#full_name = first + " " + last ou full_name = f"{first} {last}" saem o mesmo resultado as duas formas 
#print(full_name)

course = "Python Programming"
course2 = "python programming"

#modified_str = course.upper() guarda a formatação de tamanho de letra
#print(modified_str)
print(course.upper()) # retorna string com todas as letras maiusculas
print(course.lower()) # retorna a string com todas as letras minusculas
print(course2.title()) # retorna a string com a primeira letra de cada palavra maiuscula
print(course.strip()) # remove os espaços em branco em cada lado da string
print(course.lstrip()) # remove os espaços em branco em cada lado esquerdo da string
print(course.rstrip()) # remove os espaços em branco apenas do lado direito da string
print(course.find("P")) # retorna o indice da primeira ocorrencia
print(course.replace("Python", "Django")) # retorna a string com o texto substituido
# print(course.replace("P", "j"))
print("Pro" in course2) # retorna True ou False