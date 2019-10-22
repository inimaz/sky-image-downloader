import urllib
import re


def download(ra,dec,f=[0,1,2,3,4],arc_sec=600,ID='None'):
    '''
    Retrives images from the mentioned filters and the mentioned size. 1 arcsec = 1pix
    '''
    filter_names=['g','r','i','z','y']
    Im_size = 4*arc_sec
#    First we look into the website looking for the name of the folders that contain
#    the images
    link = 'http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?ra=%f&dec=%f'% (ra,dec)
    print('Searching file in ',link)
    file = urllib.request.urlopen(link)
    starweb = file.read()
    print('\nThis is the content of the web:\n',starweb)
    X=re.findall('/rings.v3.skycell/[^* ]*.fits',str(starweb))
#    X is the directory we are searching for
#    nf is the name of the filter of each cutout according to the webpage
    nf=re.findall('\s[zirgy]\s',str(starweb))
    nf=[re.sub(' ','',filt) for filt in nf]
    print('These are the filters found:\n',nf)
#    Now we download the .jpg file.
#    urlwrite(url,filename) writes and saves a file from the given url, we
#    are going to use it but first we want only the filters that are 
#    specified in f
    for j in f:
        for k,x in zip(nf,X):
            if k==filter_names[j]:
#                Now we can use the urlwrite
                Im_url='http://ps1images.stsci.edu/cgi-bin/fitscut.cgi?red=%s&RA=%f&Dec=%f&size=%d&output_size=512'% (x,ra,dec,Im_size)
                Im_name ='images/pan-starrs1/%.7f_%.7f_%s.jpg' % (ra,dec,k)
#                Uncomment this for naming the files using ID
#                    Im_name= '%s_%s.jpg' % (ID[i],k)             
                Image = open(Im_name,'wb')
                print('\nSaving image ',Im_name)
                Image.write(urllib.request.urlopen(Im_url).read())
                Image.close()

#FINAL NOTE: it takes around 5 seconds to run the program for each pair of
#coordinates(asking for pictures from the 5 filters). So if your sample is
#big, go take a coffee :)
                    
if __name__=='__main__':
    download(0,8)