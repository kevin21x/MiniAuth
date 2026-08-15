
import pytest
from MiniAuth.sistema import Sistema

@pytest.fixture
def sistema():
    sistema = Sistema()

    yield sistema

    print('Teste terminou!')

@pytest.fixture
def sistema_com_usuario(sistema):
    sistema.cadastrar_usuario('Kevin', '123')
    sistema.cadastrar_usuario('Maria', '123')

    yield sistema
    print('Limpeza dos usuarios de teste!')

def test_login_maria(sistema_com_usuario):
    usuario = sistema_com_usuario.login('Maria', '123')
    assert(usuario is not None)

def test_login_maria_senha_incorreta(sistema_com_usuario):
    usuario = sistema_com_usuario.login('Maria', '124')
    assert(usuario is None)

def test_login_com_login_vazio(sistema_com_usuario):
    usuario = sistema_com_usuario.login('', '123')
    assert(usuario is None)

def test_login_com_senha_vazia(sistema_com_usuario):
    usuario = sistema_com_usuario.login('Kevin', '')

    assert(usuario is None)

def test_cadastro_duplicado(sistema):

    sistema.cadastrar_usuario("Kevin", "123")

    resultado = sistema.cadastrar_usuario("Kevin", "123")

    assert(resultado is False)


def test_login_senha_incorreta(sistema_com_usuario):

    usuario = sistema_com_usuario.login('Kevin', '456')

    assert(usuario is None)


def test_login_correto(sistema_com_usuario):

    usuario = sistema_com_usuario.login('Kevin', '123')

    assert(usuario is not None)


def test_login_desativado(sistema_com_usuario):

    sistema_com_usuario.desativar_usuario('Kevin')

    usuario = sistema_com_usuario.login('Kevin', '123')

    assert(usuario is None)

def test_login_reativado(sistema_com_usuario):

    sistema_com_usuario.desativar_usuario('Kevin')
    
    sistema_com_usuario.reativar_usuario('Kevin')
    
    usuario = sistema_com_usuario.login('Kevin', '123')
    
    assert(usuario is not None)

def test_login_usuario_removido(sistema):
        
    sistema.cadastrar_usuario('Kevin', '123')
    
    usuario = sistema.remover_usuario('Kevin')

    usuario = sistema.login('Kevin', '123')
        
    assert(usuario is None)