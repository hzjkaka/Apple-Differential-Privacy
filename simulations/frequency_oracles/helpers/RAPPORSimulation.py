import numpy as np

from algorithms.google_ldp.rappor.server.RAPPORServer import RAPPORServer
from collections import Counter

from simulations.frequency_oracles.helpers.FrequencyOracleSimulation import FrequencyOracleSimulation


class RAPPORSimulation(FrequencyOracleSimulation):
    def __init__(self, params):
        super().__init__()
        self.num_bloombits = params["num_bloombits"]
        self.num_hashes = params["num_hashes"]
        self.num_of_cohorts = params["num_of_cohorts"]
        self.prob_p = params["prob_p"]
        self.prob_q = params["prob_q"]
        self.prob_f = params["prob_f"]

        self.name = "RAPPOR"

    def run(self, data, domain):
        # -------------------- Simulating the client and server-side process --------------------

        rappor_server = RAPPORServer(self.num_bloombits,
                                     self.num_hashes, self.num_of_cohorts,
                                     [self.prob_p, self.prob_q, self.prob_f])

        for i in range(0, len(data)):
            rappor_client = rappor_server.init_client_instance(np.random.randint(0, self.num_of_cohorts - 1))
            rappor_server.add_report(rappor_client.generate_report(str(data[i])))

        hist = rappor_server.generate_freq_hist(list(map(str, domain)))

        print(hist)

        ldp_plot_data = np.zeros(len(domain))
        for row in hist.values.tolist():
            ldp_plot_data = np.append(ldp_plot_data, [int(row[0])] * int(row[1]))

        return ldp_plot_data