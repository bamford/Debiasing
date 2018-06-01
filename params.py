data_file = '/home/ppzsb1/Dropbox/Work/notebooks/gz_nsa/nsa_debiased.csv'
output_directory = '/home/ppzsb1/Dropbox/Work/notebooks/gz_nsa/debias/'

logistic_bounds = ((0.05, 100), (-100, 100))
exponential_bounds = ((10**(-10), 1000), (10**(-10), 1000))

log_fv_range = (-1.5, 0.01)
count_suffix = '_weight'
fraction_suffix = '_weight_fraction'

Mr_column = 'r_mag'
R50_column = 'R_50_kpc'
z_column = 'z'

n_voronoi = 30
n_per_z = 50
low_signal_limit = 100
clip_percentile = 5

volume_redshift_limits = (0.03, 0.15)
survey_mag_limit = 18.5
