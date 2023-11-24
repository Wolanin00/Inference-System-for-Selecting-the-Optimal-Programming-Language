import tkinter as tk

from utils import get_prepared_data, get_model
from language_selection_app import LanguageSelectionApp


if __name__ == "__main__":
    programing_language_data = get_prepared_data(
        increase_frontend_and_backend_importance=False
    )
    fitted_model = get_model(programing_language_data)

    root = tk.Tk()
    # root.geometry("400x600")  # hardcoded scale
    root.grid_propagate(True)  # add autoscale
    app = LanguageSelectionApp(master=root, model=fitted_model)
    root.mainloop()
