import unittest
import app
class TestCheckPasswordStrength(unittest.TestCase):
    
    def test_password_length(self):
        self.assertEqual(app.check_password_strength("213"),False)
        self.assertEqual(app.check_password_strength(""),False)
        self.assertEqual(app.check_password_strength("Welcomeldfasl"),False)
    def test_password_specialchar(self):
        self.assertEqual(app.check_password_strength("4839djsja"),False)
        self.assertEqual(app.check_password_strength("4839323432"),False)
        self.assertEqual(app.check_password_strength("Welcome@123"),True)
    def test_password_isnull(self):
        self.assertEqual(app.check_password_strength(None),False)
    def test_password_hasnumbers(self):
        self.assertEqual(app.check_password_strength("sabncsmcoscsa"),False)
        self.assertEqual(app.check_password_strength("@sabncsmco123"),True)
        
if __name__=='__main__':
    unittest.main()