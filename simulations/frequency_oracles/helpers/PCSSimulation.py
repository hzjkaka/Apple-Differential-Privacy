import numpy as np

from algorithms.bnst_ldp.TreeHistogram.PrivateCountSketch import PrivateCountSketch
from collections import Counter

from simulations.frequency_oracles.helpers.FrequencyOracleSimulation import FrequencyOracleSimulation


class PCSSimulation(FrequencyOracleSimulation):
    def __init__(self, params, use_median=False):
        super().__init__()
        self.l = params["l"]
        self.w = params["w"]
        self.epsilon = params["epsilon"]
        self.use_median = use_median
        self.name = "priv_count_sketch"

    def run(self, data, domain):
        # -------------------- Simulating the client-side process --------------------
        ldp_data = []

        priv_count_sketch = PrivateCountSketch(self.l, self.w, self.epsilon, use_median=self.use_median)

        for i in range(0, len(data)):
            priv_count_sketch.set_sketch_element(str(data[i]))

        # -------------------- Simulating the server-side process --------------------

        ldp_freq = np.empty(len(domain))
        ldp_plot_data = np.empty(len(domain))

        # Generate both frequency data from the oracle and plot data to be graphed
        for i, item in enumerate(domain):
            ldp_freq[i] = priv_count_sketch.freq_oracle(str(item)) # Freq Oracle
            ldp_plot_data = np.append(ldp_plot_data, [item]*int(round(ldp_freq[i]))) # Generate estimated dataset

        return ldp_plot_data