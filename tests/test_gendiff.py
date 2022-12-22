import pytest
from gendiff.generate_diff_engine import generate_diff


correct_diff_stylish1 = open('tests/fixtures/diff1.txt').read()
correct_diff_stylish2 = open('tests/fixtures/diff2.txt').read()

correct_diff_plain1 = open('tests/fixtures/diff3.txt').read()
correct_diff_plain2 = open('tests/fixtures/diff4.txt').read()

correct_diff_json = open('tests/fixtures/diff5.txt').read()


@pytest.mark.parametrize("file1,file2,expected", [('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml', correct_diff_stylish1), ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', correct_diff_stylish2)])
def test_stylish(file1, file2, expected):
    assert generate_diff(file1, file2) == expected


@pytest.mark.parametrize("file1,file2,expected", [('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml', correct_diff_plain1), ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', correct_diff_plain2)])
def test_plain(file1, file2, expected):
    assert generate_diff(file1, file2, 'plain') == expected


def test_json():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json')
    assert diff == correct_diff_json
