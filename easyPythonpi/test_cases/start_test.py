import os
def test_all():
  os.system("python3 basics_test.py")
  os.system("python3 graph_test.py")
  os.system("python3 search_test.py")
  os.system("python3 TestBin2Hex.py")
  os.system("python3 TestFibRefactored.py")
  return "ok"
  
#test all methods  
test_all()

