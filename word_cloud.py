import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_word_cloud_from_csv(csv_file):
    # Read the CSV file with a specified delimiter
    df = pd.read_csv(csv_file, delimiter='\t')

    # Concatenate all text columns into a single string
    text = df.apply(lambda row: ' '.join(row.values.astype(str)), axis=1).str.cat(sep=' ')

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Plot the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Specify the path to the CSV file
csv_file = 'csv_data/data.csv'

# Generate word cloud from CSV
generate_word_cloud_from_csv(csv_file)