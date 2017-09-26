import ui

def calculate(sender):
	circumference = 2*3.14*float(view['radius_input'].text)
	view['radius_output'].text = 'radius: ' + str(circumference)

view = ui.load_view()
view.present('sheet')
