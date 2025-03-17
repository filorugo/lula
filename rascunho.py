import webbrowser

def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)


search_google("free fire")



html_content = driver.page_source

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")

# Find the <tbody> element
tbody_element = soup.find("concessionaria/00Q4M00000yTNvdUAG")

# Now you can work with the <tbody> data as needed
print(tbody_element.prettify())  # Print the prettified HTML content of <tbody>
sleep(10)





data_atual = datetime.now()

dia_atual = data_atual.strftime("%d/%m/%Y")



# Open the link in a new tab
    driver.execute_script("window.open('{}', '_blank');".format(link_url))











# Find the column header for "Responsável"
column_header = driver.find_element(By.XPATH, '//*[@id="lsLead"]/thead/tr/th[7]')






# Define a function to process each customer profile
def process_customer_profile():
    # Check if the "responsavel" grid cell is empty
    responsavel_cell = driver.find_element(By.XPATH, '//*[@id="lsLead"]/tbody/tr[1]/td[7]')
    if responsavel_cell.text.strip():
        driver.implicitly_wait(10)
        
        

        # Get the first link
        first_link = driver.find_element(By.XPATH, '//*[@id="lsLead"]/tbody/tr[1]/td[1]/a')
        # Add the prefix to form the complete URL
        full_url = "https://myhonda.my.site.com" + first_link.get_attribute("href")

        # Open the link in a new tab
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(full_url)
        driver.implicitly_wait(10)
        # Now you're on the first user's profile page

        # Process the customer profile (e.g., update data, save changes, etc.)
        # ...

        # Close the current tab
        driver.close()

        # Switch back to the main window
    
        driver.switch_to.window(driver.window_handles[0])

        driver.implicitly_wait(10)
        # Repeat the process for the next customer
        process_customer_profile()

# Start processing the customer profiles
process_customer_profile()

# Close the WebDriver when done
driver.quit()









//*[@id="ext-gen42"]




import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def baixar_arquivo(url, caminho):
    try:
        download = requests.get(url)
        if download.status_code == 200:
            with open(caminho, 'wb') as f:
                f.write(download.content)
            print(f"Arquivo baixado com sucesso: {caminho}")
        else:
            print(f"Falha ao baixar o arquivo. Status code: {download.status_code}")
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")

def fazer_tr(driver):
    try:
        # Encontra os elementos link1 e link2
        driver.switch_to.frame('openCaseFrame')
        sleep(1)
        link1 = driver.find_element(By.XPATH, '//*[@id="novaCNHDigitalizada"]/div[2]/div/div[2]/a').get_attribute('href')
        link2 = driver.find_element(By.XPATH, '//*[@id="novoTermoResponsabilidade"]/div[2]/div/div[2]/a').get_attribute('href')
        
        # Verifica se ambos os links possuem conteúdo
        if link1 and link2:
            print("Ambos os campos possuem conteúdo:")
            caminho_termo = os.path.join(r"C:\Users\victor.dantas\Desktop\hellou\termos_baixados", "termo_adriano.pdf")
            caminho_cnh = os.path.join(r"C:\Users\victor.dantas\Desktop\hellou\cnh_baixados", "cnh_adriano.pdf")
            baixar_arquivo(link1, caminho_cnh)
            baixar_arquivo(link2, caminho_termo)
        elif link1:
            print("Somente o campo 1 possui conteúdo.")
            caminho_cnh = os.path.join(r"C:\Users\victor.dantas\Desktop\hellou\cnh_baixados", "cnh_adriano.pdf")
            baixar_arquivo(link1, caminho_cnh)
        elif link2:
            print("Somente o campo 2 possui conteúdo.")
            caminho_termo = os.path.join(r"C:\Users\victor.dantas\Desktop\hellou\termos_baixados", "termo_adriano.pdf")
            baixar_arquivo(link2, caminho_termo)
        else:
            print("Ambos os campos estão vazios.")
    except NoSuchElementException:
        print("Um ou mais links não encontrados.")

































import os
from selenium import webdriver
import requests
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from PIL import Image
from pdf2image import convert_from_path
from pdf2image.exceptions import *
import pytesseract

def ler_arquivo(caminho_imagem):
    try:
        # Abre a imagem
        img = Image.open(caminho_imagem)
        # Usa o Tesseract para extrair o texto
        texto_extraido = pytesseract.image_to_string(img, lang='por')
        return texto_extraido.strip()
    except Exception as e:
        print(f"Erro ao extrair texto da imagem: {e}")
        return None

def verificar_cpf_no_texto(texto_imagem1, texto_imagem2, cpf_cliente):
    # Extrai apenas os números do CPF
    cpf_numeros = ''.join(filter(str.isdigit, cpf_cliente))
    
    # Verifica a presença do CPF nos textos extraídos das duas imagens
    if cpf_numeros in texto_imagem1 and cpf_numeros in texto_imagem2:
        print("aprovado")
    else:
        print("recusado")


def gerar_caminho_destino(tipo_documento, nome_arquivo):
    # Define o diretório base com base no tipo de documento
    if tipo_documento == "cnh":
        caminho_base = "C:\\Users\\victor.dantas\\Desktop\\hellou\\cnh_convertidos"
    elif tipo_documento == "termo":
        caminho_base = "C:\\Users\\victor.dantas\\Desktop\\hellou\\termos_convertidos"
    else:
        raise ValueError("Tipo de documento inválido")

    # Remove a extensão e adiciona ".jpg"
    nome_arquivo_sem_ext = os.path.splitext(nome_arquivo)[0]
    caminho_completo = f"{caminho_base}\\{nome_arquivo_sem_ext}.jpg"
    
    return caminho_completo

def baixar_arquivo(url, caminho, driver):
    try:
        # Obtém os cookies do Selenium
        cookies = driver.get_cookies()
        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])
        
        # Faz a requisição usando a sessão com os cookies
        download = session.get(url)
        
        if download.status_code == 200:
            with open(caminho, 'wb') as f:
                f.write(download.content)
            print(f"Arquivo baixado com sucesso: {caminho}")
        else:
            print(f"Falha ao baixar o arquivo. Status code: {download.status_code}")
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")

def converter_arquivo(caminho_origem, caminho_destino):
    # Obtém o nome do arquivo na pasta de origem
    arquivo = os.listdir(caminho_origem)[0]
    caminho_do_poppler = r'C:\Users\victor.dantas\Desktop\hellou\poppler\poppler-24.11.0'
    caminho_arquivo = os.path.join(caminho_origem, arquivo)

    try:
        if arquivo.lower().endswith('.pdf'):
            # Converte PDF para JPEG, assumindo uma única página
            imagens = convert_from_path(caminho_arquivo, poppler_path=caminho_do_poppler)
            
            # Verifica se há mais de uma página
            if len(imagens) > 1:
                print(f"Erro: O arquivo {arquivo} tem mais de uma página.")
                return

            # Salva a única página como JPEG
            img = imagens[0]
            caminho_saida = os.path.join(caminho_destino, os.path.splitext(arquivo)[0] + '.jpg')
            img.save(caminho_saida, 'JPEG')
            print(f"Salvo: {caminho_saida}")

        else:
            # Converte qualquer outra imagem para JPEG
            img = Image.open(caminho_arquivo)
            caminho_saida = os.path.join(caminho_destino, os.path.splitext(arquivo)[0] + '.jpg')
            img.convert('RGB').save(caminho_saida, 'JPEG')
            print(f"Salvo: {caminho_saida}")

        # Deleta o arquivo original
        if os.path.isfile(caminho_arquivo):
            os.remove(caminho_arquivo)
            print(f"Arquivo original deletado: {caminho_arquivo}")

    except Exception as e:
        print(f"Erro na conversão: {e}")

def fazer_tr(driver):
    # Encontra os elementos download_cnh e download_termo
    driver.switch_to.frame('openCaseFrame')
    sleep(1)
    download_cnh = driver.find_element(By.XPATH, '//*[@id="novaCNHDigitalizada"]/div[2]/div/div[2]/a').get_attribute('href')
    download_termo = driver.find_element(By.XPATH, '//*[@id="novoTermoResponsabilidade"]/div[2]/div/div[2]/a').get_attribute('href')
    
    # Diretórios de destino
    origem_termo = "C:\\Users\\victor.dantas\\Desktop\\hellou\\termos_baixados"
    origem_cnh = "C:\\Users\\victor.dantas\\Desktop\\hellou\\cnh_baixados"
    conv_termo = "C:\\Users\\victor.dantas\\Desktop\\hellou\\termos_convertidos"
    conv_cnh = "C:\\Users\\victor.dantas\\Desktop\\hellou\\cnh_convertidos"
    
    # Nomes dos arquivos
    nome_cnh = driver.find_element(By.XPATH, '//*[@id="novaCNHDigitalizada"]/div[2]/div/div[2]/a/span').get_attribute('title')
    nome_termo = driver.find_element(By.XPATH, '//*[@id="novoTermoResponsabilidade"]/div[2]/div/div[2]/a/span').get_attribute('title')
    
    # Verifica se ambos os campos possuem conteúdo
    if download_cnh and download_termo:
        nomecliente = driver.find_element(By.XPATH, '//*[@id="clienteNome"]/div[2]/div[1]/span').get_attribute('title')
        print(f"Salvando arquivos do cliente {nomecliente}")
        cpf_cliente = driver.find_element(By.XPATH, '//*[@id="clienteCPF"]/div[2]/div[1]/span').get_attribute('title')
        print(f'o cpf do cliente é: {cpf_cliente}')
        
        # Caminho completo para salvar os arquivos
        caminho_cnh_completo = os.path.join(origem_cnh, nome_cnh)
        caminho_termo_completo = os.path.join(origem_termo, nome_termo)
        
        print(f"Baixando CNH: {download_cnh}")
        baixar_arquivo(download_cnh, caminho_cnh_completo, driver)
        print(f"Baixando Termo: {download_termo}")
        baixar_arquivo(download_termo, caminho_termo_completo, driver)
        print('convertendo arquivos...')
        
        # Chamar as funções de conversão com os caminhos corretos
        converter_arquivo(origem_termo, conv_termo)
        sleep(2)
        converter_arquivo(origem_cnh, conv_cnh)

        return cpf_cliente  # Retorna o cpf_cliente para o main
    
    else:
        print("Um ou mais links não encontrados. Clicando no botão não lançar...")
        driver.find_element(By.XPATH, '//*[@id="form[confirmaLancamento]"]').click()
        return None

def check_tr(driver):
    try:
        # Encontre o elemento usando o XPath
        driver.switch_to.frame('casesFrame')
        sleep(1)
        driver.switch_to.frame('casesSubFrame')
        sleep(1)
        elemento = driver.find_element(By.XPATH, '//*[@id="ext-gen32"]/div[1]/table/tbody/tr/td[6]/div')
        sleep(2)
        # Verifique o texto do elemento
        if elemento.text == "Teste Ride":
            print("Teste Ride encontrado.")
            sleep(1)
            driver.find_element(By.CLASS_NAME, "x-grid3-row-first").click()
            sleep(1)
            driver.find_element(By.XPATH, '//*[@id="ext-gen42"]').click()
            sleep(5)
            fazer_tr(driver)
        else:
            print("Não há seguros na primeira linha, filtrando...")
            sleep(1)
            campo_texto = driver.find_element(By.XPATH, '//*[@id="ext-comp-1005"]')
            sleep(1)
            campo_texto.send_keys("Teste Ride")
            sleep(2)
            campo_texto.send_keys(Keys.ENTER)
            sleep(1)
            driver.find_element(By.XPATH, '//*[@id="ext-gen75"]').click()
            sleep(3)
            elemento = driver.find_element(By.XPATH, '//*[@id="ext-gen32"]/div[1]/table/tbody/tr/td[6]/div')
            if elemento.text == "Teste Ride":
                print("Teste Ride encontrado.")
                sleep(1)
                driver.find_element(By.CLASS_NAME, "x-grid3-row-first").click()
                sleep(1)
                driver.find_element(By.XPATH, '//*[@id="ext-gen42"]').click()
                sleep(5)
                fazer_tr(driver)
            else:
                print("não há Teste Rides")
                quit()
        
    except NoSuchElementException:
        print("Elemento não encontrado. Verifique o XPath ou a estrutura da página.")

# função principal, roda o resto das funções e o código inteiro
def main():
    # Abre o chrome e acessa o Processmaker.
    print("Abrindo o Processmaker no Chrome...")
    # Configura o chrome para rodar headless.
    options = Options()
    # options.add_argument('--headless=new')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    url = "http://10.1.1.57/sysfreedom/en/neoclassic/login/login"
    driver.get(url)
    # deixa o navegador em tela cheia
    driver.maximize_window()
    # Acha e insere os dados de log-in.
    print("Inserindo dados de log-in")
    
    username = driver.find_element(By.ID, "form[USR_USERNAME]").send_keys("victor.dantas")
    password = driver.find_element(By.ID, "form[USR_PASSWORD_MASK]").send_keys("Freedom.23")
    sleep(2)
    login_button = driver.find_element(By.ID, "form[BSUBMIT]").click()
    sleep(5)
    check_tr(driver)
    sleep(2)
    
    # Chama fazer_tr e obtém o cpf_cliente
    cpf_cliente = fazer_tr(driver)

    if cpf_cliente:  # Verifica se cpf_cliente foi retornado
        # Obtém os nomes dos arquivos
        nome_cnh = driver.find_element(By.XPATH, '//*[@id="novaCNHDigitalizada"]/div[2]/div/div[2]/a/span').get_attribute('title')
        nome_termo = driver.find_element(By.XPATH, '//*[@id="novoTermoResponsabilidade"]/div[2]/div/div[2]/a/span').get_attribute('title')

        # Define os caminhos de destino usando a função de geração
        caminho_cnh_destino = gerar_caminho_destino("cnh", nome_cnh)
        caminho_termo_destino = gerar_caminho_destino("termo", nome_termo)

        # Extrai o texto das imagens
        texto_cnh = ler_arquivo(caminho_cnh_destino)
        texto_termo = ler_arquivo(caminho_termo_destino)
        
        # Verifica o CPF nos textos extraídos
        verificar_cpf_no_texto(texto_cnh, texto_termo, cpf_cliente)
    else:
        print("Erro: CPF do cliente não encontrado.")

if __name__ == "__main__":
    main()
