"""

1. Scrape all divs with class="MCDropDownBody collapse" into a txt file

 

Path: <div class="MCDropDown MCDropDown_Closed dropDown" > <div class="MCDropDownBody collapse" id="xxx">

 

is it possible to scrape if the ids are different for each collapsible?

 

2. Try scraping in Sources > Snippets of Inspect

 

var elements = document.querySelectorAll(<class?>);

for (const el of elements){

    el.click();

}

 

3. Because of zscaler proxy you must manually download check version/ chrome driver

4. Have to use firefox or safari because chrome is too new to download driver

"""

from selenium import webdriver

from selenium.webdriver.firefox.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.firefox import GeckoDriverManager

import time

 

# Setup Firefox driver

options = webdriver.FirefoxOptions()

options.headless = True  # Set False for debugging

 

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

driver.get(https://docs.saviyntcloud.com/bundle/EIC-FAQ/page/Content/FAQs.htm, verify=False) # set verify to false or include .pem

 

try:

    wait = WebDriverWait(driver, 10)

 

    # 1. Click all dropdown containers to expand

    drop_downs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.MCDropDown.MCDropDown_Closed.dropDown")))

    for dd in drop_downs:

        try:

            dd.click()

            time.sleep(0.3)  # small pause for animation

        except Exception as e:

            print(f"Could not click a dropdown: {e}")

 

    # 2. Grab all divs with class="MCDropDownBody collapse"

    bodies = driver.find_elements(By.CSS_SELECTOR, "div.MCDropDownBody.collapse")

 

    # 3. Write their inner text into a file

    with open("scraped_divs.txt", "w", encoding="utf-8") as f:

        for idx, body in enumerate(bodies, start=1):

            f.write(f"--- Div {idx} ---\n")

            f.write(body.text.strip())

            f.write("\n\n")

 

    print(f"Scraped {len(bodies)} divs into scraped_divs.txt")

 

finally:

    driver.quit()
