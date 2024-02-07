# SPDX-FileCopyrightText: 2024 Daniel Aimé Valcour <fosssweeper@gmail.com>
#
# SPDX-License-Identifier: MIT

import mean.py
import math

def trimmed_mean(percent_trim, data):
    trim = percent_trim / 100
    data.sort()
    trim_count = math.floor(len(data) * trim)
    assert trim_count * 2 < len(data)
    total = 0
    trimmed_mean = mean(data[trim_count:len(data)-trim:1])
    return trimmed_mean