import os
import pandas as pd

from sklearn.svm import SVC


def get_all_programming_languages() -> list:
    """
    Function to get all programming languages

    Returns:
        data (list): all programming languages
    """
    data = read_data()

    return data["Programing language"].to_list()


def get_prepared_data(
    is_frontend: bool = False,
    is_backend: bool = False,
    increase_frontend_and_backend_importance: bool = False,
) -> list:
    """
    Prepare data for frontend and backend languages.

    Args:
        increase_frontend_and_backend_importance (bool): increase weight of frontend and backend importance for predict programming language
        is_frontend (bool): return only frontend languages
        is_backend (bool): return only backend languages

    Returns:
        data (list):
    """
    data = read_data()
    if increase_frontend_and_backend_importance:
        if is_frontend:
            data = data[data["Frontend"] != 0]
        else:
            data = data[data["Frontend"] != 1]

        if is_backend:
            data = data[data["Backend"] != 0]
        else:
            data = data[data["Backend"] != 1]

    x_col = data.columns.drop("Programing language")
    x = data[x_col]
    y = data["Programing language"]
    return [x, y]


def read_data() -> pd.DataFrame:
    """
    Read prepared data from `prog_lang_db.xlsx` file.

    Returns:
        data (pd.DataFrame):
    """
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_name = "prog_lang_db.xlsx"
    file_path = os.path.join(script_directory, file_name)

    data = pd.read_excel(file_path, decimal=",")

    return data


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
