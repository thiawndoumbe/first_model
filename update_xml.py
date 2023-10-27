import xml.etree.ElementTree as ET

# parse the xml file
tree = ET.parse("original_file.xml")
root = tree.getroot()

# Modify the content of the xml file
for child in root:
    if child.tag == "element_to_change":
        child.text = "new_content"

# write the modified content to a new file
tree.write("modified_file.xml")