# SPDX-FileCopyrightText: 2024 Daniel Aimé Valcour <fosssweeper@gmail.com>
#
# SPDX-License-Identifier: MIT

def midpoints(data):
    midpoints = [(data[i] + data[i+1] / 2) for i in range(len(data) - 1)]
    return midpoints