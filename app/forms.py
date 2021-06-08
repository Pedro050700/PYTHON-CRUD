from django.forms import ModelForm

from app.models import Funcionarios


# Create the form class.
class FuncionariosForm(ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['Nome', 'Cargo', 'Nivel']
