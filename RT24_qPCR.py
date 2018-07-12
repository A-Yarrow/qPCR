#/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def filter_data():

    parser = argparse.ArgumentParser(description='visualize grouped bar charts for RT24 mutants')
    parser.add_argument('-filename', '-f', required=True, help='input file is a tab delimited file copied from excel spreadsheet' )
    parser.add_argument('-exclude_assays', '-exa', 
                        default=[], action = 'append',
                        help='Assays you do not want to include, usually negative controls.\
                              If assay has a space, surround it in quotes. Example: -ex \'serum albumin\'')
    parser.add_argument('-exclude_samples', '-exs',
                        default=[], action = 'append',
                        help='Samples you do not want to include. use -exs flag for each sample')
    
    args = parser.parse_args()
    filename = args.filename
    
    data_frame = pd.read_csv(filename, delim_whitespace=True, header = 0)
    #Change data format from "wide" to "long"
    df1 = pd.melt(data_frame, id_vars=['Sample'], var_name='Assay', value_name='CT').sort_values(['Assay', 'CT'])
    print (df1.columns.values)
    sample_exclude_list = args.exclude_samples
    assay_exclude_list = args.exclude_assays

    for i in assay_exclude_list:
        include_mask = ~df1['Assay'].str.contains(i)
        df1 = df1[include_mask]
        
    for i in sample_exclude_list:
        include_mask = ~include_df['Sample'].str.contains(i)
        df1 = df1[include_mask]
        
    df1.to_csv(filename[0:-4]+'_melt.txt', index_label=False)
    print (df1)
    return df1, filename

def plot_data():
    df, filename = filter_data()
    sns.barplot(x='Sample', y='CT', hue='Assay', data=df)
    plt.xticks(rotation=90)
    plt.ylabel('CT')
    plt.title(filename[0:-4])
    plt.savefig(filename[0:-4]+'_barplot.png')
    plt.tight_layout()
    plt.show()
    
plot_data()

    
    