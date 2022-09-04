import healpy as hp
import h5py

file_ = h5py.File('../data/learning_phase_A//convergence_noisy.h5','r')
map_ = np.zeros(hp.nside2npix(1024))
map_[np.array(file_['PIX'])] = np.array(file_['convergence'])
file_.close()
