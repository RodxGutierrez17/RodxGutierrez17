Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac justo vel metus dapibus placerat. Fusce ultrices facilisis odio, eget tincidunt orci convallis nec. Maecenas quis turpis in mi fermentum auctor. Curabitur eu justo vel orci fermentum convallis. Integer ut massa vitae lacus varius accumsan. Vivamus vel nisl vel arcu auctor congue. Suspendisse potenti. Ut laoreet, dolor a varius sagittis, ligula justo fermentum neque, at congue nulla justo ut velit. Nullam commodo quam a tellus fermentum, ac varius nulla vestibulum. Duis vulputate odio at est vehicula, vel volutpat ligula varius. Cras luctus, arcu nec congue facilisis, lectus nisl sollicitudin turpis, nec dictum ipsum velit sit amet lectus. Nam bibendum ipsum in dolor consequat, ac mattis ligula {password} vitae.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac justo vel metus dapibus placerat. Fusce ultrices facilisis odio, eget tincidunt orci convallis nec. Maecenas quis turpis in mi fermentum auctor. Curabitur eu justo vel orci fermentum convallis. Integer ut massa vitae lacus varius accumsan. Vivamus vel nisl vel arcu auctor congue. Suspendisse potenti. Ut laoreet, dolor a varius sagittis, ligula justo fermentum neque, at congue nulla justo ut velit. Nullam commodo quam a tellus fermentum, ac varius nulla vestibulum. Duis vulputate odio at est vehicula, vel volutpat ligula varius. Cras luctus, arcu nec congue facilisis, lectus nisl sollicitudin turpis, nec dictum ipsum velit sit amet lectus. Nam bibendum ipsum in dolor consequat, ac mattis ligula {password} vitae.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac justo vel metus dapibus placerat. Fusce ultrices facilisis odio, eget tincidunt orci convallis nec. Maecenas quis turpis in mi fermentum auctor. Curabitur eu justo vel orci fermentum convallis. Integer ut massa vitae lacus varius accumsan. Vivamus vel nisl vel arcu auctor congue. Suspendisse potenti. Ut laoreet, dolor a varius sagittis, ligula justo fermentum neque, at congue nulla justo ut velit. Nullam commodo quam a tellus fermentum, ac varius nulla vestibulum. Duis vulputate odio at est vehicula, vel volutpat ligula varius. Cras luctus, arcu nec congue facilisis, lectus nisl sollicitudin turpis, nec dictum ipsum velit sit amet lectus. Nam bibendum ipsum in dolor consequat, ac mattis ligula {password} vitae.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac justo vel metus dapibus placerat. Fusce ultrices facilisis odio, eget tincidunt orci convallis nec. Maecenas quis turpis in mi fermentum auctor. Curabitur eu justo vel orci fermentum convallis. Integer ut massa vitae lacus varius accumsan. Vivamus vel nisl vel arcu auctor congue. Suspendisse potenti. Ut laoreet, dolor a varius sagittis, ligula justo fermentum neque, at congue nulla justo ut velit. Nullam commodo quam a tellus fermentum, ac varius nulla vestibulum. Duis vulputate odio at est vehicula, vel volutpat ligula varius. Cras luctus, arcu nec congue facilisis, lectus nisl sollicitudin turpis, nec dictum ipsum velit sit amet lectus. Nam bibendum ipsum in dolor consequat, ac mattis ligula {password} vitae.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac justo vel metus dapibus placerat. Fusce ultrices facilisis odio, eget tincidunt orci convallis nec. Maecenas quis turpis in mi fermentum auctor. Curabitur eu justo vel orci fermentum convallis. Integer ut massa vitae lacus varius accumsan. Vivamus vel nisl vel arcu auctor congue. Suspendisse potenti. Ut laoreet, dolor a varius sagittis, ligula justo fermentum neque, at congue nulla justo ut velit. Nullam commodo quam a tellus fermentum, ac varius nulla vestibulum. Duis vulputate odio at est vehicula, vel volutpat ligula varius. Cras luctus, arcu nec congue facilisis, lectus nisl sollicitudin turpis, nec dictum ipsum velit sit amet lectus. Nam bibendum ipsum in dolor consequat, ac mattis ligula {password} vitae.

Espero que estos párrafos sean lo suficientemente extensos para tus necesidades. ¡Buena suerte con tu ejercicio de programación!
py
py
main,py
main.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class ChromeDriverManager:
    def install(self):
        pass

# Crea el servicio y el controlador de Chrome
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# URL de la página principal de GitHub
main_url = "https://github.com/RodxGutierrez17"
driver.get(main_url)

# Encuentra los elementos con la clase "repo"
res = driver.find_elements(By.CLASS_NAME, "repo")

# Listas para almacenar los enlaces
link = []
flink = []

# Función para realizar acciones en cada página
def loop(next_page):
    global a
    driver.get(next_page)
    # Encuentra los elementos con la clase "js-navigation-open"
    res2 = driver.find_elements(By.CLASS_NAME, "Link")
    for a in res2:
        pass
        # print(a.text)
    if "py" in a.text:
        print("it is an password in the text")










# Recorre los elementos encontrados y agrega los textos a la lista 'link'
for i in res:
    link.append(i.text)

# Crea enlaces completos y realiza acciones en cada página
for l in link:
    next_page = f"{main_url}/{l}"
    flink.append(next_page)
    # print(flink)
    loop(next_page)

# Cierra el navegador
driver.quit()
