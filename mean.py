# SPDX-FileCopyrightText: 2024 Daniel Aimé Valcour <fosssweeper@gmail.com>
#
# SPDX-License-Identifier: MIT

def mean(data):
    total = 0
    for value in data:
        total += value
    mean = total / len(data)
    return mean