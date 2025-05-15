import pandas as pd

# Chargement du fichier Excel
df = pd.read_excel("Online Retail.xlsx", engine='openpyxl')

# Sélection des colonnes nécessaires
df = df[[
    'InvoiceNo',
    'StockCode',
    'Description',
    'Quantity',
    'InvoiceDate',
    'UnitPrice',
    'CustomerID',
    'Country'
]]

# Suppression des lignes avec CustomerID ou UnitPrice nulls
df = df.dropna(subset=['CustomerID', 'UnitPrice'])

# Optionnel : supprimer les doublons InvoiceNo + StockCode
df = df.drop_duplicates(subset=['InvoiceNo', 'StockCode'])

# Sauvegarde en CSV
df.to_csv("sales.csv", index=False)

print("Fichier sales.csv créé avec succès.")
