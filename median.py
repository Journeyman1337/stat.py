# SPDX-FileCopyrightText: 2024 Daniel Aimé Valcour <fosssweeper@gmail.com>
#
# SPDX-License-Identifier: MIT

import math

def median(data)
    data.sort()
    median = data[0]
    if len(data) % 2 == 0:
        low_i = int(math.floor(len(data)-1) / 2)
        high_i = low_i + 1
        median = (data[low_i] + data[high_i]) / 2
    else:
        median_i = (len(data)-1) / 2
        median = data[median_i]
    return median