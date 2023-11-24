import os
import pandas as pd

from sklearn.svm import SVC


def read_data() -> list:
    """
    Read prepared data from `prog_lang_db.xlsx` file.

    Returns:
        list: List of X and Y data.

    """
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_name = "prog_lang_db.xlsx"
    file_path = os.path.join(script_directory, file_name)

    data = pd.read_excel(file_path, decimal=",")

    x_col = data.columns.drop("Programing language")
    x = data[x_col]
    y = data["Programing language"]
    return [x, y]


def get_model(data: list, preferred_language: str = None) -> SVC:
    """
    Get fitted model.

    Args:
        data (list): List of data.
        preferred_language (str): preferred programming language.

    Returns:
         model (SVC): Fitted SVC model.
    """
    if preferred_language:
        sample_weights = {class_label: 1.0 for class_label in data[1].unique()}
        sample_weights[preferred_language] = 2.0

        svm_model = SVC(class_weight=sample_weights)
        svm_model.fit(data[0], data[1])
    else:
        svm_model = SVC()
        svm_model.fit(data[0], data[1])
    return svm_model
