import urllib

def download(ra,dec,cat_name='poss1_red',arc_sec=600,ID='None'):
    '''
    Retrives images with the mentioned size. In poss1_red 1arcsec = 1.7 pix
    more info in https://archive.stsci.edu/cgi-bin/dss_form/?fbclid=IwAR38yB4f_xiEjYB5ZFAytnKeeHn55QbHc7wUmTPu_eEFYrC4Cny4ulS0Nyk
    cat_name can be any of poss1_red,poss1_blue, poss2ukstu_red ,poss2ukstu_blue, poss2ukstu_ir, quickv, phase2_gsc2
    '''
    arc_min=arc_sec/60
    

#    Now we download the .gif file.
    Im_url='https://archive.stsci.edu/cgi-bin/dss_search?v=%s&r=%.7f&d=%.7f&e=J2000&h=%f&w=%f&f=gif&c=none&fov=NONE&v3='% (cat_name,ra,dec,arc_min,arc_min)
    Im_name ='images/%s/%.7f_%.7f.gif' % (cat_name,ra,dec)
#                Uncomment this for naming the files using ID
#                    Im_name= 'images/%s/%s.jpg' % (ID[i])             
    Image = open(Im_name,'wb')
    print('\nSaving image ',Im_name)
    Image.write(urllib.request.urlopen(Im_url).read())
    Image.close()

download(0,8)

