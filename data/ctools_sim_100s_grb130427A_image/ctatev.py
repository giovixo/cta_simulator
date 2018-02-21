
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

    # Write into the db
    for i in range(10):
        time    = str(tbdata[i][1])
        RA      = str(tbdata[i][2])
        DEC     = str(tbdata[i][3])
        ENERGY  = str(tbdata[i][4])
        DETX    = str(tbdata[i][5])
        DETY    = str(tbdata[i][6])
        MC_ID   = str(tbdata[i][7])
        strValue = '(null, ' + time + ', ' + RA + ', ' + DEC + ', ' + ENERGY + ', ' + DETX + ', ' + DETY + ', ' + MC_ID + ')'
        strValue = '(null, ' + str(0.1*i) + ', ' + str(1. + i) + ', ' + str(2. + i) + ', ' + str(3. + i) + ', ' + str(4. + i) + ', ' + str(5. + i) + ', 1)'
        sql = 'INSERT INTO evt3  VALUES' + strValue
        cur.execute(sql)

    # Close the connection
    db.commit()
    db.close()
