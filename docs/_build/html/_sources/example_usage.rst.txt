Example Usage
=============

This page show the example call of application usage and explanation of the principle of operation of buttons and sliders

Example Call
------------

.. code-block:: python

    import tkinter as tk

    from utils import get_prepared_data, get_model
    from language_selection_app import LanguageSelectionApp


    if __name__ == "__main__":
        programing_language_data = get_prepared_data(
            increase_frontend_and_backend_importance=False
        )
        fitted_model = get_model(programing_language_data)

        root = tk.Tk()
        # root.geometry("400x600")  # for hardcoded scale
        root.grid_propagate(True)  # autoscale
        app = LanguageSelectionApp(master=root, model=fitted_model)
        root.mainloop()


Explanation of the principle of operation of buttons and sliders
----------------------------------------------------------------


.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Button or slider
     - Explanation
   * - Preferred Language
     - The user can select the preferred language, then the prediction weight is increased from 1.0 to 2.0
   * - Frontend and Backend importance
     -
       * If YES, additional filtering is used to eliminate languages that are incompatible with the selected values for Backend and Frontend buttons
       * If NO, the values to be predicted are not additionally filtered by the values of the Frontend and Backend buttons
   * - Frontend
     - The user can indicate whether the programming language should be front-end for the prediction weight
   * - Backend
     - The user can indicate whether the programming language should be back-end for the prediction weight
   * - Easy to program
     - The user can indicate whether the programming language should be easy to program, the value is added to the prediction weight
   * - Data Analysis
     - The user can indicate whether the programming language should be associated with working with data, the value is added to the prediction weight
   * - Availability
     - The user can indicate whether the programming language should be common in the community, a value is added to the prediction weight
   * - Security Mechanisms
     - The user can indicate whether the programming language should be equipped with security mechanisms, the value is added to the prediction weight
