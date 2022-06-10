# The DearPyGUI window

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Windchill Calculator', width=600, height=300)

with dpg.window(label="Windchill Calculator", width=600, height=300):
    dpg.add_text("Hello, welcome to the Windchill Calculator")
    dpg.add_input_int(label="Wind Speed")
    dpg.add_input_int(label="Temperature")
    dpg.add_button(label="Enter")
    dpg.add_button(label="Clear")
    
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()