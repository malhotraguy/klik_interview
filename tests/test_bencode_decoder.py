import unittest
#  coverage run --omit="venv/*","tests/*" -m pytest
from bencode_decoder import bencode_decoder


class TestSuiteBencodeDecoder(unittest.TestCase):
    def test_bencode_decoder_int(self):
        bencode_data = "i4223e"
        decoded_value, bencode_data = bencode_decoder(bencode_data=bencode_data)
        self.assertEqual(decoded_value, 4223)
        self.assertEqual(bencode_data, "")

    def test_bencode_decoder_string(self):
        bencode_data = "8:robots54"
        decoded_value, bencode_data = bencode_decoder(bencode_data=bencode_data)
        self.assertEqual(decoded_value, "robots54")
        self.assertEqual(bencode_data, "")

    def test_bencode_decoder_list(self):
        bencode_data = "l5:green3:red4:bluee"
        decoded_value, bencode_data = bencode_decoder(bencode_data=bencode_data)
        self.assertEqual(decoded_value, ["green", "red", "blue"])
        self.assertEqual(bencode_data, "")
        bencode_data = "l4:spami42ee"
        decoded_value, bencode_data = bencode_decoder(bencode_data=bencode_data)
        self.assertEqual(decoded_value, ["spam", 42])
        self.assertEqual(bencode_data, "")

    def test_bencode_decoder_dictionary(self):
        bencode_data = "d3:bar4:spam3:fooi42ee"
        decoded_value, bencode_data = bencode_decoder(bencode_data=bencode_data)
        self.assertEqual(decoded_value, {"bar": "spam", "foo": 42})
        self.assertEqual(bencode_data, "")
