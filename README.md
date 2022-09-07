# ML challenge for WL cosmology

We describe  a simulation based challenge designed to test and validate field level inference methods for weak lensing cosmology. These include deep learning methods such as CNNs and Bayesian Hierarchical Methods. The challenge is also available for a variety of non-Gaussian statistics. Our goal is to enable groups with varying levels of expertise in lensing and cosmology to develop, test and validate their codes and to help the cosmology community  evaluate their performance. The challenge will comprise a learning phase and a blind challenge phase. We describe the simulation products and the sources of systematic uncertainties included. 

 Here we present the learning phase A. In the future learning phase B  and the (blind) challenge phase will be available. For more details, see: https://www.overleaf.com/read/thwkhkvvwxyv

# LEARNING PHASE A

 
*Map 1 [data/learning_phase_A/convergence_noiseless.h5]*

*Shear Catalogue 1 [to be uploaded; send me an email if you need it]*

Noiseless convergence map. The map comes in healpy format, with NSIDE=1024 (equivalent to a pixel resolution of ~3.4 arcmin). A short snippet to read the maps is provided in the utils/ folder.  The unmasked part of the map spans ~1100 deg^2. 2D projections of the map can be obtained, e.g., using the healpy gnomview functionality (https://healpy.readthedocs.io/en/latest/generated/healpy.visufunc.gnomview.html). Users may split the map into subpatches of desired area to run their analysis. A shear catalogue is also provided, where the (noiseless) shear field is sampled using randomly distributed galaxies with n_density = 2.5 gal/arcmin^2.

The input cosmology for the map is: \Omega_m = 0.3071; \sigma_8 = 0.8228;  n_s = 0.96; \Omega_b = 0.048; h_100 = 0.677. The map has been obtained from one N-body simulation (900^3 particles, 600 Mpc/h box size), integrating 200 full-sky snapshots between z=49 and z=0, using the code PKDGRAV. The redshift distribution is provided in the data folder.

![alt text](https://github.com/mgatti29/ML_challenge_cosmology/blob/main/data/figures/noiseless_k.png?raw=true)


*Map 2 [data/learning_phase_A/convergence_noisely.h5]*

*Shear Catalogue 2 [to be uploaded; send me an email if you need it]*


Noisy convergence map. The map comes in healpy format, with NSIDE=1024 (equivalent to a pixel resolution of ~3.4 arcmin).  The unmasked part of the map spans ~1100 deg^2. Shape noise is added assuming std_e = 0.28 and n_density = 2.5 gal/arcmin^2. 2D projections of the map can be obtained, e.g., using the healpy gnomview functionality (https://healpy.readthedocs.io/en/latest/generated/healpy.visufunc.gnomview.html). Users may split the map into subpatches of desired area to run their analysis. A shear catalogue is also provided, where the (noisy) shear field is sampled using randomly distributed galaxies with n_density = 2.5 gal/arcmin^2.

The input cosmology for the map is: \Omega_m = 0.3071; \sigma_8 = 0.8228;  n_s = 0.96; \Omega_b = 0.048; h_100 = 0.677. The map has been obtained from one N-body simulation (900^3 particles, 600 Mpc/h box size), integrating 200 full-sky snapshots between z=49 and z=0, using the code PKDGRAV. The redshift distribution is provided in the data folder.


![alt text](https://github.com/mgatti29/ML_challenge_cosmology/blob/main/data/figures/noisy_k.png?raw=true)


Issues and Questions
Please create an issue or email mgatti@sas.upenn.edu or bjain@physics.upenn.edu with any questions or requests.
