import sys
import math

F_VHI = 1.0
F_HIG = 0.8
F_MED = 0.5
F_LOW = 0.2
F_VLO = 0


def closest_fv(value):
    vals = [F_VLO, F_LOW, F_MED, F_HIG, F_VHI]
    return min(vals, key=lambda x:abs(x-value))


def generalized_bell(x, a, b, c):
    return 1 / float((1 + math.pow(abs((x-c)/float(a)), 2 * b)))


def symmetry(character):
    left_count = 0
    right_count = 0
    width = len(character[0])

    left_size = math.floor(width/float(2))
    right_size = math.ceil(width/float(2))

    for i, row in enumerate(character):
        for j, pixel in enumerate(row):
            if pixel == 0:
                if j <= left_size:
                    left_count += 1
                elif j >= right_size:
                    right_count += 1

    return left_count / float(right_count)


def width(character):
    rows = 0
    rsum = 0

    for i, row in enumerate(character):
        rows += 1
        max_row_w = 0
        row_width = 0
        for j, pixel in enumerate(row):
            if pixel == 0:
                row_width += 1
                if row_width > max_row_w:
                    max_row_w = row_width
            else:
                row_width = 0
        rsum += max_row_w

    return rsum / float(rows)


def density(character):
    count_w = 0
    count_b = 0

    for row in character:
        for pixel in row:
            if pixel == 0:
                count_b += 1
            else:
                count_w += 1

    return count_w / float(count_b)


def center(character):
    center_w = len(character[0]) / 2
    center_h = len(character) / 2

    return character[center_h][center_w] == 0


def fuzzy_symmetry(sym):
    result = generalized_bell(sym, 0.2, 1, 1)
    return closest_fv(result)


def fuzzy_width(wid):
    result = generalized_bell(wid, 1, 1, 6)
    return closest_fv(result)


def fuzzy_density(den):
    result = generalized_bell(den, 0.3, 1, 0.85)
    return closest_fv(result)


def fuzzify(character):
    sym_val = symmetry(character)
    wid_val = width(character)
    den_val = density(character)

    sym = fuzzy_symmetry(sym_val)
    wid = fuzzy_width(wid_val)
    den = fuzzy_density(den_val)
    cen = center(character)

    return sym, wid, den, cen


def defuzzify(sym, den, wid, cen):
    print sym, den, wid, cen
    if sym == F_HIG and den == F_HIG and wid == F_VHI:
        if cen:
            return 8
        else:
            return 0
    if sym == F_HIG and den == F_LOW and wid == F_LOW:
        return 1
    if sym == F_MED and den == F_MED and wid == F_HIG:
        return 2
    if sym == F_LOW and den == F_MED and wid == F_MED:
        return 3
    if sym == F_LOW and den == F_LOW and wid == F_HIG:
        return 4
    if sym == F_MED and den == F_MED and wid == F_MED:
        return 5
    if sym == F_MED and den == F_HIG and wid == F_HIG:
        return 6
    if sym == F_MED and den == F_MED and wid == F_LOW:
        return 7
    if sym == F_MED and den == F_HIG and wid == F_HIG:
        return 9


def main():
    character = [
        [255, 255, 255, 255, 255,   0,   0,   0,   0,   0,   0, 255, 255, 255, 255],
        [255, 255, 255,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 255, 255],
        [255, 255,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 255, 255],
        [255,   0,   0,   0,   0,   0, 255, 255, 255,   0,   0,   0,   0,   0, 255],
        [255,   0,   0,   0,   0, 255, 255, 255, 255, 255,   0,   0,   0,   0, 255],
        [0,   0,   0,   0, 255, 255, 255, 255, 255, 255, 255,   0,   0,   0,   0],
        [0,   0,   0,   0, 255, 255, 255, 255, 255, 255, 255,   0,   0,   0,   0],
        [0,   0,   0,   0, 255, 255, 255, 255, 255, 255, 255,   0,   0,   0,   0],
        [0,   0,   0,   0, 255, 255, 255, 255, 255, 255, 255,   0,   0,   0,   0],
        [0,   0,   0,   0, 255, 255, 255, 255, 255, 255, 255, 255,   0,   0,   0],
        [0,   0,   0,   0, 255, 255, 255, 255, 255, 255, 255, 255,   0,   0,   0],
        [0,   0,   0,   0, 255, 255, 255, 255, 255, 255, 255, 255,   0,   0,   0],
        [0,   0,   0, 255, 255, 255, 255, 255, 255, 255, 255, 255,   0,   0,   0],
        [0,   0,   0,   0, 255, 255, 255, 255, 255, 255, 255,   0,   0,   0,   0],
        [0,   0,   0,   0, 255, 255, 255, 255, 255, 255, 255,   0,   0,   0,   0],
        [0,   0,   0,   0, 255, 255, 255, 255, 255, 255, 255,   0,   0,   0,   0],
        [0,   0,   0,   0, 255, 255, 255, 255, 255, 255, 255,   0,   0,   0,   0],
        [255,   0,   0,   0,   0, 255, 255, 255, 255, 255,   0,   0,   0,   0, 255],
        [255,   0,   0,   0,   0,   0, 255, 255, 255,   0,   0,   0,   0,   0, 255],
        [255,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 255, 255],
        [255, 255,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 255, 255],
        [255, 255, 255,   0,   0,   0,   0,   0,   0,   0,   0, 255, 255, 255, 255],
        [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
    ]

    print defuzzify(*fuzzify(character))


if __name__ == '__main__':
    main()
