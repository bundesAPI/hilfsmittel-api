"""
    Hilfsmittel-API

    Der GKV-Spitzenverbund führt ein Register über alle Hilfsmittel, die der Leistungspflicht der Kassen unterliegen. Struktur: Produktgruppe -> Anwendungsort -> Untergruppe -> Produktart -> Produkt  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.hilfsmittel.model.nachweisschema_nachweis_abschnitt_anforderungen_inner_abschnitt_anforderungen_inner import (
    NachweisschemaNachweisAbschnittAnforderungenInnerAbschnittAnforderungenInner,
)

from deutschland import hilfsmittel

globals()[
    "NachweisschemaNachweisAbschnittAnforderungenInnerAbschnittAnforderungenInner"
] = NachweisschemaNachweisAbschnittAnforderungenInnerAbschnittAnforderungenInner
from deutschland.hilfsmittel.model.nachweisschema_nachweis_abschnitt_anforderungen_inner import (
    NachweisschemaNachweisAbschnittAnforderungenInner,
)


class TestNachweisschemaNachweisAbschnittAnforderungenInner(unittest.TestCase):
    """NachweisschemaNachweisAbschnittAnforderungenInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNachweisschemaNachweisAbschnittAnforderungenInner(self):
        """Test NachweisschemaNachweisAbschnittAnforderungenInner"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NachweisschemaNachweisAbschnittAnforderungenInner()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
