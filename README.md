# Inference System for Selecting the Optimal Programming Language

Project for completing the course "Intelligent reasoning systems"

## Installation
Create conda env with Python 3.9 version -> `conda create --name my_env python=3.9`

Activate conda env -> `conda activate my_env`

Install all below dependencies `pip install <package-name>`:
- `pandas` (I used 2.1.3 version)
- `scikit-learn` (I used 1.3.2 version)

Go to root folder and run `main.py` file -> `python main.py`

## Tests
To run tests go to main folder and run command -> `pytest tests/test_unit.py`

## Release 1 (19.11.2023)
### UI:
<img src="./static/scn/Release_1_UI.jpg" alt="Screenshot" style="border: 1px solid #000;"/>

### Features:
- User can set "Easy to program" slider from 0 to 100,
- User can set "Frontend" button if want to predict frontend language,
- User can set "Backend" button if want to predict backend language,
- User can set "Data Analysis" if want to predict data Analysis language,
- User can set "Availability" slider from 0 to 100,
- User can set "Security Mechanisms" slider from 0 to 100

## Release 2 (22.11.2023)
### UI:
<img src="./static/scn/Release_2_UI.jpg" alt="Screenshot"/>

### Features:
- User can set "Preferred Language" in Option Menu to set double weight in prediction
