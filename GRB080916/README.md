# CTA simulations of GRB 080916

* The event list of GRB 080916 has been simulated with ctools.
* The input light curve and spectrum are taken from
the Thomas Gasparetto's GRB database.
* The light curve is provided as a fits file and the spectrum as an ASCII file.
In this way both can be obtained from numerical simulations (i.e. not from anlaytical functions)

Below follows the list and explanations of all the files contained in this directory.

Input model XML file
* GRB080916009.xml

Input for ctobssim

* lightcrv_GRB080916009.fits
  * Lightcurve in fits format, build from an ascii file with time in the first column in units of seconds and normalization in the second column (maximum is 1, minimimum is 0).


* GRB080916009.out
  * Spectrum in ASCII format, with increasing energies in MeV units in the first column and ph/cm2/s/MeV (with 1 GeV step) flux in the second column



Output files:

* events.fits
* ctobssim.log


### Event file analysis results:

To check the simulated event list, a spectrum and a light curve
can be extracted with cslighv and csspec, respectively,
and plotted with show_lightcurve.py and show_spectrum.py, respectively.

* Output from cslighv:
  * lightcurve.fits
  * cslightcrv.log


* Plotting the lightcurve
  * show_lightcurve.py
  * lc.png


* Output from csspec
  * spectrum.fits
  * csspec.log


* Plotting the spectrum
  * show_spectrum.py
  * spectrum.png

* 3D cube from ctbin
  * cntcube.fits
  * ctbin.log
