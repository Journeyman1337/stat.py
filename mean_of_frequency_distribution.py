# SPDX-FileCopyrightText: 2024 Daniel Aimé Valcour <fosssweeper@gmail.com>
#
# SPDX-License-Identifier: MIT

import midpoints.py

def mean_of_frequency_distribution(frequencies):
    midpoints = midpoints(data)
    assert len(frequencies) == len(midpoints)
    total = 0
    for i in range(0, len(frequencies)):
        total += midpoints[i] * frequencies[i]
    total /= sum(frequencies)
    return total