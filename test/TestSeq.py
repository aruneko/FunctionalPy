import unittest

from functionalpy.Seq import Seq


class TestSeq(unittest.TestCase):
    def test_functor_1st_low(self):
        seq = Seq(1, 2, 3, 4, 5)

        def identity(x):
            return x

        self.assertEqual(seq.map(identity), identity(seq))

    def test_functor_2nd_low(self):
        seq = Seq(1, 2, 3, 4, 5)

        def f(x):
            return x + 1

        def g(x):
            return x * 2

        self.assertEqual(seq.map(lambda x: f(g(x))), seq.map(g).map(f))

    def test_applicative_1st_low(self):
        seq = Seq(1, 2, 3, 4, 5)

        def f(x):
            return x + 1

        self.assertEqual(seq.ap(Seq(f)), seq.map(f))

    def test_applicative_2nd_low(self):
        seq = Seq(1, 2, 3, 4, 5)

        def identity(x):
            return x

        self.assertEqual(seq.ap(Seq(identity)), seq)

    def test_monad_1st_low(self):
        seq = Seq(1)

        def f(x):
            return Seq(x + 1)

        self.assertEqual(seq.flat_map(f), f(1))

    def test_monad_2nd_low(self):
        seq = Seq(1, 2, 3, 4, 5)

        self.assertEqual(seq.flat_map(Seq), seq)

    def test_monad_3rd_low(self):
        seq = Seq(1, 2, 3, 4, 5)

        def f(x):
            return Seq(x + 1)

        def g(x):
            return Seq(x * 2)

        self.assertEqual(seq.flat_map(f).flat_map(g), seq.flat_map(lambda x: f(x).flat_map(g)))


if __name__ == '__main__':
    unittest.main()
