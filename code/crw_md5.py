#!/usr/bin/env python3.7

import hashlib

hotellist = [b'479628', b'16197084', b'22755589', b'393916', b'387009',
 b'2608420', b'427622', b'473770', b'436187', b'1073814', b'5926952', 
 b'21349561', b'4399431', b'441607', b'441585', b'374487', b'6874402', 
 b'15018773', b'15018492', b'427259', b'430295', b'14074638', b'456909', 
 b'1496646', b'12782071']
for id in hotellist:
    result = hashlib.md5(id)
    print(result.hexdigest())
