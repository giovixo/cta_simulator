
author = 'Giovanni De Cesare'
date = '2017-11-30'

def info():
    """
    Description: Print infos

    Usage: info()
    """
    print "Some tool to write CTA event files into mysql db"
    print "Author: " + author
    print "Date: " + date

def write(fileName='events.fits'):
    """
    Description: insert lines into the database

    Usage: write(), write(fileName)
    """
    # Connect to mysql db
    import pymysql
    db = pymysql.connect(host='localhost', user='root', passwd='CTArta2017@', db='evt-db')
    cur = db.cursor()

    # Read the fit file
    from astropy.io import fits
    hdulist = fits.open(fileName)
    tbdata = hdulist[1].data
    print "no of elements: " +  str(len(tbdata))    

    # Write into the db
    print 'Loading ...'
    for i in range(len(tbdata)):
        EVENT_ID = str(tbdata[i][0])  
        time     = str(tbdata[i][1])
        RA       = str(tbdata[i][2])
        DEC      = str(tbdata[i][3])
        ENERGY   = str(tbdata[i][4])
        DETX     = str(tbdata[i][5])
        DETY     = str(tbdata[i][6])
        MC_ID    = str(tbdata[i][7])
        #strValue = '(null, ' + time + ', ' + RA + ', ' + DEC + ', ' + ENERGY + ', ' + DETX + ', ' + DETY + ', ' + MC_ID + ')'
        strValue = '(' + EVENT_ID + ', ' + time + ', ' + RA + ', ' + DEC + ', ' + ENERGY + ', ' + DETX + ', ' + DETY + ', ' + MC_ID + ')' 
        sql = 'INSERT INTO evt3  VALUES' + strValue
        cur.execute(sql)
    db.commit()
    print 'Done.'
    db.close()
