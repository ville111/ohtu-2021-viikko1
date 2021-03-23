import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def testi_konstruktori_liian_pieni_saldo(self):
        varasto1 = Varasto(10, -10)
        self.assertAlmostEqual(varasto1.saldo, 0)
        
    def testi_konstruktori_liian_pieni_tilavuus(self):
        varasto1 = Varasto(-10)
        self.assertAlmostEqual(varasto1.tilavuus, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ota_varastosta_negatiivinen(self):
        
        self.assertAlmostEqual(self.varasto.ota_varastosta(-10), 0.0)

    def test_ota_varastosta_liikaa(self):
       # mikä tässä mättää? Eikö saldon pitäisi olla 10?
        self.assertAlmostEqual(self.varasto.ota_varastosta(300),0.0)

    def test_lisaa_negatiivinen_varastoon(self):
        maara = 10
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), maara)

    def test_lisaa_liikaa_varastoon(self):

        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test__str__(self):
        self.assertAlmostEqual(self.varasto.__str__(), f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")



