from django import forms 
from apps.mascota.models import Mascto

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascto #Modelo del que vamos a crear el formulario
        
        # Campos del modelo a se va a usar en el formulario
        # Y los labels(o etiquetas 
        fields = [ 
            'folio',
            'nombre',
            'genero',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        labels = {
            'folio': 'Folio', 
			'nombre': 'Nombre',
			'genero': 'genero',
			'edad_aproximada': 'Edad aproximada',
			'fecha_rescate':'Fecha de rescate',
			'persona': 'Adoptante',
			'vacuna': 'Vacunas',
		}
        widgets = {
            'folio':forms.TextInput(attrs={'class': 'form-control'}),
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'genero':forms.TextInput(attrs={'class': 'form-control'}),
            'edad_aproximada':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescate':forms.TextInput(attrs={'class': 'form-control'}),
            'persona':forms.Select(attrs={'class': 'form-control'}),
            'vacuna':forms.CheckboxSelectMultiple(),
        }
