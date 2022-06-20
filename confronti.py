from scipy import stats
import sys

#procedura che mi calcola la statistica di friedman prendendo in ingresso 
#name: contiene il nome del file dove salvare i risultati calcolati
def  confrontiF(name):
	#apro in lettura i file passati tramite parametro alla procedura
    path="/media/sdc/lissandrello/code/"
    f1 = open(path+"Stand_Betweeness.txt",'r')
    f2 = open(path+"Stand_Closeness.txt",'r')
    f3 = open(path+"Stand_Eigenvector.txt",'r')
    f4 = open(path+"Stand_Indegree.txt",'r') 
    f5 = open(path+"Stand_Outdegree.txt",'r')
    f6 = open(path+"Stand_Katz.txt",'r')
    f7 = open(path+"Stand_Pagerank.txt",'r')
   	#creo sette liste vuote come le centralità
    l1 = []; l2 = []; l3 = []; l4 = []; l5 = []; l6 = []; l7=[]
	#tre clicli for per caricare all'interno delle liste le varie misure
    for line in f1:
      l1.append(float(line))

    for line in f2:
      l2.append(float(line))

    for line in f3:
      l3.append(float(line))

    for line in f4:
      l4.append(float(line))

    for line in f5:
      l5.append(float(line))
    for line in f6:
      l6.append(float(line))
    for line in f7:
      l7.append(float(line))
    	#calcolo le statistiche tramite il modulo friedmanchisquare
    (statistic, p_value) = stats.friedmanchisquare(l1,l2,l3,l4,l5,l6,l7)

    	#scrivo i risultati in un file
    write_on_file(name, statistic, p_value)
    	
#procedura per scrivere all'interno di un file 2 misure (prima riga separati da uno spazio)
#name: contiene il nome del file dove scrivere le misure
#parameter1:prima misura da salvare
#parameter2:seconda misura da salvare
def write_on_file(name, parameter1, parameter2):
 #apro/creo il file in cui inserire le due misure
   # f_result = open("/media/sdc/lissandrello/data/"+name,'w')
    f_result= open("./"+name,'w')
    #scrivo la prima misura, separo da uno spazio e scrivo la seconda
    f_result.write(str(parameter1)+' '); f_result.write(str(parameter2)+'\n')
    #chiudo il file aperto/creato precedentemente
    f_result.close()
    

if(__name__=='__main__'):
   confrontiF(sys.argv[1])

