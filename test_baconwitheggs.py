try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '../src'
            )
        )
    )
except ImportError:
    raise


from src.baconwitheggs import baconWithEggsVerifier
import unittest


class TestBaconWithEggs(unittest.TestCase):
    def test_should_return_assertion_error(self):
        with self.assertRaises(AssertionError):
            baconWithEggsVerifier('a')

    def test_multipleVerifier_should_return_Bacon_com_ovos(self):
        inputs = ((15), (30), (45), (60), (75), (90), (105), (120),
                  (135), (150), (165), (180), (195), (210), (225),
                  (240), (255), (270), (285), (300), (315), (330),
                  (345))
        output = "Bacon com ovos!"
        for input in inputs:
            with self.subTest(input=input, output=output):
                self.assertEqual(baconWithEggsVerifier(
                    input), output, msg=f"{input} não retornou {output}")

    def test_multipleVerifier_should_return_Bacon(self):
        inputs = ((3), (6), (9), (12), (18), (21), (24), (27), (33), (36),
                  (39), (42), (48), (51), (54), (57), (63), (66), (69),
                  (72), (78), (81), (84), (87))
        output = "Bacon!"
        for input in inputs:
            with self.subTest(input=input, output=output):
                self.assertEqual(baconWithEggsVerifier(
                    input), output, msg=f"{input} não retornou {output}")

    def test_multipleVerifier_should_return_Ovos(self):
        inputs = ((5), (10), (20), (25), (35), (40), (50), (55), (65), (70),
                  (80), (85), (95), (100), (110), (115), (125), (130),
                  (140), (145))
        output = "Ovos!"
        for input in inputs:
            with self.subTest(input=input, output=output):
                self.assertEqual(baconWithEggsVerifier(
                    input), output, msg=f"{input} não retornou {output}")

    def test_multipleVerifier_should_return_Passara_fome(self):
        inputs = ((1), (2), (4), (7), (8), (11), (13), (14), (16), (17),
                  (19), (22), (23), (26), (28), (29), (31), (32), (34),
                  (37), (38), (41), (43), (44), (46), (47), (49), (52),
                  (53), (56), (58), (59), (61), (62), (64), (67), (68),
                  (71), (73), (74), (76), (77), (79), (82), (83), (86),
                  (88), (89), (91), (92), (94), (97), (98))
        output = "Passou Fome!"
        for input in inputs:
            with self.subTest(input=input):
                self.assertEqual(baconWithEggsVerifier(
                    input), output, msg=f"{input} não retornou {output}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
