import h5py
import criticality
import statistics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

figure_directory = '/home/jja34/public_html/Figures/' 
data_directory = '/work/imaging8/jja34/ECoG_Study/ECoG_Data/'
filter = 'filter_FIR_513_blackmanharris'

monkeys = ('A', 'K1')
bands = ('beta', 'alpha', 'theta', 'delta')
recordings = range(5)
methods = (('events', 1), ('displacements', 2), ('amplitudes', 3), ('amplitude_aucs', 4))
for monkey in monkeys:
    for band in bands:
        for i in recordings:
            f = h5py.File(data_directory+'Monkey_'+monkey+'.hdf5')
            data = f['food_tracking'+str(i)+'/'+filter+'/'+band]
            d = criticality.avalanche_analysis(data, bin_width=3)
        
            for method, fig in methods:
                X = d['size_'+method]
                plt.figure(fig)
                statistics.hist_log(X, X.max(), X.min())
                plt.xlabel('Size ('+method+')', fontsize='xx-large')
                plt.ylabel('P(Size)', fontsize='xx-large')
                plt.savefig(figure_directory+band+'_'+method+'_'+monkey)