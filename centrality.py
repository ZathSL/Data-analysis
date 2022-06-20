import networkit as nk
import numpy as np
import datetime
import sys

namefolder=''
	

def calc_centrality(path,name_folder):
 #apro il file contenente il grafo in forma testuale, in lettura
  f= open(path,'r')
  
 #variabile globale che mi indica il path dove salvare le varie distribuzioni
  global namefolder
  
 #assegno alla variabile globale il folder passato come parametro dalla riga di comando
  namefolder=name_folder
  
 #carico i grafi in memoria 
  reader= nk.graphio.EdgeListReader(separator=' ', firstNode=0, directed=True)
  G= reader.read(path)


 #Out-degree centrality
  
  print("Inizio Out-degree, Current time:-", datetime.datetime.now())
  centrality = nk.centrality.DegreeCentrality(G, False, True, True).run()
  write_on_file(centrality.scores(),'Degree_Centrality(Out-degree)')

  write_on_file(centrality.ranking(),'Degree_Centrality(Out-degree)RANK')

 #In-degree centrality
 
  print("Inizio In-degree, Current time:-", datetime.datetime.now())
  centrality = nk.centrality.DegreeCentrality(G, False, False, True).run()
  write_on_file(centrality.scores(),'Degree_Centrality(In-degree)')
  
  write_on_file(centrality.ranking(),'Degree_Centrality(In-degree)RANK')
  
 #Eigenvector centrality
  
  print("Inizio Eigenvector, Current time:-", datetime.datetime.now())
  centrality = nk.centrality.EigenvectorCentrality(G, tol=1e-9).run()
  write_on_file(centrality.scores(),'Eigenvector_Centrality')
  
  write_on_file(centrality.ranking(),'Eigenvector_CentralityRANK')
  
  
   #PageRank centrality
  
  print("Inizio PageRank, Current time:-", datetime.datetime.now())
  centrality = nk.centrality.PageRank(G, damp=0.85, tol=1e-9).run()
  
  write_on_file(centrality.scores(),'Page_Rank')
 
  write_on_file(centrality.ranking(),'Page_RankRANK')
  
  
  #Katz centrality (variante dell'eigenvector e PageRank centrality)
  
  print("Inizio Katz, Current time:-", datetime.datetime.now())
  centrality = nk.centrality.KatzCentrality(G,alpha=0.0005,beta=0.1,tol=1e-08).run()
  write_on_file(centrality.scores(),'Katz_Centrality')

 
  write_on_file(centrality.ranking(),'Katz_CentralityRANK')
   
 #ApproxBetweenness centrality
  
  print("Inizio Betweenness, Current time:-", datetime.datetime.now())
  centrality =nk.centrality.ApproxBetweenness(G,epsilon=0.01, delta=0.1, universalConstant=1.0).run()
  
  write_on_file(centrality.scores(),'Approx_Betweenness')
  
  write_on_file(centrality.ranking(),'Approx_BetweennessRANK')
  
  
 #Closeness centrality
  
  print("Inizio Closeness, Current time:-", datetime.datetime.now())
  centrality = nk.centrality.Closeness(G, False, nk.centrality.ClosenessVariant.Generalized).run()

  write_on_file(centrality.scores(),'Closeness_Centrality')
  
  write_on_file(centrality.ranking(),'Closeness_CentralityRANK')
   #chiudo il file dei grafi, aperto precedentemente
   
  print("Fine Closeness, Current time:-", datetime.datetime.now())
  f.close()
  


 #procedura per salvare i risultati di centralità in un file
def write_on_file(list_centrality, name):
  global namefolder
  #diamo il nome al file dove salvare i risultati uno per riga
  namefile = "/media/sdc/lissandrello/data/"+namefolder+'/'+name+'.txt'
  #apriamo il file (lo creiamo se non è presente)
  f = open(namefile, 'w') 
  #convertiamo la lista di float in str per poterle scrivere nel file
  new_list = []
  for item in list_centrality:
     new_list.append(str(item)+'\n')
     
  f.writelines(new_list)
  #chiudiamo il file
  f.close()


if(__name__=='__main__'):
	calc_centrality(sys.argv[1],sys.argv[2])
