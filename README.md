# Pratica AWS con boto3 

## Descrizione progetto
In questa repository troverete il workflow che ho seguito nello studio del servizio di AWS e nell'uso di questo servizio tramite linea di comando e script scritti in python. 


## Requisiti

- Python 3.x
- Le librerie nel file `requirements.txt`

## 📁 Struttura del progetto

```arduino
AWS_COURSE/
├── list_all_files_boto3.py 
├── Ordering_Pagination.py            # punto di ingresso
├── Upload_file.py 
├── requirements.txt        # dipendenze
├── .gitignore              # file ignorati
├── README.md
├── use_of_credentials.txt  # Istruzioni uso variabili d'ambiente con python-dotenv
├── src/                    # empty perchè dovrà essere poi riempito
├── tests/                  # test automatici
└── data/                   # eventuali dati (opzionale)
    └──firehose_test.csv    # Dataset usato 
    └──vini.csv             # Dataset su S3 con partizionamento Hive-like con AWS Athena

```

## Installazione

Clona il repository e installa le dipendenze:

```bash
git clone https://github.com/tuo-utente/nome-progetto.git
cd nome-progetto
pip install -r requirements.txt
'''

## Use_of_credentials.txt 

In questo file si possono trovare tutte le istruzioni su come andare a storare dati sensibili, siano questi password, utenti o altro tramite l'uso di variabili d'ambiente e della libreria python-dotenv.
