# SPDX-FileCopyrightText: 2024 Daniel Aimé Valcour <fosssweeper@gmail.com>
#
# SPDX-License-Identifier: MIT

def missing_value_from_mean(known_values, mean):
    known_total = sum(known_values)
    missing_value = (mean * (len(known_values) + 1)) - known_total
    return missing_value