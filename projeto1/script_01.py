import time

import common.template_selenium as seleniumfunction

def calcular_numero():
    numero = 2
    for i in range (200):
        numero = (numero*(2*i))
        print(numero)

if __name__ == "__main__":
    print("script1 started")
    headless = False
    browser = seleniumfunction.webdriver_standard(headless)
    print("browser started")
    browser.get("https://google.com")
    print("entrou no google")

    time.sleep(10)
    browser.quit()
    print("fechou webdriver")
    calcular_numero()
    print("Encerrando..")
