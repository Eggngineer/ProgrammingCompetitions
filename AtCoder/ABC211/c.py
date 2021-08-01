# chokudai=['c','h','o','k','u','d','a','i']
# tmp=list(str(x) for x in input().split())
# word=[]
# for x in tmp[0]:
#     word.append(x)
chokudai=('c','h','o','k','u','d','a','i')
import itertools
word = input()
all = itertools.product(word, repeat=8)
all = list(all)
print(('c','h','o','k','u','d','a','i') in all)

