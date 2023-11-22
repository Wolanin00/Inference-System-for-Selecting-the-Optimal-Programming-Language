import unittest
import tkinter as tk
from main import LanguageSelectionApp, read_data, get_model


class TestMyApp(unittest.TestCase):
    def setUp(self):
        data = read_data()
        self.data = data
        model = get_model(data)
        self.model = model
        self.root = tk.Tk()
        self.app = LanguageSelectionApp(master=self.root, model=model)

    def test_01_title(self):
        expected_title = "Choosing a Programming Language"

        self.assertEqual(self.root.title(), expected_title)

    def test_02_label_text(self):
        expected_easy_label_text = "Easy to program:"
        self.assertEqual(self.app.easy_label.cget("text"), expected_easy_label_text)

        expected_frontend_label_text = "Frontend:"
        self.assertEqual(self.app.frontend_label.cget("text"), expected_frontend_label_text)

        expected_backend_label_text = "Backend:"
        self.assertEqual(self.app.backend_label.cget("text"), expected_backend_label_text)

        expected_data_label_text = "Data Analysis:"
        self.assertEqual(self.app.data_analysis_label.cget("text"), expected_data_label_text)

        expected_availability_label_text = "Availability:"
        self.assertEqual(self.app.availability_label.cget("text"), expected_availability_label_text)

        expected_security_label_text = "Security Mechanisms:"
        self.assertEqual(self.app.security_mechanisms_label.cget("text"), expected_security_label_text)

        expected_result_label_text = "Result:"
        self.assertEqual(self.app.result_label.cget("text"), expected_result_label_text)

    def test_05_default_value(self):
        easy_default_value = 50
        fronted_bool_value = False
        backend_bool_value = False
        data_analysis_value = False
        availability_value = 50
        security_mechanisms_value = 50

        self.assertEqual(self.app.easy_slider.get(), easy_default_value)
        self.assertEqual(self.app.frontend_switch_var.get(), fronted_bool_value)
        self.assertEqual(self.app.backend_switch_var.get(), backend_bool_value)
        self.assertEqual(self.app.data_analysis_switch_var.get(), data_analysis_value)
        self.assertEqual(self.app.availability_slider.get(), availability_value)
        self.assertEqual(self.app.security_mechanisms_slider.get(), security_mechanisms_value)

    def test_10_predict_01(self):
        self.app.result_button.invoke()
        result_text = self.app.result_label.cget("text")
        result_text_splitted = result_text.split(" ")
        self.assertIn(result_text_splitted[1], list(self.model.classes_))

    def test_11_set_easy_to_100(self):
        value_to_set = 99
        self.app.easy_slider.set(value_to_set)
        self.assertEqual(self.app.easy_slider.get(), 99)

    def test_12_python_probability(self):
        scale = 100

        python_index = self.data[1][self.data[1] == "Python"].index[0]
        python_value = self.data[0][self.data[0].index == python_index]

        all_columns = list(self.data[0].columns)

        self.app.easy_slider.set(python_value[all_columns[0]].values[0]*scale)
        self.app.frontend_switch_var.set(int(python_value[all_columns[1]].values[0]))
        self.app.backend_switch_var.set(int(python_value[all_columns[2]].values[0]))
        self.app.data_analysis_switch_var.set(int(python_value[all_columns[3]].values[0]))
        self.app.availability_slider.set(python_value[all_columns[4]].values[0]*scale)
        self.app.security_mechanisms_slider.set(python_value[all_columns[5]].values[0]*scale)

        self.app.result_button.invoke()
        result_text = self.app.result_label.cget("text")
        result_text_splitted = result_text.split(" ")
        self.assertEqual(result_text_splitted[1], "Python")


if __name__ == "__main__":
    unittest.main()
