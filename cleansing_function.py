import re
import pandas as pd
from db import create_connection, get_abusive_data

def text_cleansing(text):
    # Bersihkan tanda baca (selain huruf dan angka)
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Konversi ke lowercase
    clean_text = clean_text.lower()
    # Bersihkan dengan kamus alay
    replacement_words = pd.read_csv("csv_data/alay.csv", delimiter="\t")
    replacement_dict = dict(zip(replacement_words['alay'], replacement_words['baku']))
    words = clean_text.split()
    replaced_words = [replacement_dict.get(word, word) for word in words]
    clean_text = ' '.join(replaced_words)
    # Bersihkan dengan kamus abusive
    conn = create_connection()
    df_abusive = get_abusive_data(conn)
    abusive_words = df_abusive['word'].tolist()
    for word in abusive_words:
        clean_text = clean_text.replace(word, '***')
    return clean_text

def cleansing_files(file_upload):
    # Read csv file upload, if there's an error with the default method, use encoding 'latin-1'
    df_upload = pd.DataFrame(file_upload.iloc[:,0])
    # Rename the column to "raw_text"
    df_upload.columns = ["raw_text"]
    # Cleanse the text using the text_cleansing function
    # Store the results in the "clean_text" column
    df_upload["clean_text"] = df_upload["raw_text"].apply(text_cleansing)
    print("Cleansing text success!")
    return df_upload