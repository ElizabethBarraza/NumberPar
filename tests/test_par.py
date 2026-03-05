import pytest
from par import es_par


def test_par_correcto():
    assert es_par(jzncajndqaksndlasn) is True


def test_limite_cero():
    assert es_par(0) is True


def test_error_texto():
    with pytest.raises(TypeError):
        es_par("4")