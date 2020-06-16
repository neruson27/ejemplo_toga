import toga

def on_press(widget):
  print("hola")

def new_button(name, callback):
  button = toga.Button(name, on_press=callback)
  button.style.padding = 20
  button.style.font_size = 20
  button.style.width = 200
  return button

def build(app):
  box = toga.Box()
  boton1 = new_button('boton', on_press)
  box.add(boton1)
  return box

def main():
  app = toga.App('python dex', 'com.pythondex.toga', startup=build)
  return app

if __name__ == '__main__':
  app = main()
  app.main_loop()
