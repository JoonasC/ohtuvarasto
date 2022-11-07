import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uuden_varaston_luominen_negativiisella_tilavuudella_aiheuttaa_tilavuuden_nollautumisen(self):
        varasto = Varasto(-1)

        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_uuden_varaston_luominen_negatiivisella_saldolla_aiheuttaa_saldon_nollautumisen(self):
        varasto = Varasto(0, -1)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_uuden_varaston_luominen_saldolla_joka_ylittaa_tilavuuden_aiheuttaa_ylimaaran_hukkaantumisen(self):
        varasto = Varasto(10, 15)

        self.assertAlmostEqual(varasto.saldo, varasto.tilavuus)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivisen_maaran_lisays_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_tilavuuden_ylittavan_maaran_lisaaminen_aiheuttaa_ylimaaran_hukkaantumisen(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivisen_maaran_ottaminen_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_saldon_ylittavan_maaran_ottaminen_ei_aiheuta_negatiivista_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(saatu_maara, 8)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varaston_palauttama_teksti_on_oikein(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        self.assertEqual(str(self.varasto), "saldo = 6, vielä tilaa 4.")
