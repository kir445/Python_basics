iteams=["apple","banana","Orange"]
prices=[0.99,0.45,0.88]
counts=[2,3,5]
sentences=[]

for (iteam,price,count) in iteams,prices,counts:
  iteam=str(iteam)
  price=str(price)
  count=str(count)
  sentence='I bought'+count+""+iteam+"s at"+price+"per cent."
  sentences.append(sentence)
print(sentences)
