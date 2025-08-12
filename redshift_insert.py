import redshift_connector # Import the redshift_connector library to connect to Redshift
import os

from dotenv import load_dotenv # Import load_dotenv to load environment variables from a .env file

# Load environment variables from .env file which is located in the .venv directory

load_dotenv(dotenv_path='.venv/redshift_credentials.env')  


# Dictionary  with all the information needed to connect to the Redshift database

conn_info = {
    'host': 'professionai.470880515310.eu-west-3.redshift-serverless.amazonaws.com',
    'database':'professionai',
    'user': 'mio_utente',
    'password': os.getenv('REDSHIFT_PASS'),
    'port': 5439
}

# SQL statements for inserting data and joining tables 

# table my_schema.Persona

insert_persona_sql = """
INSERT INTO my_schema.Persona (cod_fiscale, name) VALUES
    ('RSSMRA85M01H501Z', 'Mario Rossi'),
    ('VRNGNN90A01H501Z', 'Giovanni Verdi'),
    ('BNCFNC80A01H501Z', 'Francesca Bianchi'),
    ('RMLGNN85A01H501Z', 'Luca Romani'),
    ('DMLGNN90A01H501Z', 'Daniela Meloni');
    """


# table my_schema.InfoPersona


insert_info_persona_sql = """
INSERT INTO my_schema.InfoPersona (cod_fiscale, address) VALUES
    ('RSSMRA85M01H501Z', 'Via Roma 1, Milano'),
    ('VRNGNN90A01H501Z', 'Via Milano 2, Roma'),
    ('BNCFNC80A01H501Z', 'Via Napoli 3, Torino'),
    ('RMLGNN85A01H501Z', 'Via Firenze 4, Bologna'), 
    ('DMLGNN90A01H501Z', 'Via Venezia 5, Napoli');
    """

#A join query to retrieve names and addresses from both tables 

join_query = """ 
SELECT p.name, p.cod_fiscale, ip.address
FROM my_schema.Persona p 
JOIN my_schema.InfoPersona ip ON p.cod_fiscale = ip.cod_fiscale;
"""

with redshift_connector.connect(**conn_info) as conn:
    with conn.cursor() as cursor:
        # Insert data into Persona table
        cursor.execute(insert_persona_sql)

        # Insert data into InfoPersona table 
        cursor.execute(insert_info_persona_sql)

        #Execute the join query to retrieve names and addresses
        cursor.execute(join_query)
        result = cursor.fetchall()
        for row in result:
            print(f"Name: {row[0]}, Codice Fiscale: {row[1]}, Address: {row[2]}")

        # Print the query plan 
        cursor.execute("EXPLAIN " + join_query)
        plan = cursor.fetchall()
        print("\nQuery Plan:")
        for p in plan:
            print(p[0])

'''
Importante : assicurarsi di utilizzare un utente che abbia i permessi per inserire dati 
nelle tabelle e per eseguire query di join. Inoltre, le tabelle devono essere create 
in precedenza con le colonne appropriate.
'''