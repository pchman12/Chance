import re
import random
import os
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from dotenv import load_dotenv

load_dotenv()

def run(playwright):
    # # 1. 사용자 데이터를 저장할 폴더 (실제 브라우저처럼 쿠키/세션/배율 유지용)
    user_data_path = os.path.join(os.getcwd(), "chrome_profile")

    # 환경 변수에서 아이디와 비밀번호 가져오기
    # os.getenv("변수명")을 사용합니다.
    user_id_val = os.getenv("USER_ID")
    user_pw_val = os.getenv("USER_PW")

    # 창 최대화 추가 및 모든 동작 사이 2초 딜레이
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=user_data_path,
        channel="chrome",           # 실제 크롬 실행
        headless=False,
        no_viewport=True,           # 중요: 고정 해상도 해제
        ignore_https_errors=True,
        slow_mo=2000,
        args=["--start-maximized", "--force-device-scale-factor=0.8"]    # Resource 크기 0.8 비율 조정
            
        )

    # context = browser.new_context(no_viewport=True, viewport=None, ignore_https_errors=True)

    if len(context.pages) > 0:
        page = context.pages[0]
    else:
        page = context.new_page()

    # 1. Chrome Broswer 자체 팝업 발생 시, 확인 버튼 선택
    def handle_dialog_combined(dialog):
        print(f"⚠️ 브라우저 팝업 발생: {dialog.message}")
        
        # 3초 동안 화면을 유지하며 사용자가 볼 시간을 줍니다.
        time.sleep(3) 
        
        # 'dialog' 변수는 이 함수 안에서만 유효합니다. 반드시 들여쓰기를 맞춰야 합니다!
        dialog.accept() 
        print("✅ 3초 대기 후 자동으로 확인 버튼을 눌렀습니다.")

    # 2. 핸들러를 등록합니다.
    page.on("dialog", handle_dialog_combined)

    # 3. 페이지 이동 후 스크롤 로직 수행
    # current_pos = 0
    # while True:
    #     page.mouse.wheel(0, 500) 
    #     current_pos += 500
    #     page.wait_for_timeout(300) 
    #     total_height = page.evaluate("document.body.scrollHeight")
    #     if current_pos >= total_height:
    #         break

# 홈페이지로 이동
    page.goto("https://academy.vrotein.co.kr/")
    page.get_by_role("button", name="실시간 예약").click()
    page.locator("#user_id").click()
    page.locator("#user_id").fill(user_id_val)
    page.locator("#user_pw").click()
    page.locator("#user_pw").fill(user_pw_val)
    page.locator("#section").get_by_role("button", name="로그인").click()

# 프로그램 선택
    page.get_by_text("아마추어 개인 레슨").click()


# 랜덤 강사 선택
    coaches = page.locator("#coachArea h2").filter(has_not_text="최종환")
    coach_count = coaches.count()

    if coach_count > 0:
        random_index = random.randint(0, coach_count - 1)
        target_coach = coaches.nth(random_index)

        target_coach.click(force=True)
        print(f"랜덤 선택된 강사: {target_coach.inner_text()}")
    else:
        print("강사 목록을 불러오지 못했습니다. 페이지 로딩을 확인해주세요.")

# 랜덤 날짜 선택
    page.wait_for_selector("li.possible-date", state="visible", timeout=5000)
    available_dates = page.locator("ul.calendar-day-body li.possible-date")
    available_date_count = available_dates.count()

    if available_date_count > 0:
        random_index = random.randint(0, available_date_count -1)
        target_date = available_dates.nth(random_index)

        date_info = target_date.get_attribute("data-date")

        target_date.click(force=True)
        print(f"랜덤 선택된 날짜: {target_date.inner_text()}")
    else:
        print("시간을 선택하지 못했습니다. 날짜 선택 상태를 확인해주세요.")

# 랜덤 시간 선택
    # 1. 'disable' 클래스가 포함되지 않은 시간 요소들만 찾습니다.
    # timeArea 안에서 class에 'disable'이 없는 p 태그를 모두 가져옵니다.
    available_times = page.locator("#timeArea p.reservation-time:not(.pass-time)")
    page.wait_for_timeout(500)
    count = available_times.count()

    if count > 0:
        random_index = random.randint(0, count - 1)
        target_time = available_times.nth(random_index)
        target_time.click(force=True)
    else:
        print(f"시간을 선택하지 못했습니다. 시간 선택 상태를 확인해주세요.")

# 다음단계 버튼 선택
    page.get_by_text("다음단계").click()
# 이용권 선택
    page.locator("#productBtn31").click()
# 예약하기 버튼 선택
    page.get_by_role("button", name="예약하기").first.click()

# 팝업 내 예약 하기 버튼 선택
    page.locator("#popArea").get_by_role("button", name="예약하기").click()

# 예약 확인/변경 버튼 선택
    page.get_by_role("button", name="예약확인/변경").click()

# 예약취소 버튼 선택
    page.get_by_role("button", name="예약취소").click()
    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(9999999)

with sync_playwright() as playwright:
    run(playwright)
