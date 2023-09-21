# XML File Parsing Project

This Git repository contains two Python scripts that perform the tasks of parsing XML files, uploading data to a database, and generating CSV file. It streamlines the process of working with XML data and converting it into CSV format.

## Libraries

Before getting started, ensure you have the following libraries installed on your system:

**1. XML Schema.** Library for XML validation and manipulation.

**2. MySQL Connector.** Library for Python to connect and interact with MySQL databases.

**3. Pandas.** Library for data manipulation and analysis.

To install these libraries run the following command in the terminal `pip install -r requirements.txt`

It will install libraries from [requirements.txt](requirements.txt) file

## Quick MySQL Installation Guide

1. Download MySQL Installer from [official website](https://dev.mysql.com/downloads/installer/).
2. Follow on-screen instructions, selecting "MySQL Server" and additional tools.
3. Set the MySQL root password during installation.

## MySQL Database Setup

Follow these steps to set up your MySQL database and create the "sales" table:

**1. Open MySQL Workbench and connect to your local MySQL server.**

**2. Create a new schema (database) named "salesdb" if it doesn't exist.**
   - Click "Server" > "Data Import."
   - Enter "salesdb" as the target schema name.
   - Click "Apply" to create the schema.

**3. Import the table structure.**

   - Click "Server" > "Data Import."
   - Select "Import from Self-Contained File."
   - Choose your [salesdb_sales.sql](salesdb_sales) file.

Your MySQL database and table will be ready for use, and it should appear like this after executing the following code:`SELECT * FROM salesdb.sales;`

| Date | StoredID | TotalItems | TotalAmount |
|------|----------|------------|-------------|

## Running the codes

Execute the `xml_parser.py`. This script is responsible for parsing data from XML files and uploading it to a database.

After successfully running `xml_parser.py`, run the `csv_gen.py` script. This script retrieves the data from the database and generates a CSV file named [data.csv](data.csv)
