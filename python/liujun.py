#!/usr/bin/python
from __future__ import division  

import math

for i in range(1,10000):
    for j in range(1,10000):
        for k in range(1,10000):
            result1 = i/(j+k)+j/(i+k)+k/(i+j)
            if result1 < 4.00000001 and  result1 > 3.99999999 :
                print i,j,k, result1
            
              