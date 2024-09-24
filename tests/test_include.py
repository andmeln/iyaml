import iyaml
import pytest


def test_load():
    data = iyaml.load('tests/data/test_include.yaml')
    assert data['pasw'] == '12345'
    assert 'path' in data
    assert data['list'] == [1, 2]


def test_wildcard():
    data = iyaml.load('tests/data/test_wildcard.yaml')
    assert data['all_templates']['a']['description.md'] == 'A\n'


def test_cyclic_inclusion():
    with pytest.raises(ValueError):
        iyaml.load('tests/data/self_inclusion.yaml')


def test_cyclic_inclusion_2():
    with pytest.raises(ValueError):
        iyaml.load('tests/data/self_inclusion_2.yaml')


def test_save():
    # TODO !!!
    # tmp file
    # save
    # load
    # check
    pass


def test_main():
    # TODO
    pass
