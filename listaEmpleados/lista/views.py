from django.shortcuts import render

# Create your views here.
def listaEmpleados(request):
 listado = ['Aurora Jimenez', 'Mateo Diaz', 'Juan Perez', 'Nicolas Clos', 'Felipe Vergara', 'Maria Diaz', 'Veronica Soto', 'Benito Juares', 'benjamin Duarte']
 context = {'listado': listado}
 return render(request, 'listaEmpleados.html ', context)