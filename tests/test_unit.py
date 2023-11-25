import unittest
import tkinter as tk
import pandas as pd
from sklearn.svm import SVC

from language_selection_app import LanguageSelectionApp
from utils import get_prepared_data, get_model, get_all_programming_languages, read_data


class TestMyApp(unittest.TestCase):
    def setUp(self):
        data = get_prepared_data()
        self.data = data
        model = get_model(data)
        self.model = model
        self.root = tk.Tk()
        self.app = LanguageSelectionApp(master=self.root, model=model)

    def test_0a_read_data(self):
        """
        **Test cover**: Check read data.
        """
        data = read_data()
        assert isinstance(data, pd.DataFrame)

    def test_0b_get_prepared_data(self):
        """
        **Test cover**: Check prepared data.
        """
        prepared_data = get_prepared_data()
        assert isinstance(prepared_data, list)

    def test_0c_get_all_programming_languages(self):
        """
        **Test cover**: Check all programming languages.
        """
        all_programming_languages = get_all_programming_languages()
        assert isinstance(all_programming_languages, list)

    def test_0d_get_model(self):
        """
        **Test cover**: Check model.
        """
        model = get_model(data=get_prepared_data())
        assert isinstance(model, SVC)

    def test_01_title(self):
        """
        **Test cover**: Check UI title.
        """
        expected_title = "Choosing a Programming Language"

        self.assertEqual(self.root.title(), expected_title)

    def test_02_label_text(self):
        """
        **Test cover**: Check UI labels.
        """
        expected_easy_label_text = "Easy to program:"
        self.assertEqual(self.app.easy_label.cget("text"), expected_easy_label_text)

        expected_frontend_label_text = "Frontend:"
        self.assertEqual(
            self.app.frontend_label.cget("text"), expected_frontend_label_text
        )

        expected_backend_label_text = "Backend:"
        self.assertEqual(
            self.app.backend_label.cget("text"), expected_backend_label_text
        )

        expected_data_label_text = "Data Analysis:"
        self.assertEqual(
            self.app.data_analysis_label.cget("text"), expected_data_label_text
        )

        expected_availability_label_text = "Availability:"
        self.assertEqual(
            self.app.availability_label.cget("text"), expected_availability_label_text
        )

        expected_security_label_text = "Security Mechanisms:"
        self.assertEqual(
            self.app.security_mechanisms_label.cget("text"),
            expected_security_label_text,
        )

        expected_result_label_text = "Result:"
        self.assertEqual(self.app.result_label.cget("text"), expected_result_label_text)

    def test_05_default_value(self):
        """
        **Test cover**: Check UI default value.
        """
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
        self.assertEqual(
            self.app.security_mechanisms_slider.get(), security_mechanisms_value
        )

    def test_10_predict_01(self):
        """
        **Test cover**: Check UI default predict. If Result in `get_all_programming_languages()`.
        """
        self.app.result_button.invoke()
        result_text = self.app.result_label.cget("text")
        result_text_splitted = result_text.split(" ")
        self.assertIn(result_text_splitted[1], get_all_programming_languages())

    def test_11_set_label_from_0_to_100(self):
        """
        **Test cover**: Check if possible set labels from 0 to 100.
        """
        for value in range(0, 101):
            self.app.easy_slider.set(value)
            self.assertEqual(self.app.easy_slider.get(), value)

    def test_12_set_label_to_101(self):
        """
        **Test cover**: Check if possible set labels to 101 (bad path).
        """
        value_to_set = 101
        expected_error = "101 != 100"
        self.app.easy_slider.set(value_to_set)
        try:
            self.assertEqual(value_to_set, self.app.easy_slider.get())
        except AssertionError as e:
            self.assertEqual(expected_error, e.__str__())
