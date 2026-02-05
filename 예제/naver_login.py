import re
import random
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright):
    # 1. 브라우저 실행 시 '최대화' 인자를 추가합니다.
    browser = playwright.chromium.launch(
        headless=False, 
        args=["--start-maximized"], slow_mo=1000
    )
    
    # 2. viewport를 None으로 설정해야 브라우저 크기에 맞춰 화면이 꽉 찹니다.
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

    # 모든 동작 사이 1초 딜레이
    # browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    # context = browser.new_context(ignore_https_errors=True)
    # page = context.new_page()

# 홈페이지로 이동
    page.goto("https://www.naver.com/")
    page.get_by_role("link", name="NAVER 로그인").click()
    page.get_by_role("textbox", name="아이디 또는 전화번호").click()
    page.get_by_role("textbox", name="아이디 또는 전화번호").fill("소혜미님의기강문제")
    page.wait_for_timeout(9999999)
    page.pause()
#     page.get_by_role("button", name="실시간 예약").click()
#     page.locator("#user_id").click()
#     page.locator("#user_id").fill("damian")
#     page.locator("#user_pw").click()
#     page.locator("#user_pw").fill("****")
#     page.locator("#section").get_by_role("button", name="로그인").click()

# # 아카데미 메뉴 선택
#     page.get_by_role("button", name="아카데미").first.hover()
# # About us 메뉴 선택
#     page.locator("#sc-lc-wrap1").get_by_text("About us").dispatch_event("click")
#     # page.get_by_role("link", name="About us").first.dispatch_event("click")
#     # page.get_by_text("About us").dispatch_event("click")
# # About us 메뉴 하방 스크롤
#     current_pos = 0
#     while True:
#         page.mouse.wheel(0, 500) 
#         current_pos += 500
#         page.wait_for_timeout(300) 
#         total_height = page.evaluate("document.body.scrollHeight")
#         if current_pos >= total_height:
#             break

# # About us 메뉴 상방 스크롤
#     current_pos = page.evaluate("window.pageYOffset")
#     while current_pos > 0:
#         page.mouse.wheel(0, -500)  # 위로 500픽셀 스크롤 (음수 사용)
#         current_pos -= 500
#         page.wait_for_timeout(300) # 동작 확인을 위한 대기
#         # 0보다 작아지면(맨 위 도달) 멈춤
#         if current_pos <= 0:
#             break

#     page.wait_for_timeout(9999999) 
# # 아카


# # # 랜덤 강사 선택
# #     coaches = page.locator("#coachArea h2").filter(has_not_text="최종환")
# #     coach_count = coaches.count()

# #     if coach_count > 0:
# #         random_index = random.randint(0, coach_count - 1)
# #         target_coach = coaches.nth(random_index)

# #         target_coach.click(force=True)
# #         print(f"랜덤 선택된 강사: {target_coach.inner_text()}")
# #     else:
# #         print("강사 목록을 불러오지 못했습니다. 페이지 로딩을 확인해주세요.")

# # # 랜덤 날짜 선택
# #     page.wait_for_selector("li.possible-date", state="visible", timeout=5000)
# #     available_dates = page.locator("ul.calendar-day-body li.possible-date")
# #     available_date_count = available_dates.count()

# #     if available_date_count > 0:
# #         random_index = random.randint(0, available_date_count -1)
# #         target_date = available_dates.nth(random_index)

# #         date_info = target_date.get_attribute("data-date")

# #         target_date.click(force=True)
# #         print(f"랜덤 선택된 날짜: {target_date.inner_text()}")
# #     else:
# #         print("시간을 선택하지 못했습니다. 날짜 선택 상태를 확인해주세요.")

# # # 랜덤 시간 선택
# #     # 1. 'disable' 클래스가 포함되지 않은 시간 요소들만 찾습니다.
# #     # timeArea 안에서 class에 'disable'이 없는 p 태그를 모두 가져옵니다.
# #     available_times = page.locator("#timeArea p:not(.disable)")

# #     count = available_times.count()

# #     if count > 0:
# #         random_index = random.randint(0, count - 1)
# #         target_time = available_times.nth(random_index)
# #         target_time.click(force=True)
# #     else:
# #         print(f"시간을 선택하지 못했습니다. 시간 선택 상태를 확인해주세요.")

# # # 다음단계 버튼 선택
# #     page.get_by_text("다음단계").click()
# #     page.locator("#productBtn32").click()
# #     page.get_by_role("button", name="다음 단계").click()
# #     page.get_by_text("신용카드&간편결제").click()
# #     page.get_by_role("button", name="결제하기").click()
# #     page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("link", name="토스페이").click()
# #     page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("checkbox", name="[필수] 서비스 이용 약관, 개인정보 처리 동의").check()
# #     page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("button", name="다음-토스페이 결제").click()
    
#     page.pause()

# #     # ---------------------
# #     # context.close()
# #     # browser.close()


with sync_playwright() as playwright:
    run(playwright)
