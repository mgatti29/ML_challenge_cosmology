# ML challenge cosmology

This data challenge is designed to test and validate field level inference methods for weak lensing cosmology. These include deep learning methods such as CNNs and Bayesian Hierarchical Methods. The goal is to enable groups with varying levels of expertise in lensing and cosmology develop, test and validate their codes and to help the cosmology community evaluate their performance. The challenge will comprise a learning phase and a blind challenge phase. Here we present the learning phase. 


*Map 1 [data/noiseless_patches.h5]*

Noiseless convergence maps, flat-sky. 20 realisations are available. The maps are 128x128 pixles, and the pixel size is 3.435 arcminute. The input cosmology for the map is: \Omega_m = 0.3071; \sigma_8 = 0.8228;  n_s = 0.96; \Omega_b = 0.048; h_100 = 0.677. The map has been obtained from one N-body simulation (900^3 particles, 600 Mpc/h box size), integrating 200 full-sky snapshots between z=49 and z=0, using the code PKDGRAV. The redshift distribution is provided in the data folder.

![alt text](https://github.com/mgatti29/ML_challenge_cosmology/blob/main/data/figures/noiseless_k.png?raw=true)


*Map 2 [data/noisy_patches.h5]*

Noisy convergence maps, flat-sky. 20 realisations are available. The maps are 128x128 pixles, and the pixel size is 3.435 arcminute. The input cosmology for the map is: \Omega_m = 0.3071; \sigma_8 = 0.8228;  n_s = 0.96; \Omega_b = 0.048; h_100 = 0.677. The map has been obtained from one N-body simulation (900^3 particles, 600 Mpc/h box size), integrating 200 full-sky snapshots between z=49 and z=0, using the code PKDGRAV. The redshift distribution is provided in the data folder. Shape noise is added assuming std_e = 0.28 and n_density = 2.5 gal/arcmin^2


![alt text](https://github.com/mgatti29/ML_challenge_cosmology/blob/main/data/figures/noisy_k.png?raw=true)


Issues and Questions
Please create an issue or email mgatti@sas.upenn.edu or bjain@physics.upenn.edu with any questions or requests.
