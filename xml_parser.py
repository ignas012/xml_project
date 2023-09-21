import glob
import xmlschema
import xml.etree.ElementTree as ET
import mysql.connector

class XMLParser:
    def __init__(self):
        self.xmls = glob.glob("./receipts/*.xml")
        self.xsd_schema = xmlschema.XMLSchema("POSLogV6.0.0.xsd")
        self.ns = {'n0': 'http://www.nrf-arts.org/IXRetail/namespace/'}
        self.tags_to_find = ['DateTime', 'UnitID', 'Quantity', 'Total[@TotalType="TransactionNetAmount"]']
        self.db = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="admin",
            database="SalesDB"
        )
        self.cursor = self.db.cursor()

    # Checks if .xml file meets XSD schema requirements
    def files_validation(self):
        for xml in self.xmls:
                if self.xsd_schema.is_valid(xml):
                    self.xml_parsing(xml)
                else:
                    print(f"{xml} is not valid according to the XSD schema.")

    # Starts parsing .xml file
    def xml_parsing(self, xml):
        self.items = []
        tree = ET.parse(xml)
        root = tree.getroot()
        elements = [root.findall(f'.//n0:{tag}', self.ns) for tag in self.tags_to_find]
        item = []
        for element_list in elements:
            if len(element_list) == 0:
                item.append(None)
            else:
                for element in element_list:
                    item.append(element.text)
        self.items.append(item)
        self.upload_to_database()

    # Uploads parsed data to database
    def upload_to_database(self):
        insert_query = "INSERT INTO Sales (Date, StoreID, TotalItems, TotalAmount) VALUES (%s, %s, %s, %s)"
        for item in self.items:
            self.cursor.execute(insert_query, item)
        self.db.commit()

if __name__ == "__main__":
    parser = XMLParser()
    parser.files_validation()