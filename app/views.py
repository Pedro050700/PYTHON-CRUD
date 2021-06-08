from django.shortcuts import render, redirect

from app.forms import FuncionariosForm

from app.models import Funcionarios


# Create your views here.
def home(request):
    data = {}
    data['db'] = Funcionarios.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = FuncionariosForm()
    return render(request, 'form.html', data)


def create(request):
    form = FuncionariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Funcionarios.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Funcionarios.objects.get(pk=pk)
    data['form'] = FuncionariosForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Funcionarios.objects.get(pk=pk)
    form = FuncionariosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')


<<<<<<< HEAD
def load(request):
    return render(request, 'load.html')
=======
def delete(request, pk):
    db = Funcionarios.objects.get(pk=pk)
    db.delete()
    return redirect('home')


def load(request):
    return render(request, 'load.html')
>>>>>>> 1e1ef04... first commit
