from model import Session, Projeto, Categoria, Gerente, Status
from datetime import datetime
from sqlalchemy import create_engine, exc

session = Session()

statuses = [{'status': 'Não iniciado'},
        {'status': 'Em andamento'},
        {'status': 'Concluído'},
        {'status': 'Atrasado'},
        {'status': 'Suspenso'},
        {'status': 'Cancelado'},
        {'status': 'Postergado'}]

for status in statuses:
    record = Status(**status)
    try:
        session.merge(record)
        session.commit()
    except exc.IntegrityError:
        session.rollback()
        

gerentes = [{'gerente':'Fulano'},
            {'gerente':'Beltrano'},
            {'gerente':'Ciclano'},
            {'gerente':'John Doe'},
            {'gerente':'Jane Doe'}]

for gerente in gerentes:
    record = Gerente(**gerente)
    try:
        session.merge(record)
        session.commit()
    except exc.IntegrityError:
        session.rollback()


categorias = [{'categoria': 'Regulatório'},
        {'categoria': 'Estratégico'},
        {'categoria': 'Melhoria contínua'},
        {'categoria': 'Manutenção'},
        {'categoria': 'Pesquisa e Desenvolvimento'},
        {'categoria': 'Novos mercados'},
        {'categoria': 'ESG'}]

for categoria in categorias:
    record = Categoria(**categoria)
    try:
        session.merge(record)
        session.commit()
    except exc.IntegrityError:
        session.rollback()


projetos =[{'nome': 'Expansão da planta de Campinas',
            'descricao': 'Projeto de expansão da capacidade de produção da fábrica localizada em Campinas-SP',
            'inicio': datetime.strptime('01/01/2023', '%d/%m/%Y'), 
            'fim': datetime.strptime('31/12/2023', '%d/%m/%Y'),
            'id_categoria': 2,
            'id_gerente': 3,
            'id_status': 2},

            {'nome': 'Novos modelos de transporte',
            'descricao': 'Estudo da viabilidade técnica, financeira e operacional de novos modais de transporte para produto acabado',
            'inicio': datetime.strptime('01/01/2023', '%d/%m/%Y'), 
            'fim': datetime.strptime('31/12/2023', '%d/%m/%Y'),
            'id_categoria': 5,
            'id_gerente': 5,
            'id_status': 1},

            {'nome': 'Nova legislação de efluentes',
            'descricao': 'Análise das alternativas e atendimento a nova legislação de emissão de efluentes',
            'inicio': datetime.strptime('01/01/2023', '%d/%m/%Y'), 
            'fim': datetime.strptime('31/12/2023', '%d/%m/%Y'),
            'id_categoria': 1,
            'id_gerente': 1,
            'id_status': 3},

            {'nome': 'Projeto ambiental',
            'descricao': 'Trabalho em conjunto com a comunidade local para restauração de áreas nativas próximo as unidades de produção',
            'inicio': datetime.strptime('01/01/2024', '%d/%m/%Y'), 
            'fim': datetime.strptime('30/06/2024', '%d/%m/%Y'),
            'id_categoria': 7,
            'id_gerente': 1,
            'id_status': 7}]

for projeto in projetos:
    record = Projeto(**projeto)
    try:
        session.merge(record)
        session.commit()
    except exc.IntegrityError:
        session.rollback()