import time
import g4f
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import subprocess

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = "https://ngl.link/f.d20226/"

messages = [];

def get_ai_response():
    response = g4f.ChatCompletion.create(
        model=g4f.models.Phi_3_mini_4k_instruct,
        messages=[{"role": "user", "content": f"Donne moi une phrase de drague pour une fille, tu peux y mettre des emojis et beaucoup de personalisation , de romantisme et d'autenticité. ta phrase ne doit pas faire partir de cette liste de messages {messages} "}],
    )
    return response

while True:
    try:
        driver.get(link)
        textarea = driver.find_element(By.TAG_NAME, "textarea")
        textarea.click()
        time.sleep(1)
        msg = get_ai_response()
        print(f"=> {msg}\n")
        textarea.send_keys(msg)
        button = driver.find_element(By.TAG_NAME, "button")
        button.click()
        messages.append(msg)
        
        with open("messages.txt", "w") as f:
            for item in messages:
                f.write("%s\n" % item)

        time.sleep(1)
    except Exception as e:
        continue
        

            
        
    

# if __name__ == "__main__":
#     r = get_ai_response()
#     print(r)