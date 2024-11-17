from django import forms
from .models import Reseña, Festival

class ReseñaForm(forms.ModelForm):
    CALIFICACIONES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    calificacion = forms.ChoiceField(
        choices=CALIFICACIONES,
        widget=forms.RadioSelect,  # Usa radio buttons
        label="Calificación"
    )

    class Meta:
        model = Reseña
        fields = ['nombre', 'festival', 'comentario', 'calificacion']
