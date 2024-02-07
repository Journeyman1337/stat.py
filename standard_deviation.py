# SPDX-FileCopyrightText: 2024 Daniel Aimé Valcour <fosssweeper@gmail.com>
#
# SPDX-License-Identifier: MIT

def standard_deviation(frequencies, midpoints):
    assert len(frequencies) == len(midpoints)
    result = 0
    for i in range(0, len(frequencies)):
        result += midpoint[i] ** 2 * frequencies[i]
    subtotal = 0
    for i in range(0, len(frequencies)):
        subtotal += midpoint[i] * frequences[i]
    result *= len(frequences)
    result -= subtotal
    result /= len(frequencies) * (len(frequencies) - 1)
    return result