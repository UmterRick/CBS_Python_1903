from xml.etree import ElementTree

tree = ElementTree.parse("storage.xml")
root = tree.getroot()
print("Root: ", root)
for record in root:
    print(record)
    print("PK: ", record.attrib)
    for info in record:
        print(f"{info.tag} = {info.text}")


