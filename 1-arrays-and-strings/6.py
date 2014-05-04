import copy
import pprint


def rotate_image(image):
    """Rotate image by 90 degrees. Rotates in place, i.e. mutates the
    original image in memory.

    -- image: NxN matrix, i.e. a list of N lists of length N"""
    
    n = len(image)-1
    for i in xrange(0,n):
        for j in xrange(i, n-i):
            image[i][j], image[j][n-i], image[n-i][n-j], image[n-j][i] = (
                image[n-j][i], image[i][j], image[j][n-i], image[n-i][n-j])
    return image


if __name__ == '__main__':
    test_images = (
        [[0, 1], [2, 3]],
        [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]],
        [[0]]
        )
    expected = (
        [[2, 0], [3, 1]],
        [[20, 15, 10, 5, 0], [21, 16, 11, 6, 1], [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3], [24, 19, 14, 9, 4]],
        [[0]]
        )
    for i in xrange(len(test_images)):
        result = rotate_image(test_images[i])
        if expected[i] != result:
            print "============="
            print "Image:"
            pprint.pprint(test_images[i])
            print "-------------"
            print "Expected:"
            pprint.pprint(expected[i])
            print "-------------"
            print "Result:"
            pprint.pprint(result)
        else:
            print "Success!"

