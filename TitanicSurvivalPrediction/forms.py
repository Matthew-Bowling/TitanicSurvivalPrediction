from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

class MakePredictions(forms.Form):
    sex_type = forms.ChoiceField(widget=forms.RadioSelect(),
        choices=[(0, 'Male'),(1, 'Female')],
        help_text="Are they male or female?", required=True)
    p_class = forms.ChoiceField(widget=forms.RadioSelect(), 
        choices = [(1, 'Upper Class'),(2,'Middle Class'),(3, 'Lower Class')], 
        help_text='were they first, second, or third class?', required=True)
    embarked = forms.ChoiceField(widget=forms.RadioSelect(), 
        choices = [(0, 'S'),(1, 'C'),(2,'Q')], 
        help_text='Where did they embark out of?', required=True)
    age_category = forms.ChoiceField(widget=forms.RadioSelect(), 
        choices = [(0, 'child'), (1, 'young adult'), (2, 'adult'), (3, 'middle aged'),(4, 'elderly')], 
        help_text='What age group were they?', required=True)
    fare_category = forms.ChoiceField(widget=forms.RadioSelect(),
        choices = [(0, 'dirt cheap'),(1, 'cheap'),(2,'lower than average'),(3,'average priced'),(4, 'above average price'), (5, 'expensive')],
        help_text='About how much was their fare?', required=True)
    family_size = forms.IntegerField(
        help_text='how many family members were present?', 
        required=True,
        validators=[MaxValueValidator(20), MinValueValidator(0)])

    def clean_family_size(self):
        data = self.cleaned_data['family_size']

        if not isinstance(data, int):
            raise ValidationError(_('Invalid Family Size value. Please enter a integer'))

        return data
