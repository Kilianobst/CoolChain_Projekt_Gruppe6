import pyodbc

# Verbindungsdaten
server = 'tcp:sc-db-server1.database.windows.net,1433'
database = 'supplychain'
username = 'rse'
password = 'Pa$$w0rd'

conn_str = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=yes;'
    'TrustServerCertificate=yes;'
    'Connection Timeout=30;'
)

try:
    print("Klopfe beim Server an...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Nur ein kleiner Test-Snack, um die Leitung zu prüfen
    cursor.execute('SELECT TOP 5 * FROM dbo.coolchain')
    
    print("\n Erfolgreich verbunden! Hier sind die ersten 5 Datensätze:")
    print("-----------------------------------------------------------")
    
    for row in cursor:
        print(row)

    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print("\n Fehler beim Verbindungsaufbau:", e)