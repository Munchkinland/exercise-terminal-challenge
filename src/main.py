# Obligatorio: Generar una tabla usando Python con TODOS los ficheros (recursivamente) del workspace que contenga el nombre del fichero, el peso REAL y la última fecha de modificación.
import os
import datetime
import pandas as pd

def list_files_in_directory(directory):
    data = []
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            name = os.path.basename(full_path)
            size = os.path.getsize(full_path)
            modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
            data.append([name, size, modification_date])

    headers = ["Name", "Size", "Last Modification Date"]

    df = pd.DataFrame(data, columns=headers)

    # Export the DataFrame to an Excel file in the same directory as the script
    excel_file_path = os.path.join(directory, "information_files.xlsx")
    df.to_excel(excel_file_path, index=False)

base_directory = r"C:\Users\Rubén\Documents\GitHub\exercise-terminal-challenge"
list_files_in_directory(base_directory)

# Opcional: Hacer lo mismo que en la línea anterior pero en Bash Scripting y exportando un CSV