import re
import pandas as pd

def text_cleansing(text):
    if not isinstance(text, (str, bytes)):
        return text  # Return input as-is if it's not a string or bytes-like object
    # Bersihkan tanda baca (selain huruf dan angka)
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Konversi ke lowercase
    clean_text = clean_text.lower()
    # Bersihkan dengan kamus alay
    clean_text = clean_with_alay(clean_text)
    # Bersihkan dengan kamus abusive
    clean_text = clean_with_abusive(clean_text)
    return clean_text

def load_alay_dictionary():
    alay_csv_file = "csv_data/alay.csv"
    df_alay = pd.read_csv(alay_csv_file, delimiter="\t")
    if 'alay_word' in df_alay.columns:
        alay_dict = dict(zip(df_alay['alay_word'], df_alay['formal_word']))
    else:
        alay_dict = dict(zip(df_alay['alay'], df_alay['baku']))
    return alay_dict

def load_abusive_dictionary():
    abusive_csv_file = "csv_data/abusive.csv"
    df_abusive = pd.read_csv(abusive_csv_file)
    abusive_dict = set(df_abusive['ABUSIVE'])
    return abusive_dict

def clean_with_alay(text):
    # Load alay dictionary
    alay_dict = load_alay_dictionary()
    # Iterate over the dictionary and replace alay words with their formal counterparts
    for alay_word, formal_word in alay_dict.items():
        text = text.replace(alay_word, formal_word)
    return text

def clean_with_abusive(text):
    # Load abusive dictionary
    abusive_dict = load_abusive_dictionary()
    # Iterate over the dictionary and replace abusive words with an appropriate replacement (e.g., asterisks)
    for abusive_word in abusive_dict:
        text = text.replace(abusive_word, '***')
    return text

def cleansing_files(file_upload):
    # Read csv file upload, if there's an error with the default method, use encoding 'latin-1'
    # Take only the first column
    df_upload = pd.DataFrame(file_upload.iloc[:,0])
    # Rename the column to "raw_text"
    df_upload.columns = ["raw_text"]
    # Cleanse the text using the text_cleansing function
    # Store the results in the "clean_text" column
    df_upload["clean_text"] = df_upload["raw_text"].apply(text_cleansing)
    print("Cleansing text success!")
    return df_upload
