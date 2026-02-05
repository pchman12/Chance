import re
import random
import os
from playwright.sync_api import Playwright, sync_playwright, expect
from dotenv import load_dotenv

load_dotenv()

def run(playwright):
    # 환경 변수에서 아이디와 비밀번호 가져오기
    # os.getenv("변수명")을 사용합니다.
    user_id_val = os.getenv("USER_ID")
    user_pw_val = os.getenv("USER_PW")
    
    # 창 최대화 추가 및 모든 동작 사이 1초 딜레이
    browser = playwright.chromium.launch(
        headless=False, 
        args=["--start-maximized"], slow_mo=2000
    )
    
    context = browser.new_context(no_viewport=True, ignore_https_errors=True)
    page = context.new_page()

    # # 3. 페이지 이동 후 스크롤 로직 수행
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
    page.locator("#section").get_by_text("필드 퍼팅 컨디셔닝").scroll_into_view_if_needed()
    page.locator("#section").get_by_text("필드 퍼팅 컨디셔닝").click()
    # page.get_by_role("link", name="필드 퍼팅 컨디셔닝").scroll_into_view_if_needed()
    # page.get_by_role("link", name="필드 퍼팅 컨디셔닝").click()

    # 랜덤 강사 선택
    coaches = page.locator("#coachArea h2").filter(has_not_text=re.compile(r"최종환|배후영|천승록"))
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
    
# 랜덤 시간 선택은 필드 퍼팅 컨디셔닝에선 사용 하지 않음.
    # 1. 'disable' 클래스가 포함되지 않은 시간 요소들만 찾습니다.
    # timeArea 안에서 class에 'disable'이 없는 p 태그를 모두 가져옵니다.
    # available_times = page.locator("#timeArea p:not(.disable)")

    # count = available_times.count()

    # if count > 0:
    #     random_index = random.randint(0, count - 1)
    #     target_time = available_times.nth(random_index)
    #     target_time.click(force=True)
    # else:
    #     print(f"시간을 선택하지 못했습니다. 시간 선택 상태를 확인해주세요.")
    

    # 다음단계 버튼 선택
    page.get_by_text("다음단계").click()
    page.get_by_role("button", name="다음 단계").click()
    page.get_by_text("토스").click()
    # 결제하기 버튼 선택
    page.get_by_role("button", name="결제하기").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="결제하기").click()
  
    # payletter 결제 창으로 권한을 변경
    pages = context.pages
    print(pages)
    payletter_toss = page1_info.value
    payletter_toss = pages[-1]

    # payletter 동의
    payletter_toss.get_by_text("모두 동의합니다.").click()
    payletter_toss.get_by_text("동의하고 넘어가기").click()
    
    # payletter 결제 방식(머니/포인트결제) 선택
    payletter_toss.get_by_text("머니/포인트결제").click()
   
   # 이메일 주소 변경
    payletter_toss.get_by_role("textbox", name="이메일").click()
    payletter_toss.get_by_role("textbox", name="이메일").fill("")
    payletter_toss.get_by_role("textbox", name="이메일").fill("damian@vrotein.co.kr")
    
    # QR 코드 화면 이동
    payletter_toss.get_by_text("다음").click()
    
    # QR코드 대기
    page.wait_for_timeout(9999999)    
    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
