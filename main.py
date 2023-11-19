import pandas as pd
import tkinter as tk
from sklearn.ensemble import RandomForestClassifier


class LanguageSelectionApp:
    def __init__(self, master):

        programing_language_data = self.read_data()
        model = self.get_model(programing_language_data)

        # UI
        master.title("Choosing a Programming Language")

        tk.Label(text="", pady=5).pack()  # break

        # Easy to program
        self.easy_label = tk.Label(master, text="Easy to program:")
        self.easy_label.pack()

        self.easy_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300)
        self.easy_slider.set(50)
        self.easy_slider.pack()

        # Frontend
        self.frontend_label = tk.Label(master, text="Frontend:")
        self.frontend_label.pack()

        self.frontend_switch_var = tk.BooleanVar(value=False)
        self.frontend_switch_button = tk.Button(root, text="NO",
                                                command=lambda: self.toggle_switch(switch_var=self.frontend_switch_var,
                                                                                   button=self.frontend_switch_button),
                                                bg="grey", width=15, height=2)
        self.frontend_switch_button.pack(pady=10)

        # Backend
        self.backend_label = tk.Label(master, text="Backend:")
        self.backend_label.pack()

        self.backend_switch_var = tk.BooleanVar(value=False)
        self.backend_switch_button = tk.Button(root, text="NO",
                                               command=lambda: self.toggle_switch(switch_var=self.backend_switch_var,
                                                                                  button=self.backend_switch_button),
                                               bg="grey", width=15, height=2)
        self.backend_switch_button.pack(pady=10)

        # Data Analysis
        self.data_analysis_label = tk.Label(master, text="Data Analysis:")
        self.data_analysis_label.pack()

        self.data_analysis_switch_var = tk.BooleanVar(value=False)
        self.data_analysis_switch_button = tk.Button(root, text="NO",
                                                     command=lambda: self.toggle_switch(
                                                         switch_var=self.data_analysis_switch_var,
                                                         button=self.data_analysis_switch_button),
                                                     bg="grey", width=15, height=2)
        self.data_analysis_switch_button.pack(pady=10)

        # Availability
        self.availability_label = tk.Label(master, text="Availability:")
        self.availability_label.pack()

        self.availability_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300)
        self.availability_slider.set(50)
        self.availability_slider.pack()

        # Security Mechanisms
        self.security_mechanisms_label = tk.Label(master, text="Security Mechanisms:")
        self.security_mechanisms_label.pack()

        self.security_mechanisms_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300)
        self.security_mechanisms_slider.set(50)
        self.security_mechanisms_slider.pack()

        tk.Label(text="", pady=5).pack()  # break

        # RESULT
        self.result_button = tk.Button(master, text="Result", command=lambda: self.get_predict(model), bg="grey",
                                       width=15, height=2)
        self.result_button.pack()

        self.result_label = tk.Label(master, text="Result: -----", font=("Helvetica", 16), pady=10)
        self.result_label.pack()

        tk.Label(text="", pady=5).pack()  # break

    @staticmethod
    def toggle_switch(switch_var, button):
        if switch_var.get():
            button.config(text="NO", bg="red")
            switch_var.set(False)
        else:
            button.config(text="YES", bg="green")
            switch_var.set(True)

    @staticmethod
    def read_data():
        data = pd.read_excel("./prog_lang_db.xlsx")
        x_col = data.columns.drop('Programing language')
        x = data[x_col]
        y = data['Programing language']
        return [x, y]

    @staticmethod
    def get_model(data):
        model = RandomForestClassifier()
        model.fit(data[0], data[1])
        return model

    def get_predict(self, model):
        new_case = pd.DataFrame(
            {
                'Easy to program': [self.easy_slider.get() / 100],
                "Frontend": [self.frontend_switch_var.get()],
                "Backend": [self.backend_switch_var.get()],
                "Data Analysis": [self.data_analysis_switch_var.get()],
                "Availability": [self.availability_slider.get() / 100],
                "Security Mechanisms": [self.security_mechanisms_slider.get() / 100],
            })
        predictions = model.predict(new_case)
        self.result_label.config(text=f"Result: {predictions[0]}")


if __name__ == '__main__':

    root = tk.Tk()
    root.geometry("400x600")
    app = LanguageSelectionApp(root)
    root.mainloop()
