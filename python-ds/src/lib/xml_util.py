import xml.etree.ElementTree


def get_root(file_name):
    e = xml.etree.ElementTree.parse(file_name).getroot()
    return e


def get_row(root, row_name='row'):
    return root.findall(row_name)
