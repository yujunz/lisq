import botnus.query as query
from deepdiff import DeepDiff
import unittest


class TestQuery(unittest.TestCase):
    def test_select(self):
        records = [{'a': 1, 'b': 1}, {'a': 2, 'b': 2}]
        selected = query.select(records, ['a'])
        expected = [{'a': 1}, {'a': 2}]
        self.assertEqual(DeepDiff(selected, expected), {})

    def test_select_as(self):
        records = [{'a': 1, 'b': 1}, {'a': 2, 'b': 2}]
        select_as = query.select(records, {'a': 'c'})
        expected = [{'c': 1}, {'c': 2}]
        self.assertEqual(DeepDiff(select_as, expected), {})

    def test_group_by(self):
        records = [{'a': 1}, {'a': 2}, {'a': 1}]
        groups = dict(query.group(records, 'a'))
        expected = {1: [{'a': 1}, {'a': 1}], 2: [{'a': 2}]}
        self.assertEqual(DeepDiff(groups, expected),{})

    def test_accumulate(self):
        stat = query.accumulate([{'a': 1}, {'a': 2}], ['a'])
        self.assertDictEqual(stat, {'a': 3})

    def test_join(self):
        t1 = [{'a': 1, 'b': 2}]
        t2 = [{'c': 2, 'd': 3}]
        j = query.join(t1, t2, ('b', 'c'))
        self.assertEqual(j, [{'a': 1, 'b': 2, 'c': 2, 'd': 3}], {})
