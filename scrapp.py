
# from selenium.webdriver import Remote, ChromeOptions
# from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
# from bs4 import BeautifulSoup


# SBR_WEBDRIVER = 'https://brd-customer-hl_fc6b1f7b-zone-scraping_browser1:n5j1ffnzeb7b@brd.superproxy.io:9515'
# def scrape_website(website):
#     print("Launching EDGE...")

#     sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
#     with Remote(sbr_connection, options=ChromeOptions()) as driver:
        
#         driver.get(website)
        
#         print('Waiting captcha to solve...')
#         solve_res = driver.execute('executeCdpCommand', {
#             'cmd': 'Captcha.waitForSolve',
#             'params': {'detectTimeout': 10000},
#         })
#         print('Captcha solve status:', solve_res['value']['status'])
#         print('Navigated! Scraping page content...')
#         html = driver.page_source
#         return html


#we are no longer using 3rd party browser for scraping with captcha required websites and above code works for that


# import selenium.webdriver as webdriver
# from selenium.webdriver.edge.service import Service
# import time
# from bs4 import BeautifulSoup

# def scrape_website(website):
#     print("Launching EDGE...")

#     Edge_driver_path = "./msedgedriver.exe"
#     options = webdriver.EdgeOptions()
#     driver = webdriver.Edge(service=Service(Edge_driver_path), options=options)

#     try:
#         driver = webdriver.Edge()
#         driver.get(website)
#         print("Spiders are weaving their web... Please wait while we gather the information for you!")
#         html = driver.page_source
#         time.sleep(4)
#         return html
#     finally:
#         driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching Chrome...")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(website)
        print("Spiders are weaving their web... Please wait while we gather the information for you!")
        html = driver.page_source
        time.sleep(4)
        return html
    finally:
        driver.quit()



def extract_body_content(html_content):
    soup = BeautifulSoup(html_content,"html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def cleanBC(body_content):               #will be filtering the unnecessary data

    soup = BeautifulSoup(body_content,"html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip() 
    )
    return cleaned_content


def split_dom_content(dom_content, max_length=6000):     #for our llm token size
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]

print("successful execution")