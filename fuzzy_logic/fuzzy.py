import sys
import math

F_VHI = 1.0
F_HIG = 0.8
F_MED = 0.5
F_LOW = 0.2
F_VLO = 0

class Fuzzy:

    def __init__(self, data):
        self.data = data


    def closest_fv(self, value):
        vals = [F_VLO, F_LOW, F_MED, F_HIG, F_VHI]
        return min(vals, key=lambda x:abs(x-value))


    def generalized_bell(self, x, a, b, c):
        return 1 / float((1 + math.pow(abs((x-c)/float(a)), 2 * b)))


    def horizontal_symmetry(self, character):
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

    def vertical_symmetry(self, character):
        top_count = 0
        bot_count = 0
        height = len(character)

        top_size = math.floor(height/float(2))
        bot_size = math.ceil(height/float(2))

        for i, row in enumerate(character):
            for j, pixel in enumerate(row):
                if pixel == 0:
                    if i <= top_size:
                        top_count += 1
                    elif i >= bot_size:
                        bot_count += 1

        return top_count / float(bot_count)


    def width(self, character):
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

    def center_width(self, character):
        height = math.floor(len(character) / float(2))
        rows = 0
        rsum = 0

        for i, row in enumerate(character):
            if i >= height - 2 or i <= height + 2:
                rows += 1
                for j, pixel in enumerate(row):
                    if pixel == 0:
                        rsum += 1

        return rsum / float(rows)

    def density(self, character):
        count_w = 0
        count_b = 0

        for row in character:
            for pixel in row:
                if pixel == 0:
                    count_b += 1
                else:
                    count_w += 1

        return count_w / float(count_b)


    def center(self, character):
        center_w = len(character[0]) / 2
        center_h = len(character) / 2

        return character[center_h][center_w] == 0


    def fuzzy_hor_symmetry(self, sym):
        result = self.generalized_bell(sym, 0.3, 1.7, 1.2)
        return self.closest_fv(result)

    def fuzzy_ver_symmetry(self, sym):
        result = self.generalized_bell(sym, 1, 3, 1)
        return self.closest_fv(result)


    def fuzzy_width(self, wid):
        result = self.generalized_bell(wid, 1, 1, 6)
        return self.closest_fv(result)


    def fuzzy_density(self, den):
        result = self.generalized_bell(den, 0.3, 1, 0.85)
        return self.closest_fv(result)

    def fuzzy_center_width(self, cw):
        result = self.generalized_bell(cw, 1, 1, 4)
        return self.closest_fv(result)


    def fuzzify(self, character):
        sym_val = self.horizontal_symmetry(character)
        wid_val = self.width(character)
        den_val = self.density(character)

        sym = self.fuzzy_symmetry(sym_val)
        wid = self.fuzzy_width(wid_val)
        den = self.fuzzy_density(den_val)
        cen = self.center(character)

        # print sym_val, wid_val, den_val, sym, wid, den, cen

        return sym, wid, den, cen


    def defuzzify(self, sym, den, wid, cen):
        # print sym, den, wid, cen
        if sym == F_VHI:
            if cen:
                return 8
            else:
                return 0
        if den <= F_VHI and wid == F_LOW and cen == True:
            return 1
        if sym == F_VHI and den == F_VHI and wid == F_MED and cen == True:
            return 2
        if sym == F_LOW and den == F_HIG and wid == F_HIG and cen == True:
            return 3
        if sym == F_LOW and den == F_VHI and wid == F_MED and cen == False:
            return 4
        if sym == F_MED and den == F_MED and wid == F_MED:
            return 5
        if sym == F_MED and den == F_HIG and wid == F_HIG:
            return 6
        if sym == F_MED and den == F_MED and wid == F_LOW:
            return 7
        if sym == F_HIG and den == F_HIG and wid == F_VHI and cen == True:
            return 9

    def center_piece(self, char):
        blackCount = 0
        charWidth = len(char[0])
        measureWidth = charWidth / 3
        charHeight = len(char)
        measureHeight = charHeight / 3
        for i in range(measureHeight, 2*measureHeight):
            for j in range(measureWidth, 2*measureWidth):
                if char[i][j] == 0:
                    blackCount += 1
        pixelCount = (charWidth - 2*measureWidth) * (charHeight - 2*measureHeight)
        blackPercentage = 1.0 * blackCount / pixelCount
        # print("%.2f" % blackPercentage),
        return blackPercentage

    def top_left(self, char):
        blackCount = 0
        charWidth = len(char[0])
        measureWidth = charWidth / 3
        charHeight = len(char)
        measureHeight = charHeight / 3

        for i in range(0, measureHeight):
            for j in range(0, measureWidth):
                if char[i][j] == 0:
                    blackCount += 1
        pixelCount = (charWidth - 2*measureWidth) * (charHeight - 2*measureHeight)
        blackPercentage = 1.0 * blackCount / pixelCount
        # print("%.2f" % blackPercentage),
        return blackPercentage

    def top_right(self, char):
        blackCount = 0
        charWidth = len(char[0])
        measureWidth = charWidth / 3
        charHeight = len(char)
        measureHeight = charHeight / 3

        for i in range(0, measureHeight):
            for j in range(2*measureWidth, charWidth):
                if char[i][j] == 0:
                    blackCount += 1
        pixelCount = (charWidth - 2*measureWidth) * (charHeight - 2*measureHeight)
        blackPercentage = 1.0 * blackCount / pixelCount
        # print("%.2f" % blackPercentage),
        return blackPercentage

    def bot_left(self, char):
        blackCount = 0
        charWidth = len(char[0])
        measureWidth = charWidth / 3
        charHeight = len(char)
        measureHeight = charHeight / 3

        for i in range(measureHeight*2, charHeight):
            for j in range(0, measureWidth):
                if char[i][j] == 0:
                    blackCount += 1
        pixelCount = (charWidth - 2*measureWidth) * (charHeight - 2*measureHeight)
        blackPercentage = 1.0 * blackCount / pixelCount
        # print("%.2f" % blackPercentage),
        return blackPercentage

    def bot_right(self, char):
        blackCount = 0
        charWidth = len(char[0])
        measureWidth = charWidth / 3
        charHeight = len(char)
        measureHeight = charHeight / 3

        for i in range(measureHeight*2, charHeight):
            for j in range(2*measureWidth, charWidth):
                if char[i][j] == 0:
                    blackCount += 1
        pixelCount = (charWidth - 2*measureWidth) * (charHeight - 2*measureHeight)
        blackPercentage = 1.0 * blackCount / pixelCount
        # print("%.2f" % blackPercentage),
        return blackPercentage

    def btw(self, x, left, right):
        if x >= left and x <= right:
            return True
        return False

    def run(self, char):
        a = self.top_left(char)
        b = self.top_right(char)
        c = self.center_piece(char)
        d = self.bot_left(char)
        e = self.bot_right(char)

        if c < 0.1 and self.btw(a, 0.25, 0.65) and self.btw(b, 0.25, 0.65) and self.btw(d, 0.25, 0.65) and self.btw(e, 0.25, 0.65):
            return 0
        elif c > 0.2 and self.btw(a, 0.25, 0.7) and self.btw(b, 0.25, 0.7) and self.btw(d, 0.25, 0.7) and self.btw(e, 0.25, 0.7) and self.btw(self.fuzzy_hor_symmetry(self.horizontal_symmetry(char)), 0.8, 1.0) and self.btw(self.fuzzy_density(self.density(char)), 1, 1.0):
            return 8
        elif c > 0.4 and self.btw(a, 0.1, 0.4) and self.btw(d, 0, 0.4) and self.btw(e, 0.25, 1):
            return 1
        elif self.btw(c, 0, 0.5) and self.btw(b, 0.45, 0.65) and self.btw(a, 0.15, 0.55) and self.btw(self.fuzzy_hor_symmetry(self.horizontal_symmetry(char)), 0.8, 1) and self.btw(e, 0.2, 0.75):
            return 2
        elif self.btw(c, 0.1, 0.4) and self.btw(a, 0.1, 0.5) and self.btw(self.fuzzy_hor_symmetry(self.horizontal_symmetry(char)), 0, 0.2):
            return 3
        elif self.btw(c, 0.2, 0.5) and self.btw(a, 0, 0.1):
            return 4
        elif self.btw(c, 0.15, 0.35) and self.btw(b, 0.15, 0.45) and self.btw(a, 0.1, 0.6) and self.btw(d, 0.2, 0.55) and self.btw(e, 0.35, 0.65): # fixme!
            return 5
        elif self.btw(c, 0.2, 0.4) and self.btw(e, 0.35, 0.65) and self.horizontal_symmetry(char) > 1:
            return 6
        elif self.btw(e, 0, 0.15):
            return 7
        else:
            return 9



        # print self.fuzzy_center_width(self.center_width(char))
        #print self.center_piece(char),
        # self.top_left(char),
        # self.top_right(char),
        # self.bot_left(char),
        # self.center_piece(char),

        # print self.defuzzify(*self.fuzzify(char)),
