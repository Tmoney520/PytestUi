# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/25 23:09
#  :TGW
"""

import os
import pytest

def run():
    pytest.main(['-v','--alluredir','./report/result','--clean-alluredir','--allure-no-capture'])
    os.system('allure generate ./report/result/ -o ./report/report_allure/ --clean')

if __name__ == '__main__':
    run()