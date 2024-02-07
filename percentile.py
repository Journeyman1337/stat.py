# SPDX-FileCopyrightText: 2024 Daniel Aimé Valcour <fosssweeper@gmail.com>
#
# SPDX-License-Identifier: MIT

import math
def percentile(values, percentile):
    values.sort()
    L = (percentile / 100) * len(values)
    L = math.ceil(L)
    return values[int(L)]