import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_saldo_vahenee_jos_kortilla_rahaa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_saldo_sama_jos_kortilla_ei_rahaa(self):
        self.maksukortti.ota_rahaa(10000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_metodi_true_jos_kortilla_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)

    def test_metodi_false_jos_kortilla_ei_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10000), False)

    def test_maksukorttilla_oikea_tuloste(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")