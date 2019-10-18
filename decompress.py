def decompress_transfer(source_file):
    
    import pandas as pd

    file_name = source_file.split('/')[-1].split('.')[0]
    destin_file = file_name + '.csv'

    if str(source_file).lower().endswith('.gz'):
        df = pd.read_csv(source_file, index_col = False, compression='gzip', header=None, sep='|', quotechar='"', error_bad_lines=False)
        print('loaded dataframe')
        df.to_csv(destin_file, sep="|", header = None, line_terminator="\n")
        print('convert successfully')
    
    if str(source_file).lower().endswith('.dat'):
        df = pd.read_csv(source_file, index_col = False, header=None, sep='|', quotechar='"', error_bad_lines=False)
        print('loaded dataframe')
        df.to_csv(destin_file, sep="|", header = None, line_terminator="\n")
        print('convert successfully')
