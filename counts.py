import pandas as pd
from pathlib import Path

dir = Path('./scripts/')

def main():
    df_list = []
    for file in dir.rglob('*counts*'):
        df = get_df(file)
        df_list.append(df)


    merged = pd.concat(df_list, axis=1)
    print(merged)

    merged.to_csv("designMatrix.txt", sep='\t')

def get_df(count_df):
    columns = ['gene_id', f'{count_df.stem}']
    df = pd.read_csv(count_df, sep='\t', names=columns)
    df = df.set_index('gene_id')

    return df


if __name__ == '__main__':
    main()
