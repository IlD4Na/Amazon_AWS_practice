import pandas as pd
import os

# Percorso del CSV originale
input_csv_path = "data/vini.csv"  # Cambia con il percorso reale, se diverso

# Cartella di output (può essere una directory temporanea o collegata a un bucket S3)
output_base_dir = "output"  # Puoi anche usare "/mnt/data/output" o simili

# Leggi il CSV originale
df = pd.read_csv(input_csv_path)

# Crea cartelle partizionate e salva CSV
for regione, group_df in df.groupby("regione"):
    # Nome cartella in formato "regione=NomeRegione"
    partition_folder = os.path.join(output_base_dir, f"regione={regione}")
    os.makedirs(partition_folder, exist_ok=True)
    
    # Percorso del CSV all'interno della cartella della partizione
    output_file_path = os.path.join(partition_folder, f"{regione}.csv")
    
    # Scrivi solo le colonne NON partizionate
    group_df.drop(columns=["regione"]).to_csv(output_file_path, index=False)

print("✅ CSV partizionati creati correttamente.")
