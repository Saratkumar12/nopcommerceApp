import pytest

class TestFixpractice:

    @pytest.fixture(scope="module")
    def test_before_testrun(self):
        print("run autosue=ture method")


    def test_testrun_test2(self):
        print("testcase 2 is pass")


    def test_testrun_test3(self):
         print("testcase 3 is pass")


    def test_testrun_test4(self):
        print("testcase 4 is pass")
