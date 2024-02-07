# SPDX-FileCopyrightText: 2024 Daniel Aimé Valcour <fosssweeper@gmail.com>
#
# SPDX-License-Identifier: MIT

import percentile.py

def five_number_summary(values):
    values.sort()
    return [
        values[0],
        percentile(values, 25)
        percentile(values, 50)
        percentile(values, 75),
        values[len(values) - 1]
    ]