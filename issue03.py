from typing import List, Tuple
import unittest

def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class Tests(unittest.TestCase):
    def test_eq(self):
        res = fit_transform(list("sos"))
        exp = [("s", [0, 1]), ("o", [1, 0]), ("s", [0, 1])]
        self.assertEqual(res, exp)

    def test_eq2(self):
        res = fit_transform(list("vl"))
        exp = [("v", [0, 1]), ("l", [1, 0])]
        self.assertEqual(res, exp)

    def test_notin(self):
        res = fit_transform(list("wa"))
        exp = [("w", [1, 0]), ("a", [0, 1])]
        self.assertNotIn(res, exp)

    def test_except(self):
        self.assertRaises(TypeError, fit_transform)


if __name__ == "__main__":
    unittest.main()
