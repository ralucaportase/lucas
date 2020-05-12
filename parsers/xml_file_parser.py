from xml.dom import minidom
import csv


def write_loc_from_xml_file(xml_file: str, csv_file_name: str):
    xmldoc = minidom.parse(xml_file)
    loclist = xmldoc.getElementsByTagName('loc')
    csv_file = open(csv_file_name, 'w')
    writer = csv.writer(csv_file, delimiter=',')
    for loc in loclist:
        writer.writerow([loc.firstChild.nodeValue])


