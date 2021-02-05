from django.shortcuts import render

# Create your views here.
import requests
import pandas as pd
import datetime
import random
from random import randrange
from datetime import timedelta
from django.http import HttpResponseRedirect
from pacientes.models import Pacientes

def nome():
    nome_arq = pd.read_csv(r'.\csv\nome.csv')
    df_nome = nome_arq.sample()
    index_nome = df_nome.index
    nome_dict = df_nome.to_dict()
    nome = nome_dict["0"][index_nome[0]]
    nome = nome.title()
    return (nome)

def sbnome():
    sbnome_arq = pd.read_csv(r'.\csv\sobrenome.csv')
    df_sbnome = sbnome_arq.sample()
    index_sbnome = df_sbnome.index
    sbnome_dict = df_sbnome.to_dict()
    sbnome = sbnome_dict["0"][index_sbnome[0]]
    sbnome = sbnome.title()
    return (sbnome)

def gera_data():
    data_atual = datetime.date.today()
    data_past = datetime.date(data_atual.year - 100, data_atual.month, data_atual.day)
    delta = data_atual - data_past
    int_delta = delta.days * 24 * 60 * 60
    rand_sec = randrange(int_delta)
    data_dt = (data_past + timedelta(seconds=rand_sec))
    data_str = datetime.datetime.strftime(data_dt, '%Y%m%d')
    data = datetime.datetime.strptime(data_str, '%Y%m%d').strftime('%Y-%m-%d')
    print(data)
    return data


def gera_cpf():
    cpf = [random.randint(0, 9) for x in range(9)]

    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

        cpf.append(11 - val if val > 1 else 0)

    return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

def gera_tel():
    tel_list = ([random.randint(0, 9) for x in range(8)])
    tel_list.insert(0,9)
    tel = ''.join(map(str, tel_list))
    tel = tel[:5] + '-' + tel[5:]
    return tel

def gera_end():
    end_arq = pd.read_csv(r'.\csv\endereco.csv')
    df_end = end_arq.sample()
    index_end = df_end.index
    end_dict = df_end.to_dict()
    end_str = end_dict["CEP;Tipo_Logradouro;Logradouro;Bairro;Cidade;UF"][index_end[0]].split(';')
    cep = end_str[0]
    end = end_str[1] + ' ' + end_str[2]
    bairro = end_str[3]
    cidade = end_str[4]
    uf = end_str[5]
    return cep, end, bairro, cidade, uf

def gerarPaciente(request):
    num = int(request.POST.get('numero',''))

    url = 'http://127.0.0.1:8000/root/pacientes/'

    for i in range (num):
        cep, end, bairro, cidade, uf = gera_end()

        paciente_dados = {
            "nome": nome() + ' ' + sbnome(),
            "nasc": gera_data(),
            "cpf": gera_cpf(),
            "end": end,
            "cep": cep,
            "bairro": bairro,
            "cidade": cidade,
            "uf": uf,
            "tel": gera_tel(),
        }
        requests.post(url=url, json=paciente_dados)
    
    return HttpResponseRedirect('pacientes')

def pacienteInfo(request):
    pacientes = Pacientes.objects.all()
    return render(request, 'pacientes.html', {'paciente': pacientes})
    