#pylint: skip-file

from day_four import find_horizontal, find_vertical, find_diagonal

def test_horizontal():
    assert find_horizontal(['XMAS']) == 1
    assert find_horizontal(['XMASXMAS']) == 2
    assert find_horizontal(['XXMAS']) == 1
    assert find_horizontal(['XMAS','XXXX']) == 1
    assert find_horizontal(['XMASXMAS','XMASXXXX']) == 3
    assert find_horizontal(['XXMAS','XXMAS']) == 2
    assert find_horizontal(['XXXX','XXXX']) == 0

def test_backwards_horizontal():
    assert find_horizontal(['SAMX'], True) == 1
    assert find_horizontal(['XMAS'], True) == 0
    assert find_horizontal(['SAMXSAMX'], True) == 2
    assert find_horizontal(['SAMXX'], True) == 1
    assert find_horizontal(['SAMX','XXXX'], True) == 1
    assert find_horizontal(['SAMXSAMX','XXXXSAMX'], True) == 3
    assert find_horizontal(['SAMXX','SAMXX'], True) == 2
    assert find_horizontal(['XXXX','XXXX'], True) == 0

def test_vertical():
    assert find_vertical(['XXXX',
                          'MXXX',
                          'AXXX',
                          'SXXX']) == 1
    assert find_vertical(['XXXX',
                          'MMMM',
                          'AAAA',
                          'SSSS']) == 4
    assert find_vertical(['XMAX',
                          'XMAX',
                          'SSSS',
                          'XXXX']) == 0
    assert find_vertical(['XXXXX',
                          'XMXXX',
                          'XAXMX',
                          'XSXAX',
                          'XXXSX']) == 2

def test_backwards_vertical():
    assert find_vertical(['SXXX',
                          'AXXX',
                          'MXXX',
                          'XXXX'], True) == 1
    assert find_vertical(['SSSS',
                          'AAAA',
                          'MMMM',
                          'XXXX'], True) == 4
    assert find_vertical(['XXXX',
                          'MASX',
                          'XXXX',
                          'MASS'], True) == 0
    assert find_vertical(['SSSSS',
                          'SASSS',
                          'SMSAS',
                          'SXSMS',
                          'SSSXS'], True) == 2

def test_diagonal():
    assert find_diagonal(['XXXX',
                          'MMXX',
                          'AXAX',
                          'SXXS']) == 1
    assert find_diagonal(['XXXX',
                          'MMMM',
                          'AAAA',
                          'SSSS']) == 2
    assert find_diagonal(['XMAX',
                          'XMAX',
                          'SSSS',
                          'XXXX']) == 0
    assert find_diagonal(['XXXXX',
                          'XMMMX',
                          'XAAAX',
                          'XSXSS',
                          'XXXSX']) == 3

def test_backwards_diagonal():
    assert find_diagonal(['SXXX',
                          'MAXX',
                          'AXMX',
                          'SXXX'], True) == 1
    assert find_diagonal(['SSSS',
                          'AAAA',
                          'MMMM',
                          'XXXX'], True) == 2
    assert find_diagonal(['XMAX',
                          'XMAX',
                          'SSSS',
                          'XXXX'], True) == 0
    assert find_diagonal(['SSSSS',
                          'SAAAS',
                          'SMMMS',
                          'XSSXX',
                          'SSSSS'], True) == 3
