import xml.etree.ElementTree as ET

tree = ET.parse("/Users/binjesus/Parse XML/stocks.xml")
root = tree.getroot()

print(root.tag)
print(len(root))

#Access root child
print(root[0].tag)
print(len(root[0]))

#Loop over root children

for child in root:
    print(child[2].tag)
    print(child[2].text)

#Root Grandchildren
print(root[0][0].tag)
print(root[0][0].text)

print(root[1][0].tag)
print(root[1][0].text)

#Get attribute
print(root.attrib)

#loop over ticker tag
for ticker in root.iter('ticker'):
    print(ticker.text)


#Find Children with price tag
print(len(root[0].findall('price')))
print(root[0].findall('price')[0].text)

#Change price and remove currency
root[0][2].text = "233"
root[1].remove(root[1][3])
tree.write("/Users/binjesus/Parse XML/stocks.xml")

