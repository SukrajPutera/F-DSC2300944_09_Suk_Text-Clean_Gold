import nltk
nltk.download('stopwords')
nltk.download('punkt')
import pandas as pd
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud
from nltk.corpus import stopwords as nltk_stopwords
from nltk.tokenize import word_tokenize

def generate_word_cloud_from_csv(csv_file, abusive_file, alay_file):
    # Read the CSV file with a specified delimiter
    df = pd.read_csv(csv_file, delimiter='\t')
    
    # Read the abusive words CSV file
    abusive_df = pd.read_csv(abusive_file, delimiter='\t')
    abusive_words = abusive_df['ABUSIVE'].values.tolist()

    # Read the alay words CSV file
    alay_df = pd.read_csv(alay_file, delimiter='\t')
    alay_words = alay_df['alay'].values.tolist()

    # Concatenate all text columns into a single string
    text = df.apply(lambda row: ' '.join(row.values.astype(str)), axis=1).str.cat(sep=' ')

    # Preprocess the text
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    stop_words = set(nltk_stopwords.words('indonesian'))  # Get Indonesian stopwords
    word_tokens = word_tokenize(text)  # Tokenize the text
    filtered_text = [word for word in word_tokens if word not in stop_words and word not in abusive_words and word not in alay_words]  # Remove stopwords, abusive words, and alay words

    # Join the filtered words back into a single string
    filtered_text = ' '.join(filtered_text)

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(filtered_text)

    # Plot the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Specify the path to the CSV file
csv_file = 'csv_data/data.csv'

# Specify the path to the abusive words CSV file
abusive_file = 'csv_data/abusive.csv'

# Specify the path to the alay words CSV file
alay_file = 'csv_data/alay.csv'

# Generate word cloud from CSV
generate_word_cloud_from_csv(csv_file, abusive_file, alay_file)
