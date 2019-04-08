#!/usr/bin/env python3.7

import hashlib
from pylab import *

dt = genfromtxt("../data/tb_1030id.csv",dtype = str, delimiter = ',')
print(dt.shape)
print(dt[1:5,])

hashid = []
for i in range(len(dt[:,0])):
    hashid.append(hashlib.md5(dt[i,0].encode()).hexdigest())
print(hashid[:10])

f = open('../data/tb_1030hashed.csv', 'a')
for i in range(dt.shape[0]):
    f.write('%s\t' % dt[i,0])
    f.write('%s\t' % dt[i,1])
    f.write('%s\t' % dt[i,2])
    f.write('%s\n' % hashid[i])
f.close()
