import unittest

def DtB(decimal):
    binary = bin(decimal).replace("0b", "")
    return binary

def DtH(decimal):
    hexadecimal = hex(decimal).replace("0x", "")
    return hexadecimal

def DtO(decimal):
    octal = oct(decimal).replace("0o", "")
    return octal



####################################################
#TEST

class TestDecimalBinario(unittest.TestCase):
    def test1(self):
        result = DtB(20)
        self.assertEqual(result, "10100")
        
class TestDecimalBinario(unittest.TestCase):
    def test1(self):
        result = DtH(20)
        self.assertEqual(result, "14")
        
class TestDecimalBinario(unittest.TestCase):
    def test1(self):
        result = DtO(20)
        self.assertEqual(result, "24")
        


if __name__ == '__main__':
    unittest.main()
