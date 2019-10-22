import panstarrs1
import poss
import merge
import pandas as pd

#This is the main loop
def cycle(ra,dec):
    for ra_i,dec_i in zip(ra,dec):
        panstarrs1.download(ra_i,dec_i)
        poss.download(ra_i,dec_i)
        merge.resize_pic(ra_i,dec_i)
        merge.merge_into_pic(ra_i,dec_i)
    
if __name__ == '__main__':
    df = pd.read_csv('data/Coord.csv')
    RA = df['correct_ra'].tolist()
    DEC = df['correct_dec'].tolist()
    cycle(RA,DEC)