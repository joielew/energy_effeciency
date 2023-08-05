from django.shortcuts import render
from .forms import EnergyPredictionForm
import pickle
import os
import numpy as np

def predict_energy_consumption(request):
    file_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

    if request.method == 'POST':
        form = EnergyPredictionForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            with open(file_path, 'rb') as file:
                model = pickle.load(file)

            T1 = cleaned_data.get('T1')
            T2 = cleaned_data.get('T2')
            T3 = cleaned_data.get('T3')
            T4 = cleaned_data.get('T4')
            T5 = cleaned_data.get('T5')
            T7 = cleaned_data.get('T7')
            T8 = cleaned_data.get('T8')
            RH_1 = cleaned_data.get('RH_1')
            RH_2 = cleaned_data.get('RH_2')
            RH_3 = cleaned_data.get('RH_3')
            RH_4 = cleaned_data.get('RH_4')
            RH_5 = cleaned_data.get('RH_5')
            RH_6 = cleaned_data.get('RH_6')
            RH_7 = cleaned_data.get('RH_7')
            RH_8 = cleaned_data.get('RH_8')
            RH_9 = cleaned_data.get('RH_9')
            T_out = cleaned_data.get('T_out')
            Tdewpoint = cleaned_data.get('Tdewpoint')
            RH_out = cleaned_data.get('RH_out')
            Press_mm_hg = cleaned_data.get('Press_mm_hg')
            Windspeed = cleaned_data.get('Windspeed')

            prediction_input = np.array([
                T1, T2, T3, T4, T5, T7, T8, RH_1, RH_2, RH_3, RH_4, RH_5, RH_6, RH_7, RH_8, RH_9, T_out, Tdewpoint, RH_out, Press_mm_hg, Windspeed
            ]).reshape(1, -1)

            energy_predicted = model.predict(prediction_input)[0]
            energy_predicted = round(energy_predicted, 2)

            output_message = f"The appliances energy consumed will be {energy_predicted} Wh."

            context = {'form': form, 'output_message': output_message}
            return render(request, 'prediction.html', context)
        
    else:
        form = EnergyPredictionForm()

    context = {'form': form}
    return render(request, 'prediction.html', context)