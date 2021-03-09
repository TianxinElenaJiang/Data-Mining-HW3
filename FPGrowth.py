import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
import itertools as it
from mlxtend.frequent_patterns import fpgrowth
from collections import Counter

dataset = [['Bread','Milk'],
           ['Bread','Diaper','Beer','Eggs'],
           ['Milk','Diaper','Beer','Coke'],
           ['Bread','Milk','Diaper','Beer'],
           ['Bread','Milk','Diaper','Coke']]
te = TransactionEncoder()
te_ary=te.fit(dataset).transform(dataset)
df=pd.DataFrame(te_ary, columns=te.columns_)

#Parameters
minsup=0.4
minsupcount=minsup*len(df)
minconf=0.6

# Merge the dataset into a single list
merged = list(it.chain(*dataset))
print(merged)
c= Counter(merged)
print(c)
sorteddataset=[['Bread','Milk'],
               ['Bread','Diaper','Beer'],
               ['Milk','Diaper','Beer','Coke'],
               ['Bread','Milk','Diaper','Beer'],
               ['Bread','Milk','Diaper','Coke']]
item=list(it.chain(*sorteddataset))

#Tree class for FP-Tree
class tree:
    def __init__(self, parent, sup, name):
        self.nodeLink = None
        self.parent = parent
        self.sup = sup
        self.name = name
        self.children = []

def ispresent(node,name):
    f=-1
    for i in node.children:
        f=f+1
        if(i.name==name):
            return f
    return -1
lastocc=item[1]
frequent_itemsets=fpgrowth(df, min_support=0.4, use_colnames=True)
print(fpgrowth(df, min_support=0.4, use_colnames=True))
root = tree("root",-1,None)
z=0
for i in item:
    current=root
    for j in range(len(i)):
        if(ispresent(current,i[j])>=0):
            current=current.children[ispresent(current,i[j])]
            current.sup=current.sup+1
        else:
            child=tree(i[j],1,current)
            current.children.append(child)
            t=current
            current=current.children[ispresent(current,i[j])]
            current.parent=t

rule_antecedents = []
rule_consequents = []
