import time
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

class TourputtTest:
    def __init__(self):
        # 1. 초기 데이터 설정 (환경 변수 등)
        self.user_id = os.getenv("USER_ID")
        self.user_pw = os.getenv("USER_PW")
        self.server_url = 'http://127.0.0.1:4723'
        self.driver = None

    def _get_options(self):
        """에뮬레이터 및 앱 실행 옵션 정의"""
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.automation_name = 'UiAutomator2'
        options.device_name = 'emulator-5554'
        options.app_package = 'com.vrotein.tourputtpersonal'
        options.app_activity = 'com.unity3d.player.UnityPlayerActivity'
        
        # 키보드 및 앱 상태 유지 설정
        options.set_capability("appium:resetKeyboard", False)
        options.set_capability("appium:unicodeKeyboard", False)
        options.no_reset = True 
        options.full_reset = False
        
        # Unity 앱 튕김 방지 및 안정성 설정
        options.set_capability("appium:dontStopAppOnReset", True)
        options.set_capability("appium:noSign", True)
        options.set_capability("appium:appWaitDuration", 30000)
        options.set_capability("appium:newCommandTimeout", 3600)
        
        return options

    def setup(self):
        """드라이버 연결 및 초기화"""
        print("Appium 서버에 연결 중...")
        self.driver = webdriver.Remote(self.server_url, options=self._get_options())
        
        # # 비밀번호를 클립보드에 복사
        # if self.user_pw:
        #     self.driver.set_clipboard_text(self.user_pw)
        #     print("비밀번호가 클립보드에 복사되었습니다.")
        return self.driver

    def Ranking_scroll_down(self):
        """아래에서 위로 Swipe하여 화면을 하단으로 스크롤"""
        if not self.driver:
            print("드라이버가 설정되지 않았습니다.")
            return

        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        # 좌표 설정: 아래(80%) -> 위(20%)
        center_x = 500
        area_top = 821
        area_bottom = 2115
        
        start_y = area_bottom - 100
        end_y = area_top + 100

        actions = ActionBuilder(self.driver)
        # 터치 입력을 'finger'라는 이름으로 생성
        finger = actions.add_pointer_input(interaction.POINTER_TOUCH, "finger")
        
        # 1. 시작 위치로 이동
        finger.create_pointer_move(duration=0, x=center_x, y=start_y)
        # 2. 화면 누르기 (button=0은 왼쪽 클릭/터치를 의미)
        finger.create_pointer_down(button=0)
        # 3. 목표 위치로 이동 (1초 동안 부드럽게)
        finger.create_pointer_move(duration=1000, x=center_x, y=end_y)
        # 4. 손가락 떼기
        finger.create_pointer_up(button=0)
        
        actions.perform()
        print("Ranking Page 스크롤 다운 동작 수행 완료")

    def Ranking_scroll_up(self):
        """아래에서 위로 Swipe하여 화면을 하단으로 스크롤"""
        if not self.driver:
            print("드라이버가 설정되지 않았습니다.")
            return

        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        # 좌표 설정: 아래(80%) -> 위(20%)
        center_x = 500
        area_top = 821
        area_bottom = 2115
        
        start_y = area_top + 100
        end_y = area_bottom - 100

        actions = ActionBuilder(self.driver)
        # 터치 입력을 'finger'라는 이름으로 생성
        finger = actions.add_pointer_input(interaction.POINTER_TOUCH, "finger")
        
        # 1. 시작 위치로 이동
        finger.create_pointer_move(duration=0, x=center_x, y=start_y)
        # 2. 화면 누르기 (button=0은 왼쪽 클릭/터치를 의미)
        finger.create_pointer_down(button=0)
        # 3. 목표 위치로 이동 (1초 동안 부드럽게)
        finger.create_pointer_move(duration=1000, x=center_x, y=end_y)
        # 4. 손가락 떼기
        finger.create_pointer_up(button=0)
        
        actions.perform()
        print("Ranking Page 스크롤 업 동작 수행 완료")

    def teardown(self):
        """테스트 종료 및 세션 닫기"""
        if self.driver:
            self.driver.quit()
            print("세션이 종료되었습니다.")

    def previous_scroll_down(self):
        """아래에서 위로 Swipe하여 화면을 하단으로 스크롤"""
        if not self.driver:
            print("드라이버가 설정되지 않았습니다.")
            return

        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        # 좌표 설정: 아래(80%) -> 위(20%)
        center_x = 500
        area_top = 553
        area_bottom = 2115
        
        start_y = area_bottom - 100
        end_y = area_top + 100

        actions = ActionBuilder(self.driver)
        # 터치 입력을 'finger'라는 이름으로 생성
        finger = actions.add_pointer_input(interaction.POINTER_TOUCH, "finger")
        
        # 1. 시작 위치로 이동
        finger.create_pointer_move(duration=0, x=center_x, y=start_y)
        # 2. 화면 누르기 (button=0은 왼쪽 클릭/터치를 의미)
        finger.create_pointer_down(button=0)
        # 3. 목표 위치로 이동 (1초 동안 부드럽게)
        finger.create_pointer_move(duration=1000, x=center_x, y=end_y)
        # 4. 손가락 떼기
        finger.create_pointer_up(button=0)
        
        actions.perform()
        print("Previous Page 스크롤 다운 동작 수행 완료")

    def previous_scroll_up(self):
        """위에서 아래로 Swipe하여 화면을 상단으로 스크롤"""
        if not self.driver:
            print("드라이버가 설정되지 않았습니다.")
            return

        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        # 좌표 설정: 아래(80%) -> 위(20%)
        center_x = 500
        area_top = 700
        area_bottom = 1900
        
        start_y = area_top + 100
        end_y = area_bottom - 100

        actions = ActionBuilder(self.driver)
        # 터치 입력을 'finger'라는 이름으로 생성
        finger = actions.add_pointer_input(interaction.POINTER_TOUCH, "finger")
        
        # 1. 시작 위치로 이동
        finger.create_pointer_move(duration=0, x=center_x, y=start_y)
        # 2. 화면 누르기 (button=0은 왼쪽 클릭/터치를 의미)
        finger.create_pointer_down(button=0)
        # 3. 목표 위치로 이동 (1초 동안 부드럽게)
        finger.create_pointer_move(duration=600, x=center_x, y=end_y)
        # 4. 손가락 떼기
        finger.create_pointer_up(button=0)
        
        actions.perform()
        print("Previous Page 스크롤 업 동작 수행 완료")
    
# --- 실행부 ---
if __name__ == "__main__":
    tester = TourputtTest()
    try:
        driver = tester.setup()
        
        # View All 선택
        time.sleep(3)
        driver.tap([(919, 517)])
       
        # Information(?) 버튼 선택
        time.sleep(3)
        driver.tap([(319, 495)])

        # Information(?) 팝업 닫기
        time.sleep(3)
        driver.tap([(936, 383)])

        # Raking Space 최하단까지 Scroll
        time.sleep(3)
        tester.Ranking_scroll_down()
        tester.Ranking_scroll_down()

        # Raking Space 최상단까지 Scroll
        time.sleep(3)
        tester.Ranking_scroll_up()
        tester.Ranking_scroll_up()

        # Previous 선택
        time.sleep(3)
        driver.tap([(939, 374)])
        
        # Raking Space 최하단까지 Scroll
        time.sleep(3)
        tester.previous_scroll_down()
        tester.previous_scroll_down()

        # Raking Space 최상단까지 Scroll
        time.sleep(3)
        tester.previous_scroll_up()
        tester.previous_scroll_up()

    except Exception as e:
        print(f"테스트 중 에러 발생: {e}")
    # finally:
    #     tester.teardown()