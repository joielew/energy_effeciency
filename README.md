# Energy Efficiency
## Using Machine Learning to Predict Appliances Energy Consumption
This repository contains a project that focuses on developing an energy consumption prediction system using machine learning techniques. The system aims to provide valuable insights into energy usage patterns and enable users to make informed decisions to optimize energy consumption.

## Project Overview
The energy_efficiency repository houses a predictive model capable of estimating appliance energy consumption based on relevant environmental variables. The project utilizes the CRISP-DM (Cross-Industry Standard Process for Data Mining) framework to address different stages of the data mining process, ensuring a robust and reliable model.

## Contents
1. **Data Understanding**: Gain insights into the dataset, identify relevant features, and perform exploratory data analysis to understand relationships between variables.

2. **Data Preparation**: Scale the data and split it into training and testing sets, ensuring the model's accuracy and reliability.

3. **Model Evaluation**: Train four machine learning algorithms to predict appliance energy consumption and evaluate their performance using appropriate evaluation metrics. The RandomForestRegressor algorithm emerged as the top-performing model, showcasing its superiority in predicting energy consumption.

4. **Integration with Django Web Application**: The trained model is integrated into a user-friendly Django web application. Users can interact with the system and obtain energy consumption predictions by inputting the relevant environmental variables.

5. **Real-world Adaptation**: Recommendations for further enhancements, such as integrating a database model, allow the system to continuously collect and update data in real-world scenarios. This improves the model's accuracy over time and supports better energy management practices in dynamic environments.

## Installation

1. Clone the repository to your local machine:
git clone https://github.com/joielew/energy_efficiency.git

cd energy_efficiency

3. Install the required dependencies:
pip install -r requirements.txt

4. Launch the Django web application:
python manage.py runserver

## Challenges and Solutions
The project encountered several challenges, including locating the model file, handling the dimensionality of input data, and incorporating all relevant features for accurate predictions. Solutions were implemented using techniques like the os method to locate the model file, reshaping input data using np.array.reshape(), and incorporating all essential features to overcome these challenges successfully.

## Future Enhancements
**Database Integratio**n: Integrate a database model for storing and managing new data in real-world scenarios, enabling the model to adapt to changing patterns and improve its accuracy over time.

**Real-time Monitoring**: Explore the possibility of integrating the predictive model with real-time energy monitoring systems for more robust and reliable predictions.

## Conclusion
The "energy_efficiency" repository showcases my first web application of machine learning techniques to predict appliance energy consumption. The developed system provides valuable insights into energy usage patterns and empowers users to optimize energy consumption, contributing to better energy management and sustainability efforts in various domains.

Feel free to explore the repository, try out the web application, and provide feedback on its functionalities and potential improvements. Happy energy optimization!

For any questions or collaborations, please contact me at lewxinyu98@gmail.com.
