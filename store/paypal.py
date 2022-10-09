import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AbAhm7EMXRO2kAOEyrwdY7cvLRouUYKqujnthC4e2VKIE4kC-0Xc4f6Oh39WgC5G3_LwZ0GOuo0zn0vd"
        self.client_secret = "EDedj6sRZnSWGYmYjs3TgXtnEu2rnQEfY-fz2q_2r0vbFXSJ_39wf-pGQeMFLyg2du_Lkb_q-s8fDNZy"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)