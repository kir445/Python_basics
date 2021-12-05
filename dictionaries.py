from collections import OrderedDict

k={"keerti":0,"sharma":1}
#print(k.get("sharma"))
#(()are Tuples they are used for storing info which cant be appened lateri.e, for safety purposes)
#([] theses are lists or arrays which are used normally for storing indexed values)
#({} THese are used as sets that dosent stores duplicate values)
#({"":233}these are dictoniries that are used to stored random index given by us variables or data in a key-values format)


info={
  "keerti":("6578493","icici","23/02/2002"),
  "shruti":("7645839","sbi","27/01/2001"),
  "joe":("739284","bob","22/2/1986"),
  "jane":["6847803","icici","09/12/2012"],
  "Riya":{"acc_no":23464321,"bank_name":"icici","DOB":"23/09/2009"}
  }
  #ways of extracting values from dictionary
print(info["Riya"]["DOB"])
print(info.get("keerti"))
print(info["joe"][1])



#functions of dictionary


#get()
#iteams()
#values()

#.pop(itams)
#popiteams()
#.clear


#ordered dict
dict1=sorted(info)
print(dict1)
d=OrderedDict.fromkeys(info)
d.move_to_end('joe',last=False)
d.move_to_end('jane',last=False)
d.move_to_end('Riya')
''.join(d.keys())
print(d)
