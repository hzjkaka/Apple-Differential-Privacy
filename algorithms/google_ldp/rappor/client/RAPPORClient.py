from algorithms.google_ldp.rappor.client.rappor import Encoder, SecureIrrRand


class RAPPORClient:
    def __init__(self, cohort, params):
        self.cohort = cohort
        self.params = params
        self.encoder = Encoder(self.params, self.cohort, "secret", SecureIrrRand(self.params))

    def generate_report(self, data):
        return (self.encoder.encode(data), self.cohort)
