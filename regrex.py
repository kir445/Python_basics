import re
#it is  a way to scrape out specified texts 
#THIS IS KNOWN AS REGULAR EXPRESSONS
text=" yourname@gmail.com myname@888.net"
#re=libraryy contains compile()-the job of compile is to store the specied into pattern as a object
pattern=re.compile("[a-z0-9]+@[0-9a-zA-z]+\.[a-z]+")
#this is used to search the kind of specified text in an variable
#.peroid/ known as scape
result=pattern.findall(text)
print(result) 
