from django import forms

class EnergyPredictionForm(forms.Form):
    T1 = forms.FloatField(label='Temperature in kitchen')
    T2 = forms.FloatField(label='Temperature in living room')
    T3 = forms.FloatField(label='Temperature in laundry')
    T4 = forms.FloatField(label='Temperature in office')
    T5 = forms.FloatField(label='Temperature in bathroom')
    T7 = forms.FloatField(label='Temperature in ironing room')
    T8 = forms.FloatField(label='Temperature in teenager room')
    RH_1 = forms.FloatField(label='Humidity in kitchen')
    RH_2 = forms.FloatField(label='Humidity in living room')
    RH_3 = forms.FloatField(label='Humidity in laundry')
    RH_4 = forms.FloatField(label='Humidity in office')
    RH_5 = forms.FloatField(label='Humidity in bathroom')
    RH_6 = forms.FloatField(label='Humidity outside the building (north)')
    RH_7 = forms.FloatField(label='Humidity in ironing room')
    RH_8 = forms.FloatField(label='Humidity in teenager room')
    RH_9 = forms.FloatField(label='Humidity in parents room')
    T_out = forms.FloatField(label='Temperature outside')
    Tdewpoint = forms.FloatField(label='Dew Point')
    RH_out = forms.FloatField(label='Humidity outside')
    Press_mm_hg = forms.FloatField(label='Pressure outside')
    Windspeed = forms.FloatField(label='Wind Speed')

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data
    