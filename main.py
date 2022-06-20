import sys
import statistics 

def rank(path, namefile, n):
    f = open(path, 'r')
    out = open("./"+namefile, 'w')
    cont = 0
    for riga in f:
      tmp = riga[1:riga.find(',')]
      out.writelines(tmp+'\n')
      cont = cont+1
      if(cont == n):
        break
    f.close()
    out.close()
def misure(path,path_result):
  result=open("./Lista200.txt",'r')
  misurain=open(path,'r')
  resultout=open(path_result,'w')
  l_result =[]; l_misure=[]; l_out=[]
  for riga in result:
    l_result.append(riga)
  for riga in misurain:
    l_misure.append(riga)
  for elem in l_result:
    for elem2 in l_misure:
      x=elem2[1:elem2.find(",")]
      y1=int(x)
      y2=int(elem)
      if(int(elem)==int(x)):
        print("trovato")
        l_out.append(elem2)
        break
  for e in l_out:
    resultout.writelines(e)
  result.close(); misurain.close() ; resultout.close()

def valori(path,namepath):
  f=open(path,'r')
  f2=open(namepath,'w')
  l = []; l1 = []
  for riga in f:
    tmp=riga[riga.find(',')+2:-2]
    l.append(float(tmp))
  for i in range(200):
    y=l[i]
    f2.writelines(str(y)+'\n')
  f.close(); f2.close()

def standardization(path, namepath):
  f=open(path,'r')
  f2=open(namepath,'w')
  l = [] ; l1 = []
  for riga in f:
    l.append(float(riga))
  
  somma = 0
  for elem in l:
    tmp = somma + elem
    somma = tmp
    
  media = somma / 200
  sd = statistics.stdev(l)
  for elem in l:
    z = (elem - media) / sd
    l1.append(z)
  
  for i in range(200):
    f2.writelines(str(l1[i])+'\n')
  
  f.close(); f2.close()
  
rank("/media/sdc/lissandrello/data/Money/Degree_Centrality(In-degree)RANK.txt","Lista200.txt",100)
resultin=open("./Lista200.txt",'r')
rank("/media/sdc/lissandrello/data/Money/Degree_Centrality(Out-degree)RANK.txt","Lista1000outdegree.txt",1000)

res=open("./Lista200.txt",'a')
outdegree=open("./Lista1000outdegree.txt",'r')
count=0
trovato=0;
l=[]
l2=[]
for riga in outdegree:
  l.append(riga)
for riga in resultin:
  l2.append(riga)
for elem in l:
  for elem2 in l2:
    if(elem==elem2):
      trovato=1 
      break
  if(trovato==0):
   res.writelines(elem)
   count=count+1
  else: 
    trovato=0
  if(count==100):
    break
outdegree.close(); res.close()
if(sys.argv[1]=="m"):
  misure(sys.argv[2],sys.argv[3])
if(sys.argv[1]=="v"):
  valori(sys.argv[2],sys.argv[3])
if(sys.argv[1]=="s"):
  standardization(sys.argv[2], sys.argv[3])

