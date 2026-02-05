import random
import os
from playwright.sync_api import sync_playwright
import playwright_stealth

def run_bypass():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        user_name = os.getlogin()
        user_data_path = f"C:/Users/Park/AppData/Local/Google/Chrome/User Data/Default"
        # 실제 사용자와 동일한 환경 구축
        context = browser.new_context(
            no_viewport=True,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        # 언어와 플랫폼 정보를 일반 PC처럼 속입니다.
        locale="ko-KR",
        timezone_id="Asia/Seoul",
        extra_http_headers={
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
    }
)
        page = context.new_page()
        
        # 스텔스 적용 (함수 직접 호출 방식)
        try:
            from playwright_stealth.stealth import stealth_sync
            stealth_sync(page)
        except:
            pass 

        # 봇 탐지 회피를 위한 랜덤 대기 후 접속
        page.wait_for_timeout(random.uniform(2000, 4000))
        page.goto("https://www.naver.com")
        page.pause()        
        # print("현재 화면을 확인하세요. 차단 문구가 없다면 성공입니다!")
        # input("다음 단계로 넘어가려면 엔터를 누르세요...")
        # browser.close()

if __name__ == "__main__":
    run_bypass()