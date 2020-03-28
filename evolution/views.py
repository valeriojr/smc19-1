from django.shortcuts import render


def graph_evolution(request):

    return render(request, 'evolution/graph_evolution.html', context={})