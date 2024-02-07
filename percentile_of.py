# SPDX-FileCopyrightText: 2024 Daniel Aimé Valcour <fosssweeper@gmail.com>
#
# SPDX-License-Identifier: MIT

def percentile_of(value, data):
    number_less_than = 0
    for rate in rates:
        if rate < value:
            number_less_than+=1
    result = (number_less_than / len(rates)) * 100
    return result