import cv2
import numpy
import os
import neural_network.neural as neural
import random
import pickle

def cleardir(dir):
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e


def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def binarization(image):
    # gaussian blur the image to decrease noise
    blur = cv2.GaussianBlur(image, (3,3), 0)

    # perform otsu's method to create black and white image
    ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    cv2.imwrite('images/debug/blur.png', blur)
    cv2.imwrite('images/debug/otsu.png', otsu)

    #cv2.imshow('gaussian', blur)
    #cv2.imshow('otsu', otsu)
    #cv2.waitKey(0)

    return otsu


def lineSeparation(image):
    rowBlackCount = []
    for i in range(len(image)):
        blackCount = 0
        for j in range(len(image[i])):
            if (image[i][j] == 0):
                blackCount = blackCount + 1
        rowBlackCount.append(blackCount)

    foundLine = False
    lineStart = 0
    whiteLineCount = 0
    lineImages = []
    for i in range(len(rowBlackCount)):
        if foundLine == False:
            if rowBlackCount[i] > 0:
                foundLine = True
                lineStart = i
        else:
            if rowBlackCount[i] == 0:
                if whiteLineCount < 2:
                    whiteLineCount = whiteLineCount + 1
                else:
                    foundLine = False
                    lineEnd = i - 1
                    lineImage = image[lineStart:lineEnd]
                    lineImages.append(lineImage)
                    whiteLineCount = 0

    for i in range(len(lineImages)):
        fileName = 'images/debug/lines/' + str(i) + '.png'
        cv2.imwrite(fileName, lineImages[i])

    return lineImages


def charSeparation(line):
    if len(line) < 1:
        return
    width = len(line[0])

    columnBlackCount = []
    for i in range(width):
        blackCount = 0
        for j in range(len(line)):
            if (line[j][i] == 0):
                blackCount = blackCount + 1
        columnBlackCount.append(blackCount)

    foundChar = False
    charStart = 0
    charImages = []
    for i in range(len(columnBlackCount)):
        if foundChar == False:
            if columnBlackCount[i] > 0:
                foundChar = True
                charStart = i
        else:
            if columnBlackCount[i] == 0:
                foundChar = False
                charEnd = i
                charImage = numpy.zeros((len(line), charEnd - charStart))
                for j in range(len(line)):
                    for k in range(charEnd - charStart):
                        charImage[j][k] = line[j][k + charStart]
                charImages.append(charImage)
    return charImages


def charSeparationFromLines(lines):
    lineCharacters = []
    for i in range(len(lines)):
        charImages = charSeparation(lines[i])
        lineCharacters.append(charImages)
        mkdir('images/debug/characters/' + str(i))
        cleardir('images/debug/characters/' + str(i))
        for j in range(len(charImages)):
            fileName = 'images/debug/characters/' + str(i) + '/' + str(j) + '.png'
            cv2.imwrite(fileName, charImages[j])

    return lineCharacters



def bufferCharImages(chars):
    lineCharImages = []
    for i in range(len(chars)):
        charImages = []
        mkdir('images/debug/bufferedcharacters/' + str(i))
        cleardir('images/debug/bufferedcharacters/' + str(i))
        for j in range(len(chars[i])):
            charImage = numpy.zeros((26, 18))
            for k in range(26):
                for l in range(18):
                    if k < len(chars[i][j]) and l < len(chars[i][j][k]):
                        charImage[k][l] = chars[i][j][k][l]
                    else:
                        charImage[k][l] = 255
            fileName = 'images/debug/bufferedcharacters/' + str(i) + '/' + str(j) + '.png'
            cv2.imwrite(fileName, charImage)
            charImages.append(charImage)
        lineCharImages.append(charImages)
    return lineCharImages

def main():
    mkdir('images/debug/')
    mkdir('images/debug/lines/')
    mkdir('images/debug/characters/')
    mkdir('images/debug/bufferedcharacters/')
    cleardir('images/debug/')
    cleardir('images/debug/lines/')
    cleardir('images/debug/characters/')
    cleardir('images/debug/bufferedcharacters/')


    # # read and grey scale image
    # image = cv2.imread('images/training/num.png', 0)
    # cv2.imwrite('images/debug/grey.png', image)
    # #cv2.imshow('greyscale', grey)
    # #cv2.waitKey(0)


    # # binarize the image
    # binaryImage = binarization(image)


    # # process image by skewing it if enough time and needed
    # # ????????


    # # line separation
    # lines = lineSeparation(binaryImage)


    # # character separation
    # characters = charSeparationFromLines(lines)


    # bufferedCharacters = bufferCharImages(characters)




    #test = neural.Neural(bufferedCharacters)
    #test.train()


    #with open('test.txt', 'wb') as f:
    #    pickle.dump(test, f)

    with open('MLPWeights', 'rb') as f:
        test2 = pickle.load(f)






    image = cv2.imread('images/test/2.png', 0)
    binaryImage = binarization(image)
    lines = lineSeparation(binaryImage)
    characters = charSeparationFromLines(lines)
    bufferedCharacters = bufferCharImages(characters)

    for i in range(len(bufferedCharacters)):
        for j in range(len(bufferedCharacters[i])):
            # noise
            #bufferedCharacters[0][i][random.randint(0, 25)][random.randint(0, 16)] = 0
            #bufferedCharacters[0][i][random.randint(0, 25)][random.randint(0, 16)] = 0
            #bufferedCharacters[0][i][random.randint(0, 25)][random.randint(0, 16)] = 0
            #bufferedCharacters[0][i][random.randint(0, 25)][random.randint(0, 16)] = 0
            #cv2.imshow('noise', bufferedCharacters[i][j])
            #cv2.waitKey(0)

            #retval = test.run(bufferedCharacters[0][i])
            #print retval
            retval = test2.run(bufferedCharacters[i][j])
            print retval,
        print ''

if __name__ == '__main__':
    main()