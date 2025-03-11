import unittest
from cancer_prediction.cancer_model import CancerModel

class TestCancerModel(unittest.TestCase):
    def test_diagnosis_to_target(self): # same name as function we are testing
        model = CancerModel() # instantiate cancer model
        diagnosis = "Malignant"

        target = model.diagnosis_to_target(diagnosis) # call function we are testing
        self.assertEqual(target, 0) # check if the function returns the expected value of 0 for malignant

        # assertEqual is a method from the unittest.TestCase class that checks if the two values are equal
        # If the values are equal, the test passes. If they are not equal, the test fails.

if __name__ == '__main__':
    unittest.main()
# The test_diagnosis_to_target function tests the diagnosis_to_target method of the CancerModel class.
# The test checks if the method correctly maps the diagnosis "Malignant" to the target value 0.