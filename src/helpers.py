"""
Copyright (c) 2021 Robert Bosch GmbH

All rights reserved.

This source code is licensed under the MIT license found in the LICENSE file in the root directory of this source tree.

@author: Barbara Rakitsch
"""

import numpy as np
import matplotlib.pylab as plt

def rmse(Y_true, Y_hat):
    """
    returns root mean squared error

    Args:
        Y_true   :    true outputs [N,(1)]
        Y_hat    :    predicted outputs [N, (1)]
    """
    if Y_true.ndim == 2:
        Y_true = Y_true[:, 0]
    if Y_hat.ndim == 2:
        Y_hat = Y_hat[:, 0]
    return np.sqrt(np.mean((Y_true - Y_hat)**2))


def create_plot(t, y, idx_train, idx_test1, idx_test2, y_mean, y_var=None, title=None):
    """
    plots predictions

    Args:
        t         :   time [Nx1]
        y         :   observations [Nx1]
        idx_train :   training indices
        idx_test1 :   first set of test indices
        idx_test2 :   second set of test indices
        y_mean    :   mean predictions [Nx1]
        y_var     :   variance predictions [Nx1]
    """
    fig = plt.figure(figsize=(10,3))
    ax = fig.add_subplot(111)

    if y_var is not None:
        plt.fill_between(t[:,0], y_mean[:,0] - 2*np.sqrt(y_var[:,0]), y_mean[:,0] + 2*np.sqrt(y_var[:,0]), color='y', alpha=0.1)
    plt.plot(t, y_mean, color='y', linewidth=2, label='Y')

    plt.plot(t[idx_train], y[idx_train], '.', label='train')
    plt.plot(t[idx_test1], y[idx_test1], '.', label='test1')
    plt.plot(t[idx_test2], y[idx_test2], '.', label='test2')

    plt.xlabel('Time [s]')
    plt.ylabel('Y')
    if title is not None: plt.title(title)
