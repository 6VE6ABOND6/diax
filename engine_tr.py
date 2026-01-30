import itertools
import datetime as T

todayYear=int(T.date.today().year)


def engineHearth(name,secondName,yearBirth):
 #name+symbol
 yield from nameGen(name,secondName,yearBirth)
 #name+team+symbol
 yield from teamGen(name)
 yield from teamGen(name.capitalize())
 #name+plate+#symbol
 yield from plateGen(name)
    

def symbolGen(word):
    
    symbols=["_",".","-","!"]
    for sembol in symbols:   
     if word[-4:].isdigit():
       yield word[:-4] + sembol + word[-4:] 
        
        
     elif word[:4].isdigit():
      yield word[:4] + sembol + word[4:]

       
     elif word[-2:].isdigit():
        yield word[:-2] + sembol + word[-2:] 
             
       
     yield word + sembol      
     yield sembol + word 
     
def nameGen(name,secondName,yearBirth):
 
 for i in range(2000,todayYear+1): #Name + 2002 + !
     f=f"{i}"
     
     yield from symbolGen(name+f)
     yield from symbolGen(name.capitalize()+f)
     
     
 pool={
     name,
     name.upper(),
     name[::-1],
     name.capitalize(),
     name.capitalize()+yearBirth,
     name+yearBirth,
     name+yearBirth[2:],
     name+secondName,
     name+secondName+yearBirth,
     
 }
 yield from pool
 
 
def teamGen(name):
     teamNames=["gs","bjk","fb","ts","bsk","ksk","goz","samsun","ads","eses","bursa","cimbom","aslan","ultraslan","kanarya","sari","lacivert",
                "kartal","kara","bordomavi","firtina","sarikirmizi","sari_lacivert","siyahbeyaz",
     ]
     teamYears=["1905","1907","1903","1967","1963","1954","1965","1925","1912","1453","1881","1938"]
     
     
     for t, y in itertools.product(teamNames, teamYears):
        peaces = [name, t, y]  
        for lenght in range(2,4):
          
         for placement in itertools.permutations(peaces,lenght):
             yield from symbolGen("".join(placement))
          
       
     
def plateGen(name):
        for i in range(1,82): #plate
         y=f"{i:02}"
    
        yield from symbolGen(y+name)
        yield from symbolGen(name+y)


    

