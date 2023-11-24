import pandas as pd
import tkinter as tk
from utils import read_data, get_model
from sklearn.svm import SVC


class LanguageSelectionApp:
    """
    Language Selection App to help in inferring the appropriate programming language according to the given parameters.

    Example usage:

    .. code-block:: python

        programing_language_data = read_data()
        fitted_model = get_model(programing_language_data)

        root = tk.Tk()
        root.grid_propagate(True)
        app = LanguageSelectionApp(master=root, model=fitted_model)
        root.mainloop()
    """

    def __init__(self, master: tk.Tk, model: SVC):
        # SET UI
        master.title("Choosing a Programming Language")
        self.row = 0
        self.model = model
        pad_x = 15

        tk.Label(text="", pady=5).grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )  # break
        self.preferred_lang = tk.Label(master, text="Preferred Language:")
        self.preferred_lang.grid(row=self.row, column=0)

        options = list(self.model.classes_)
        options.append("None")
        selected_option = tk.StringVar(master)
        selected_option.set("None")
        self.preferred_lang_button = tk.OptionMenu(
            master,
            selected_option,
            *options,
            command=self.update_model_about_preferred_lang,
        )
        self.preferred_lang_button.config(width=15, height=2)
        self.preferred_lang_button.grid(
            row=self.increment_and_return_row_number(), column=1
        )

        tk.Label(text="", pady=5).grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )  # break

        # Easy to program
        self.easy_label = tk.Label(master, text="Easy to program:")
        self.easy_label.grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )

        self.easy_slider = tk.Scale(
            master, from_=0, to=100, orient="horizontal", length=300
        )
        self.easy_slider.set(50)
        self.easy_slider.grid(
            row=self.increment_and_return_row_number(),
            column=0,
            pady=3,
            columnspan=2,
            padx=pad_x,
        )

        # Frontend and Backend
        self.frontend_label = tk.Label(master, text="Frontend:")
        self.frontend_label.grid(row=self.row, column=0)

        self.backend_label = tk.Label(master, text="Backend:")
        self.backend_label.grid(row=self.increment_and_return_row_number(), column=1)

        self.frontend_switch_var = tk.BooleanVar(value=False)
        self.frontend_switch_button = tk.Button(
            master,
            text="NO",
            command=lambda: self.toggle_switch(
                switch_var=self.frontend_switch_var, button=self.frontend_switch_button
            ),
            bg="grey",
            width=15,
            height=2,
        )
        self.frontend_switch_button.grid(row=self.row, column=0)

        self.backend_switch_var = tk.BooleanVar(value=False)
        self.backend_switch_button = tk.Button(
            master,
            text="NO",
            command=lambda: self.toggle_switch(
                switch_var=self.backend_switch_var, button=self.backend_switch_button
            ),
            bg="grey",
            width=15,
            height=2,
        )
        self.backend_switch_button.grid(
            row=self.increment_and_return_row_number(), column=1
        )

        tk.Label(text="").grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )  # break

        # Data Analysis
        self.data_analysis_label = tk.Label(master, text="Data Analysis:")
        self.data_analysis_label.grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )

        self.data_analysis_switch_var = tk.BooleanVar(value=False)
        self.data_analysis_switch_button = tk.Button(
            master,
            text="NO",
            command=lambda: self.toggle_switch(
                switch_var=self.data_analysis_switch_var,
                button=self.data_analysis_switch_button,
            ),
            bg="grey",
            width=15,
            height=2,
        )
        self.data_analysis_switch_button.grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )

        tk.Label(text="").grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )  # break

        # Availability
        self.availability_label = tk.Label(master, text="Availability:")
        self.availability_label.grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )

        self.availability_slider = tk.Scale(
            master, from_=0, to=100, orient="horizontal", length=300
        )
        self.availability_slider.set(50)
        self.availability_slider.grid(
            row=self.increment_and_return_row_number(), column=0, pady=3, columnspan=2
        )

        # Security Mechanisms
        self.security_mechanisms_label = tk.Label(master, text="Security Mechanisms:")
        self.security_mechanisms_label.grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )

        self.security_mechanisms_slider = tk.Scale(
            master, from_=0, to=100, orient="horizontal", length=300
        )
        self.security_mechanisms_slider.set(50)
        self.security_mechanisms_slider.grid(
            row=self.increment_and_return_row_number(), column=0, pady=3, columnspan=2
        )

        tk.Label(text="", pady=5).grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )  # break

        # RESULT
        self.result_button = tk.Button(
            master,
            text="Result",
            command=lambda: self.get_predict(model_to_predict=self.model),
            bg="grey",
            width=15,
            height=2,
        )
        self.result_button.grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )

        self.result_label = tk.Label(
            master, text="Result:", font=("Helvetica", 16), pady=10
        )
        self.result_label.grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )

        tk.Label(text="", pady=5).grid(
            row=self.increment_and_return_row_number(), column=0, columnspan=2
        )  # break

    @staticmethod
    def toggle_switch(switch_var: tk.BooleanVar, button: tk.Button) -> None:
        """
        Method to switch button status (ON : OFF)

        Args:
            switch_var (tk.BooleanVar):
            button (tk.Button):

        Returns:
            `None`
        """
        if switch_var.get():
            button.config(text="NO", bg="red")
            switch_var.set(False)
        else:
            button.config(text="YES", bg="green")
            switch_var.set(True)

    def update_model_about_preferred_lang(self, selected_option: str | None) -> None:
        """
        Update model about preferred lang

        Args:
            selected_option (str):

        Returns:
            `None`
        """
        if selected_option != "None":
            new_model = get_model(data=read_data(), preferred_language=selected_option)
            self.model = new_model
        else:
            new_model = get_model(data=read_data())
            self.model = new_model

    def increment_and_return_row_number(self) -> int:
        """
        Used for UI :
        increment and return row number

        Returns:
            row (int):
        """

        row = self.row
        self.row += 1
        return row

    def get_predict(self, model_to_predict: SVC) -> None:
        """
        Get predicted programing language

        Args:
            model_to_predict (SVC):

        Returns:
            `None`
        """

        new_case = pd.DataFrame(
            {
                "Easy to program": [self.easy_slider.get() / 100],
                "Frontend": [self.frontend_switch_var.get()],
                "Backend": [self.backend_switch_var.get()],
                "Data Analysis": [self.data_analysis_switch_var.get()],
                "Availability": [self.availability_slider.get() / 100],
                "Security Mechanisms": [self.security_mechanisms_slider.get() / 100],
            }
        )
        predictions = model_to_predict.predict(new_case)
        self.result_label.config(text=f"Result: {predictions[0]}")
