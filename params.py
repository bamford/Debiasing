data_file = '/Volumes/SD_Extra/galaxy_zoo_nsa_matching/debias/nsa_to_debias_with_fractions.csv'
output_directory = '/Volumes/SD_Extra/galaxy_zoo_nsa_matching/debias/'

logistic_bounds = ((0.5, 10), (-10, 10))
exponential_bounds = ((10**(-5), 10), (10**(-5), 10))

log_fv_range = (-1.5, 0.01)
count_suffix = '_weight'
fraction_suffix = '_weight_fraction'

Mr_column = 'r_mag'
R50_column = 'petroth50'
z_column = 'z'

n_voronoi = 30
n_per_z = 50
low_signal_limit = 100
clip_percentile = 5

volume_redshift_limits = (0.03, 0.10)
survey_mag_limit = 19.8
