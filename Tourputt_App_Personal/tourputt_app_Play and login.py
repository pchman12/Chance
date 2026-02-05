import time
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv

load_dotenv()


def run_tourputt_test():
    # 환경 변수에서 아이디와 비밀번호 가져오기
    # os.getenv("변수명")을 사용합니다.
    user_id_val = os.getenv("USER_ID")
    user_pw_val = os.getenv("USER_PW")

    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.automation_name = 'UiAutomator2'
    options.device_name = 'emulator-5554'
    options.app_package = 'com.vrotein.tourputtpersonal'
    options.app_activity = 'com.unity3d.player.UnityPlayerActivity'
    options.set_capability("appium:resetKeyboard", False)
    options.set_capability("appium:unicodeKeyboard", False)
    
    # 앱 상태 유지
    options.no_reset = True 
    options.full_reset = False
    options.set_capability("appium:dontStopAppOnReset", True)
    options.set_capability("appium:noSign", True)
    options.set_capability("appium:appWaitDuration", 30000)
    options.set_capability("appium:newCommandTimeout", 3600)
 
    appium_server_url = 'http://127.0.0.1:4723'

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.set_clipboard_text(os.getenv("USER_PW"))
    
    try:
        print("TOURPUTT 앱을 직접 실행합니다...")
        driver = webdriver.Remote(appium_server_url, options=options)
        print("TOURPUTT 실행 성공!")

        user_pw = os.getenv("USER_PW")
        
    # Continue with another method 선택
        time.sleep(10)
        driver.tap([(530, 2239)])
        
    # Log in with ID 선택
        time.sleep(3)
        driver.tap([(525,1396)])

    # ID 입력 창 선택        
        time.sleep(3)
        driver.set_clipboard_text("")
        driver.tap([(157,696)])

    # ID 입력 
        time.sleep(3)
        ActionChains(driver).send_keys(user_id_val).perform()

    # 패스워드 입력 창 선택    
        time.sleep(3)
        driver.tap([(525,880)])
    
    # Password 입력
        time.sleep(3)
        driver.set_clipboard_text(user_pw_val)
        driver.press_keycode(50, 4096)
        # ActionChains(driver).send_keys(user_pw_val).perform()

    # 로그인 버튼 선택
        time.sleep(3)
        driver.tap([(516,1083)])

    # 로그인 성공 팝업 선택
        time.sleep(3)
        driver.tap([(525,1354)])

    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    run_tourputt_test()