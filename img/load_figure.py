import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import pickle as pkl

quicksave = lambda filename: plt.savefig(filename, bbox_inches='tight')

def save_figure_obj(fig, filename):
    with open(filename, 'wb') as file:
        pkl.dump(fig, file)

def load_figure_obj(filename):
    fig = plt.figure()
    with open(filename, 'rb') as file:
        figx = pkl.load(file)
    return fig


def save_all(fig, filename):
    quicksave(filename)
    file_base = filename.split('.')[0]
    save_figure_obj(fig, file_base + "_mpl_fig.pkl")


fig = load_figure_obj('PNP_conv_2D_dofs_mpl_fig.pkl')
#fig.show();
