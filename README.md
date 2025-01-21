
# Machine Downtime Prediction

Try out the application at : https://machine-downtime.onrender.com

![Machine Downtime Prediction](https://i.imgur.com/gqpPcMy.png)

## Dataset

The dataset has been taken from Kaggle. It has 2500 rows and 16 columns. There are some missing values
which have been imputed using 'mean' of the column. The dataset is about downtime records of a factory
and predicts if there is a machine failure or not. The target column includes only two values : 
'Machine_Failure' and 'No_Machine_Failure' which have been converted into numerical values 0 and 1 during 
preprocessing.

## Model

The dataset was trained on 3 models (after a 80:20 split) - Logistic Regression, Decision Tree Classifier and 
Support Vector Classifier. The best accuracy was achieved on Decision Tree Classifier so it has been used in the 
final application.

## Endpoints

There are basically two endpoints:

1. /upload: This lets you upload csv files and then train the model.
2. /predict: This lets you predict the output for some test data.

## Output Format

The output is received as a json consisting of {"prediction" : result}

## Example API requests and responses

1. Request : {
    "Hydraulic_Pressure_bar": 123.095808,
    "Coolant_Pressure_bar": 3.053149,
    "Air_System_Pressure_bar": 5.994826,
    "Coolant_Temperature": 11.9,
    "Hydraulic_Oil_Temperature_C": 47.3,
    "Spindle_Bearing_Temperature_C": 34.5,
    "Spindle_Vibration_m": 1.134,
    "Tool_Vibration_m": 15.695,
    "Spindle_Speed_RPM": 14266.0,
    "Voltage_volts": 351.0,
    "Torque_Nm": 22.884905,
    "Cutting_kN": 1.95
  }

  Response : {
    "prediction" : "No Machine Failure"
  }

2. Request : {
    "Hydraulic_Pressure_bar": 71.04,
    "Coolant_Pressure_bar": 6.933725,
    "Air_System_Pressure_bar": 6.284965,
    "Coolant_Temperature": 25.6,
    "Hydraulic_Oil_Temperature_C": 46.0,
    "Spindle_Bearing_Temperature_C": 33.4,
    "Spindle_Vibration_m": 1.291,
    "Tool_Vibration_m": 26.492,
    "Spindle_Speed_RPM": 25892.0,
    "Voltage_volts": 335.0,
    "Torque_Nm": 24.055326,
    "Cutting_kN": 3.58
  }

  Response : {
    "prediction" : "Machine Failure"
  }


## Setting up

1. Install the dependencies

```bash
python install -r requirements.txt
```

2. Run the application using 

```bash
python app.py
```

[or use python3 in case of python in the commands if you specifically want to use python3]

## Requirements

Inside the data directory, the dataset used for the project is present along with some samples json
files for tetsing.
