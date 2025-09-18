from django.shortcuts import render
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth
from .models import Venda
from datetime import datetime

def dashboard(request):

    # informações para tabela vendas -------------------------------------------------------------------------

    vendas_por_mes_labels = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai','jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    totais_por_mes = Venda.objects.annotate(mes=TruncMonth('data_venda')).values('mes').annotate(montante_total=Sum(F('quantidade') * F('produto__preco'))).order_by('mes')

    total_vendido = []

    for vendas in totais_por_mes:
        total_vendido.append(vendas['montante_total'])

    # informações para tabela vendas -------------------------------------------------------------------------

    # nova tabela de vendas 2025 -------------------------------------------------------------------------
    vendas_2025 = Venda.objects.filter(data_venda__year=datetime.now().year).annotate(mes=TruncMonth('data_venda')).values('mes').annotate(montante_total=Sum(F('quantidade') * F('produto__preco'))).order_by('mes')
    meses = [ 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez' ]
    data = []
    labels = []
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        soma_mes = 0
        for i in vendas_2025:
            if i['mes'].month == mes and i['mes'].year == ano:
                soma_mes += i['montante_total']
        
        labels.append(meses[mes - 1])
        data.append(soma_mes)

    # nova tabela de vendas 2025 -------------------------------------------------------------------------

    # informações para os cards -------------------------------------------------------------------------

    total_unidades_vendidas_ano = Venda.objects.aggregate(Sum('quantidade'))

    media_unidades_vendidas_mes = total_unidades_vendidas_ano['quantidade__sum'] / 12


    receita_anual = sum(total_vendido)

    media_mensal = receita_anual / 12

    # informações para os cards -------------------------------------------------------------------------

    top4_produtos = Venda.objects.values('produto__nome').annotate(total_vendido=Sum('quantidade')).order_by('-total_vendido')[:4]

    produtos_labels = []

    produtos_data = []

    for produto_nome in top4_produtos:
        produtos_labels.append(produto_nome['produto__nome'])

    for produto_quantidade in top4_produtos:
        produtos_data.append(produto_quantidade['total_vendido'])
    
    #------------------------------------------------------------------------------------------------

    vendas_ano_2025 = Venda.objects.filter(data_venda__year=2025).aggregate(total_vendas_2025=Sum(F('quantidade') * F('produto__preco')))


    context = {
        'vendas_por_mes_labels': vendas_por_mes_labels,
        'vendas_por_mes_data': total_vendido,
        'produtos_labels': produtos_labels,
        'produtos_data': produtos_data,
        'receita_anual': receita_anual,
        'media_mensal': media_mensal,
        'total_vendas_mes': media_unidades_vendidas_mes,
        'total_vendas_ano': total_unidades_vendidas_ano['quantidade__sum'],
        'total_vendas_ano_2025': vendas_ano_2025['total_vendas_2025'],
        'vendas_ano_atual_labels': labels[::-1],
        'vendas_ano_atual_data': data[::-1],
    }

    return render(request, 'dashboard/dashboard.html', context)

def estatisticas(request):
    vendas_por_mes_labels = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai','jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    totais_por_mes = Venda.objects.annotate(mes=TruncMonth('data_venda')).values('mes').annotate(montante_total=Sum(F('quantidade') * F('produto__preco'))).order_by('mes')

    total_vendido = []

    for vendas in totais_por_mes:
        total_vendido.append(vendas['montante_total'])
    

    context = {
        'vendas_labels': vendas_por_mes_labels,
        'vendas_data': total_vendido,
    }
    return render(request, 'dashboard/estatisticas.html', context)


def produtos(request):
    
    top4_produtos = Venda.objects.values('produto__nome').annotate(total_vendido=Sum('quantidade')).order_by('-total_vendido')[:4]

    produtos_labels = []

    produtos_data = []

    for produto_nome in top4_produtos:
        produtos_labels.append(produto_nome['produto__nome'])

    for produto_quantidade in top4_produtos:
        produtos_data.append(produto_quantidade['total_vendido'])
    context = {
        'produtos_labels': produtos_labels,
        'produtos_data': produtos_data,
    }
    return render(request, 'dashboard/produtos.html', context)


def estoque(request):
    return render(request, 'dashboard/estoque.html')
