# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# output: [1,'a','cat',2,3,'dog',4,5]

# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]

from audioop import reverse
from multiprocessing.connection import Listener


input1= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
input2= [[1, 2], [3, 4], [5, 6, 7]]


#question 1

listelem=[] #the output list
def controller(list):
    for elem in list: #for iteration
        if type(elem) == type(list): #check type of element in list
            controller(elem) #if element is list run function
        else:
            listelem.append(elem) #if element is not list add the element the final list

controller(input1)  
print(listelem)


#question 2
def all_reverse(liste):
    for elem in liste: #iteration of list
        if type(elem) == type(list): #control of list elements
            all_reverse(elem) 
        else:
            elem.reverse()


all_reverse(input2)
reversedliste=input2[::-1] #reverse the outer list
print(reversedliste)