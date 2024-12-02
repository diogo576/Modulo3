#programa para ler as notas de 3 alunos e caucular a media 
 
import exercicio1
#from  exercicio1 import mediaD

nota1=int(input("introduza uma nota:"))
nota2=int(input("introduza uma nota:"))
nota3=int(input("introduza uma nota:"))

media=exercicio1.mediaD(nota1,nota2,nota3)#mediaD

print(f"a media das notas é de {media}")
