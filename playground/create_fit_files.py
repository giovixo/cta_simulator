import numpy as np
from astropy.io import fits

hdu = fits.PrimaryHDU()
hdu.data = np.random.random((20,2))
# Add a keyworld
hdu.header['telescop'] = 'Python Observatory'
# write the fit file
hdu.writeto('random_array.fits', overwrite=True)
