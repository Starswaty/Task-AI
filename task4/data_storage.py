import pandas as pd

def save_to_csv(data, filename='financial_updates.csv'):
    df = pd.DataFrame(data)
    
    df = df[['title', 'source', 'link']]
 
    df['title'] = df['title'].str.strip()
    df['link'] = df['link'].str.strip()

    df.drop_duplicates(subset=['title', 'link'], inplace=True)
    
    df.to_csv(filename, index=False)
    return df
