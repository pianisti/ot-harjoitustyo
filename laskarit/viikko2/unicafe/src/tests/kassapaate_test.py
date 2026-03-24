import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksu = 1000
        self.maksukortti = Maksukortti(1000)

    def test_kassapaate_luotu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisen_kateismaksu_riittaa(self):
        self.kassapaate.syo_edullisesti_kateisella(self.maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisen_kateismaksu_riittaa_ja_oikeat_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(self.maksu), self.maksu - 240)

    def test_edullisen_kateismaksu_riittaa_ja_lounasmaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(self.maksu)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_kateismaksu_ei_riita(self):
        maksu = 100
        self.kassapaate.syo_edullisesti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(maksu), maksu)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_kateismaksu_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(self.maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaan_kateismaksu_riittaa_ja_oikeat_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(self.maksu), self.maksu - 400)

    def test_maukkaan_kateismaksu_riittaa_ja_lounasmaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(self.maksu)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_kateismaksu_ei_riita(self):
        maksu = 100
        self.kassapaate.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(maksu), maksu)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_korttimaksu_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)

    def test_edullisen_korttimaksu_riittaa_ja_lounasmaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_korttimaksu_ei_riita(self):
        maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_korttimaksu_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)

    def test_maukkaan_korttimaksu_riittaa_ja_lounasmaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_korttimaksu_ei_riita(self):
        maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassan_rahamaara_sama_korttimaksu_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_lataa_kortille_rahaa_ja_kassa_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001.0)
        self.assertEqual(self.maksukortti.saldo_euroina(), 11.0)