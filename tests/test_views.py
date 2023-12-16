from tests.conf_test import client

# teste si lápplication envoie bien les pages en dernier un test avec des données POST

def test_index_status_codeOK(client):
    response = client.get('/index/')
    print(response.status_code)
    assert response.status_code == 200

def test_origin_status_codeOK(client):
    response = client.get('/')
    print(response.status_code)
    assert response.status_code == 200

def test_CV_status_codeOK(client):
    response = client.get('/cv/')
    print(response.status_code)
    assert response.status_code == 200

def test_data_status_codeOK(client):
    response = client.get('/data/')
    print(response.status_code)
    assert response.status_code == 200

def test_determination_pingouin_status_codeOK(client):
    response = client.get('/determination_pingouin/')
    print(response.status_code)
    assert response.status_code == 200

def test_description_IA_pingouin_status_codeOK(client):
    response = client.get('/description_IA_pingouin/')
    print(response.status_code)
    assert response.status_code == 200

def test_python_data_status_codeOK(client):
    response = client.get('/python_data/')
    print(response.status_code)
    assert response.status_code == 200

def test_python_graph_codeOK(client):
    response = client.get('/python_graph/')
    print(response.status_code)
    assert response.status_code == 200

def test_aide_memoire_codeOK(client):
    response = client.get('/aide_memoire/')
    print(response.status_code)
    assert response.status_code == 200

def test_git_codeOK(client):
    response = client.get('/git/')
    print(response.status_code)
    assert response.status_code == 200

def test_ansible_codeOK(client):
    response = client.get('/ansible/')
    print(response.status_code)
    assert response.status_code == 200

def test_docker_codeOK(client):
    response = client.get('/docker/')
    print(response.status_code)
    assert response.status_code == 200

def test_flask_codeOK(client):
    response = client.get('/flask/')
    print(response.status_code)
    assert response.status_code == 200

def test_variable_serveur_codeOK(client):
    response = client.get('/variable_serveur/')
    print(response.status_code)
    assert response.status_code == 200

def test_terraform_codeOK(client):
    response = client.get('/terraform/')
    print(response.status_code)
    assert response.status_code == 200

def test_liens_codeOK(client):
    response = client.get('/liens/')
    print(response.status_code)
    assert response.status_code == 200

def test_git_codeOK(client):
    response = client.get('/git/')
    print(response.status_code)
    assert response.status_code == 200
