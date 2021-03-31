from django.shortcuts import render,HttpResponse
from core.Calculadora import Calculadora
# Create your views here.
def hello(request,nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos.</h1>'.format(nome,idade ))

def somando(request,valor_a,valor_b):
    total = Calculadora.soma(request,valor_a,valor_b)
    return HttpResponse('<h1>Somando {} + {} = {}.</h1>'.format(valor_a,valor_b,total))


def subtraindo(request,valor_a,valor_b):
    total = Calculadora.subtracao(request,valor_a,valor_b)
    return HttpResponse('<h1>Subtraindo {} + {} = {}.</h1>'.format(valor_a,valor_b,total))

def dividindo(request,valor_a,valor_b):
    if valor_b == 0:
        return HttpResponse('<h1>Divisão por 0 não realizada.</h1>')
    else:
        total =Calculadora.divisao(request,valor_a,valor_b)
        return HttpResponse('<h1>Dividindo {} + {} = {}.</h1>'.format(valor_a,valor_b,total))

def multiplicando(request,valor_a,valor_b):
    total = Calculadora.multiplicasao(request,valor_a,valor_b)
    return HttpResponse('<h1>Multiplicando {} + {} = {}.</h1>'.format(valor_a,valor_b,total))