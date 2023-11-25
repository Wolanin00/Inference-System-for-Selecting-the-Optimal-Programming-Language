import unittest
import tkinter as tk
from language_selection_app import LanguageSelectionApp
from utils import get_prepared_data, get_model


class TestE2E(unittest.TestCase):
    def setUp(self):
        data = get_prepared_data()
        self.data = data
        model = get_model(data)
        self.model = model
        self.root = tk.Tk()
        self.app = LanguageSelectionApp(master=self.root, model=model)

    def test_1_python_probability(self):
        """
        **Test cover**: Set all parameters for `Python`, and verify if `Python` predicted.
        """
        scale = 100

        python_index = self.data[1][self.data[1] == "Python"].index[0]
        python_value = self.data[0][self.data[0].index == python_index]

        all_columns = list(self.data[0].columns)

        self.app.easy_slider.set(python_value[all_columns[0]].values[0] * scale)
        self.app.frontend_switch_var.set(int(python_value[all_columns[1]].values[0]))
        self.app.backend_switch_var.set(int(python_value[all_columns[2]].values[0]))
        self.app.data_analysis_switch_var.set(
            int(python_value[all_columns[3]].values[0])
        )
        self.app.availability_slider.set(python_value[all_columns[4]].values[0] * scale)
        self.app.security_mechanisms_slider.set(
            python_value[all_columns[5]].values[0] * scale
        )

        self.app.result_button.invoke()
        result_text = self.app.result_label.cget("text")
        result_text_splitted = result_text.split(" ")
        self.assertEqual(result_text_splitted[1], "Python")
