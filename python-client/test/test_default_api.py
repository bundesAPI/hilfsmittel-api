"""
    Hilfsmittel-API

    Der GKV-Spitzenverbund führt ein Register über alle Hilfsmittel, die der Leistungspflicht der Kassen unterliegen. Struktur: Produktgruppe -> Anwendungsort -> Untergruppe -> Produktart -> Produkt  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.hilfsmittel.api.default_api import DefaultApi  # noqa: E501

from deutschland import hilfsmittel


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_nachweisschema_id_get(self):
        """Test case for nachweisschema_id_get

        Details zu einem Nachweisschema abfragen  # noqa: E501
        """
        pass

    def test_produkt_get(self):
        """Test case for produkt_get

        Kompaktliste aller Produkte  # noqa: E501
        """
        pass

    def test_produkt_id_get(self):
        """Test case for produkt_id_get

        Details zu einem Produkt abfragen  # noqa: E501
        """
        pass

    def test_produktart_id_get(self):
        """Test case for produktart_id_get

        Details zu einer Produktart abfragen  # noqa: E501
        """
        pass

    def test_produktgruppe_id_get(self):
        """Test case for produktgruppe_id_get

        Details zu einer Produktgruppe abfragen  # noqa: E501
        """
        pass

    def test_untergruppe_id_get(self):
        """Test case for untergruppe_id_get

        Details zu einer Untergruppe abfragen  # noqa: E501
        """
        pass

    def test_verzeichnis_tree_level_get(self):
        """Test case for verzeichnis_tree_level_get

        Lädt alle Knoten im Produktbaum bis zum gegebenen Level.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()