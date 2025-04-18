'''
sample_pac/ab/__init__.py
from sample_pac.ab import *

sample_pac/ab/a.py
sample_pac/ab/b.py
'''

__all__ = ['a'] # * 로 import 할때 적용되는 범위를 지정
print('sample_pac 패키지 안의 ab 패키지를 로드 했습니다.')