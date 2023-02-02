import os
from azure.datalake.store import DataLakeStoreAccount

# Connect to Data Lake Store
account = DataLakeStoreAccount("<account_name>.azuredatalakestore.net", "<client_id>", "<client_secret>")

# Read a file from Data Lake Store
file_path = "<file_path_in_datalake_store>"
with account.read(file_path) as stream:
    data = stream.read()
    print(data)
