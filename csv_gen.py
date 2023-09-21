from xml_parser import XMLParser
import pandas as pd

class CSVGenerator:
    def __init__(self):
        self.parser = XMLParser()
        self.agg_dict = {
            'Date': 'first',
            'TotalItems': 'sum',
            'TotalAmount': 'sum',
        }

    # Fetches data from database
    def fetch_data(self):
            select_query = "SELECT * FROM Sales"
            self.parser.cursor.execute(select_query)
            self.result = self.parser.cursor.fetchall()

    # Generates CSV from dataframe
    def generate_csv(self):
        self.fetch_data()
        data = []
        for row in self.result:
            data.append(row)
        df = pd.DataFrame(data, columns=['Date', 'StoreID', 'TotalItems', 'TotalAmount'])
        df['TotalAmount'] = pd.to_numeric(df['TotalAmount'], errors='coerce').fillna(0)
        df = df.groupby('StoreID').agg(self.agg_dict).reset_index()
        df['TotalReceipts'] = round(df['TotalAmount'].sum(), 2)
        df.loc[1:, 'TotalReceipts'] = ''
        df.to_csv('data.csv', index=False)

if __name__ == "__main__":
    csv_gen = CSVGenerator()
    csv_gen.generate_csv()