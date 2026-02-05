import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


# ChromeDriver 경로 설정
# driver_path = r"C:\Users\Park\파이썬자동화\tourputt/chromedriver.exe"
# service = Service(driver_path)
service = Service(ChromeDriverManager().install())
# Chrome 옵션 설정
chrome_options = Options()
# chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

# WebDriver 초기화
driver = webdriver.Chrome(service=service, options=chrome_options)
options = Options()

# url = "https://play.google.com/store/apps/details?id=com.vrotein.tourputtpersonal"
url = "https://www.tourputt.com/"

driver.get(url)
time.sleep(3)

#tourputt.com 메인페이지에서 More 버튼 위치로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(2): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#MORE 버튼 선택(ABOUT Page 접근)
more_button = driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/div[2]/div/div/div/div[2]/a[text()="MORE"]')
time.sleep(3)
more_button.click()
time.sleep(3)

#이전 페이지로 돌아가기
time.sleep(3)
driver.back()
time.sleep(3)

#TOURPUTT PRODUCT Page로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(1): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#TOURPUTT_CIRCLE 버튼 선택
time.sleep(3)
tourputt_circle_banner = driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/div[3]/div/div/div[2]/ul/li[1]/a')
tourputt_circle_banner.click()

#TOURPUTT_CIRCLE 버튼 이미지 전환
time.sleep(3)
tourputt_circle_image_button = driver.find_element(By.XPATH, '//button[text()="0"]')
tourputt_circle_image_button.click()
time.sleep(1)
tourputt_circle_image_button = driver.find_element(By.XPATH, '//button[text()="1"]')
tourputt_circle_image_button.click()
time.sleep(1)
tourputt_circle_image_button = driver.find_element(By.XPATH, '//button[text()="0"]')
tourputt_circle_image_button.click()
time.sleep(3)

# #HOW TO USE TOURPUTT 영상화면으로 이동
# body = driver.find_element(By.TAG_NAME, 'body')
# for _ in range(4): 
#     body.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.5)

# #HOW TO USE TOURPUTT 영상(Vimeo) 재생(막혔음.)
# how_to_use_video = driver.find_element(By.XPATH, '//*[@id="player"]/div[6]/div[7]/div[1]/button')
# how_to_use_video.click()

#TOURPUTT_CIRCLE 페이지 내 최하단으로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(10): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#이전 페이지로 돌아가기
time.sleep(3)
driver.back()
time.sleep(3)

#TOURPUTT_GROUND 버튼 선택
tourputt_ground_banner = driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/div[3]/div/div/div[2]/ul/li[2]/a')
tourputt_ground_banner.click()

#TOURPUTT_GROUND 버튼 이미지 전환
time.sleep(3)
tourputt_ground_image_button = driver.find_element(By.XPATH, '//button[text()="0"]')
tourputt_ground_image_button.click()
time.sleep(1)
tourputt_ground_image_button = driver.find_element(By.XPATH, '//button[text()="1"]')
tourputt_ground_image_button.click()
time.sleep(1)
tourputt_ground_image_button = driver.find_element(By.XPATH, '//button[text()="0"]')
tourputt_ground_image_button.click()
time.sleep(3)

#TOURPUTT_GROUND 페이지 내 최하단으로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(8): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#이전 페이지로 돌아가기
time.sleep(3)
driver.back()
time.sleep(3)

#TOURPUTT_BOX 버튼 선택
tourputt_box_banner = driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/div[3]/div/div/div[2]/ul/li[3]/a')
tourputt_box_banner.click()
time.sleep(3)

#TOURPUTT_BOX 페이지 내 최하단으로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(6): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#이전 페이지로 돌아가기
time.sleep(3)
driver.back()
time.sleep(3)

#CONTACT 버튼으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(3): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#CONTACT 버튼 선택
contact_button = driver.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/div[5]/div/div/div[3]/a[text()="CONTACT"]')
time.sleep(3)
contact_button.click()
time.sleep(3)

#CONTACT 페이지 입력창으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(1): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#CONTACT 페이지 성명 입력
contact_name = driver.find_element(By.ID, "writer_name")
contact_name.send_keys("박찬현")
time.sleep(3)

#CONTACT 페이지 연락처 입력
contact_phone_number = driver.find_element(By.ID, "writer_phone")
contact_phone_number.send_keys("01044252985")
time.sleep(3)

#CONTACT 페이지 이메일 입력
contact_email = driver.find_element(By.ID, "writer_email")
contact_email.send_keys("pchman1212@gmail.com")
time.sleep(3)

#CONTACT 페이지 내용 입력
contact_content = driver.find_element(By.CLASS_NAME, "c-textarea")
contact_content.send_keys("자동화 테스트 중입니다.")
time.sleep(3)

#투어펏을 알게 된 경로 택 1 선택
tourputt_known_route = driver.find_element(By.XPATH, '//input[@type="radio" and @value="인터넷 검색"]')
tourputt_known_route.click()
time.sleep(1.5)

tourputt_known_route = driver.find_element(By.XPATH, '//input[@type="radio" and @value="SNS(인스타그램, 페이스북 등)"]')
tourputt_known_route.click()
time.sleep(1.5)

tourputt_known_route = driver.find_element(By.XPATH, '//input[@type="radio" and @value="전단 또는 옥외광고"]')
tourputt_known_route.click()
time.sleep(1.5)

tourputt_known_route = driver.find_element(By.XPATH, '//input[@type="radio" and @value="신문 및 잡지광고"]')
tourputt_known_route.click()
time.sleep(1.5)

tourputt_known_route = driver.find_element(By.XPATH, '//input[@type="radio" and @value="브랜드 후원광고"]')
tourputt_known_route.click()
time.sleep(1.5)

tourputt_known_route = driver.find_element(By.XPATH, '//input[@type="radio" and @value="설치매장 방문"]')
tourputt_known_route.click()
time.sleep(1.5)

tourputt_known_route = driver.find_element(By.XPATH, '//input[@type="radio" and @value="지인추천"]')
tourputt_known_route.click()
time.sleep(1.5)

tourputt_known_route = driver.find_element(By.XPATH, '//input[@type="radio" and @value="ETC"]')
tourputt_known_route.click()
time.sleep(1.5)

#기타 입력창 입력
ETC_content = driver.find_element(By.ID, "path_detail")
ETC_content.send_keys("기타 입력창 자동화 테스트 중입니다.")
time.sleep(3)

#문의하기 버튼으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(1): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

# #문의하기 버튼 선택
# time.sleep(3)
# contact_us = driver.find_element(By.XPATH, '/html/body/div/form/div[1]/div/div/div/div[4]/a')
# contact_us.click()

#이전 페이지로 돌아가기
time.sleep(3)
driver.back()
time.sleep(3)

#ABOUT Page 접근
about_page = driver.find_element(By.XPATH, '/html/body/div/div/div/div/ul/li/a[text()="ABOUT"]')
about_page.click()
time.sleep(3)

#TOURPUTT App 다운로드 버튼으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(8): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#Google Playstore Store 버튼 선택
google_playstore_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[7]/div/div[1]/div[2]/a[1][text()="Google Play"]')
google_playstore_button.click()
time.sleep(3)

# 현재 창과 모든 창 핸들 가져오기
original_window = driver.current_window_handle
all_windows = driver.window_handles

# 새 창으로 전환
for window_handle in all_windows:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

#Google PlayStore 내 설치 버튼 선택
# google_play_setup_button = driver.find_element(By.CSS_SELECTOR, "button.VfPpkd-LgbsSe-OWXEXe-k8QpJ")
google_play_setup_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div/div[1]/div/div/div/div[1]/div/c-wiz/div/div/div/div/button')
google_play_setup_button.click()
time.sleep(3)

#Google PlayStore 로그인 팝업 발생 시, 닫기 버튼 선택
login_close = driver.find_element(By. XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/div[2]/div[4]/div')
login_close.click()
time.sleep(3)

#Google PlayStore 내 설치 버튼 재선택1
google_play_setup_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div/div[1]/div/div/div/div[1]/div/c-wiz/div/div/div/div/button')
google_play_setup_button.click()
time.sleep(3)

#Google Play Store 로그인 버튼 선택
google_play_login_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/div[3]/div/button[2]')
google_play_login_button.click()
time.sleep(3)

#이전 페이지로 돌아가기
time.sleep(3)
driver.back()
time.sleep(3)

#Google PlayStore 내 설치 버튼 재선택2
google_play_setup_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div/div[1]/div/div/div/div[1]/div/c-wiz/div/div/div/div/button')
google_play_setup_button.click()
time.sleep(3)

#Google PlayStore 취소 버튼 선택
google_play_cancel_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/div[3]/div/button[1]')
google_play_cancel_button.click()
time.sleep(3)

#TOURPUTT Google PlayStore App 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(3): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#Google Playstore App 브라우저 닫기
time.sleep(3)
driver.close()
time.sleep(3)

# 작업 후 다시 원래 창으로 전환
driver.switch_to.window(original_window)

#TOURPUTT iOS APP Store 버튼 선택
ios_appstore_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[7]/div/div[1]/div[2]/a[2]')
ios_appstore_button.click()
time.sleep(3)

# 현재 창과 모든 창 핸들 가져오기
original_window = driver.current_window_handle
all_windows = driver.window_handles

# 새 창으로 전환
for window_handle in all_windows:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

#TOURPUTT iOS Appstore 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(3): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#iOS App 브라우저 닫기
time.sleep(3)
driver.close()
time.sleep(3)

# 작업 후 다시 원래 창으로 전환
driver.switch_to.window(original_window)

#ABOUT Page 최하단으로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(3): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#PRODUCT내 TOURPUTT_CIRCLE Page 접근
product_circle_page = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/ul/li[2]/a[text()="PRODUCT"]')
product_circle_page.click()
time.sleep(3)

#PRODUCT CIRCLE Page 최하단으로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(10): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#PRODUCT Menu에 FOCUS ON 하기
product_menu_focus = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/ul/li[2]/a')

# ActionChains를 사용하여 마우스를 요소 위에 올림
actions = ActionChains(driver)
actions.move_to_element(product_menu_focus).perform()

#PRODUCT 내 TOURPUTT_GROUND Page 접근
product_ground_menu = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/ul/li[2]/ul/li[2]/a')
product_ground_menu.click()
time.sleep(3)

#PRODUCT GROUND Page 최하단으로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(8): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#PRODUCT Menu에 FOCUS ON 하기
product_menu_focus = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/ul/li[2]/a')

# ActionChains를 사용하여 마우스를 요소 위에 올림
actions = ActionChains(driver)
actions.move_to_element(product_menu_focus).perform()

#PRODUCT 내 TOURPUTT_BOX Page 접근
product_box_menu = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/ul/li[2]/ul/li[3]/a')
product_box_menu.click()
time.sleep(3)

#PRODUCT BOX Page 최하단으로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(6): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#PRODUCT Menu에 FOCUS ON 하기
product_menu_focus = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/ul/li[2]/a')

# ActionChains를 사용하여 마우스를 요소 위에 올림
actions = ActionChains(driver)
actions.move_to_element(product_menu_focus).perform()

#PRODUCT 내 TRAINING_AIDS Page 접근
product_training_aids_menu = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/ul/li[2]/ul/li[4]/a')
product_training_aids_menu.click()
time.sleep(3)

#THE ARC 상품으로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(3): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#THE ARC 구매하기 버튼 선택
the_arc_buy_button = driver.find_element(By. XPATH, '/html/body/div/div[2]/div/div/div[3]/div/div[1]/div[3]/a')
the_arc_buy_button.click()
time.sleep(3)

# 현재 창과 모든 창 핸들 가져오기
original_window = driver.current_window_handle
all_windows = driver.window_handles

# 새 창으로 전환
for window_handle in all_windows:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

#THE ARC 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(17): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#THE ARC 브라우저 닫기
time.sleep(3)
driver.close()
time.sleep(3)

# 작업 후 다시 원래 창으로 전환
driver.switch_to.window(original_window)

#THE IMPACT 상품으로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(1): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#THE IMPACT 구매하기 버튼 선택
the_impact_buy_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[3]/div/div[2]/div[3]/a')
the_impact_buy_button.click()
time.sleep(3)

# 현재 창과 모든 창 핸들 가져오기
original_window = driver.current_window_handle
all_windows = driver.window_handles

# 새 창으로 전환
for window_handle in all_windows:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

#THE IMPACT 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(17): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#THE IMPACT 브라우저 닫기
time.sleep(3)
driver.close()
time.sleep(3)

# 작업 후 다시 원래 창으로 전환
driver.switch_to.window(original_window)

#THE MAT 상품으로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(1): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#THE MAT 구매하기 버튼 선택
the_mat_buy_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[3]/div/div[3]/div[3]/a')
the_mat_buy_button.click()
time.sleep(3)

# 현재 창과 모든 창 핸들 가져오기
original_window = driver.current_window_handle
all_windows = driver.window_handles

# 새 창으로 전환
for window_handle in all_windows:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

#THE MAT 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(17): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#THE MAT 브라우저 닫기
time.sleep(3)
driver.close()
time.sleep(3)

# 작업 후 다시 원래 창으로 전환
driver.switch_to.window(original_window)

#THE TRACK 상품으로 이동
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(1): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#THE TRACK 구매하기 버튼 선택
the_track_buy_button = driver.find_element(By. XPATH, '/html/body/div/div[2]/div/div/div[4]/div/div/div[3]/a')
the_track_buy_button.click()
time.sleep(3)

# 현재 창과 모든 창 핸들 가져오기
original_window = driver.current_window_handle
all_windows = driver.window_handles

# 새 창으로 전환
for window_handle in all_windows:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

#THE TRACK 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(15): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#THE TRACK 브라우저 닫기
time.sleep(3)
driver.close()
time.sleep(3)

# 작업 후 다시 원래 창으로 전환
driver.switch_to.window(original_window)

#SERVICE Page 접근
service_page = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/ul/li[3]/a[text()="SERVICE"]')
service_page.click()
time.sleep(3)

#FAQ Banner 선택
faq_banner = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div[2]/a[1]')
faq_banner.click()

#FAQ No.1 선택
faq_number_1 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/ul/li[1]/a')
faq_number_1.click()
time.sleep(3)
faq_number_1.click()
time.sleep(3)

#FAQ No.2 선택
faq_number_2 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/ul/li[2]/a')
faq_number_2.click()
time.sleep(3)
faq_number_2.click()
time.sleep(3)

#FAQ No.3 선택
faq_number_3 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/ul/li[3]/a')
faq_number_3.click()
time.sleep(3)
faq_number_3.click()
time.sleep(3)

#FAQ No.4 선택
faq_number_4 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/ul/li[4]/a')
faq_number_4.click()
time.sleep(3)
faq_number_4.click()
time.sleep(3)

#FAQ No.5 선택
faq_number_5 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/ul/li[5]/a')
faq_number_5.click()
time.sleep(3)

#FAQ 페이지 No.5 내용으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(1): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
time.sleep(3)

#FAQ 페이지 No.5 버튼으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(1): 
    body.send_keys(Keys.PAGE_UP)
    time.sleep(1)

#FAQ No.5 재선택하기
faq_number_5 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/ul/li[5]/a')
faq_number_5.click()
time.sleep(3)

#FAQ 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(1): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
time.sleep(3)

#BLOG Page 접근
blog_page = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/ul/li[4]/a[text()="BLOG"]')
blog_page.click()
time.sleep(3)
    
#전체 메뉴 선택
blog_all_menu = driver.find_element(By. XPATH, '/html/body/div/form/div/div/div/div/div[2]/div[1]/ul/li[1]/a')
blog_all_menu.click()

#전체 메뉴의 첫번째 BLOG 선택
first_blog = driver.find_element(By. XPATH, '/html/body/div/form/div/div/div/div/div[2]/ul/li[1]/a')
first_blog.click()
time.sleep(3)

#첫번째 BLOG 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(6): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
time.sleep(3)

#목록 버튼 선택하기
list_page_button = driver.find_element(By.XPATH, '/html/body/div/form/div/div/div/div/div[2]/div[4]/a')
list_page_button.click()
time.sleep(3)

#전체 메뉴의 두번째 BLOG 선택
second_blog = driver.find_element(By. XPATH, '/html/body/div/form/div/div/div/div/div[2]/ul/li[2]/a')
second_blog.click()
time.sleep(3)

#두번째 BLOG 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(5): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
time.sleep(3)

#목록 버튼 선택하기
list_page_button = driver.find_element(By.XPATH, '/html/body/div/form/div/div/div/div/div[2]/div[4]/a')
list_page_button.click()
time.sleep(3)

#전체 메뉴의 세번째 BLOG 선택
third_blog = driver.find_element(By. XPATH, '/html/body/div/form/div/div/div/div/div[2]/ul/li[3]/a')
third_blog.click()
time.sleep(3)

#세번째 BLOG 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(4): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
time.sleep(3)

#목록 버튼 선택하기
list_page_button = driver.find_element(By.XPATH, '/html/body/div/form/div/div/div/div/div[2]/div[4]/a')
list_page_button.click()
time.sleep(3)

#네번째 블로그 페이지 위치로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(1): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
time.sleep(3)

#전체 메뉴의 네번째 BLOG 선택
third_blog = driver.find_element(By. XPATH, '/html/body/div/form/div/div/div/div/div[2]/ul/li[4]/a')
third_blog.click()
time.sleep(3)

#네번째 BLOG 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(3): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
time.sleep(3)

#목록 버튼 선택
list_page_button = driver.find_element(By.XPATH, '/html/body/div/form/div/div/div/div/div[2]/div[4]/a')
list_page_button.click()
time.sleep(3)

#트레이닝 메뉴 선택
blog_training_button = driver.find_element(By. XPATH, '/html/body/div/form/div/div/div/div/div[2]/div[1]/ul/li[2]/a')
blog_training_button.click()
time.sleep(3)

#이전 페이지로 돌아가기
driver.back()
time.sleep(3)

#소식 메뉴 선택
blog_news_menu = driver.find_element(By. XPATH, '/html/body/div/form/div/div/div/div/div[2]/div[1]/ul/li[3]/a')
blog_news_menu.click()
time.sleep(3)

#소식 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(2): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
time.sleep(3)

#소식 페이지 최상단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(2): 
    body.send_keys(Keys.PAGE_UP)
    time.sleep(1)
time.sleep(3)

#일반 메뉴 선택
blog_general_menu = driver.find_element(By.XPATH, '/html/body/div/form/div/div/div/div/div[2]/div[1]/ul/li[4]/a')
blog_general_menu.click()
time.sleep(3)

#이전 페이지로 돌아가기
driver.back()
time.sleep(3)

#CONTACT 메뉴 선택
contact_page = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/ul/li[5]/a[text()="CONTACT"]')
contact_page.click()
time.sleep(3)

#CONTACT 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(2): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
time.sleep(3)

#서비스 이용약관 버튼 선택
terms_of_use_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div[1]/a')
terms_of_use_button.click()
time.sleep(3)

# 현재 창과 모든 창 핸들 가져오기
original_window = driver.current_window_handle
all_windows = driver.window_handles

# 새 창으로 전환
for window_handle in all_windows:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

#이용약관 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(3): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#이용약관 브라우저 닫기
time.sleep(3)
driver.close()
time.sleep(3)

# 작업 후 다시 원래 창으로 전환
driver.switch_to.window(original_window)
time.sleep(3)

#개인정보처리방침 버튼 선택
privacy_policy = driver.find_element(By. XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/a')
privacy_policy.click()
time.sleep(3)

# 현재 창과 모든 창 핸들 가져오기
original_window = driver.current_window_handle
all_windows = driver.window_handles

# 새 창으로 전환
for window_handle in all_windows:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

#개인정보처리방침 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(5): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#개인정보처리방침 브라우저 닫기
time.sleep(3)
driver.close()
time.sleep(3)

# 작업 후 다시 원래 창으로 전환
driver.switch_to.window(original_window)
time.sleep(3)

#마케팅/광고 활용 동의 버튼 선택
maketing_advertising_button = driver.find_element(By. XPATH, '/html/body/div/div[2]/div/div[3]/div[3]/a')
maketing_advertising_button.click()
time.sleep(3)

# 현재 창과 모든 창 핸들 가져오기
original_window = driver.current_window_handle
all_windows = driver.window_handles

# 새 창으로 전환
for window_handle in all_windows:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

#마케팅/광고 활용 동의 페이지 최하단으로 이동하기
body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(1): 
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#마케팅/광고 활용 동의 브라우저 닫기
time.sleep(3)
driver.close()
time.sleep(3)

#테스트 종료
time.sleep(3)
driver.quit()

# #Tourputt Circle 용 비디오_KOR 위치 접근
# body = driver.find_element(By.TAG_NAME, 'body')
# for _ in range(4): 
#     body.send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)

# #Tourputt Circle 용 비디오_KOR 영상(Vimeo) 재생
# tourputt_circle_video_kor = driver.find_element(By.XPATH, '//*[@id="player"]/div[6]/div[7]/div[1]/button/svg')
# tourputt_circle_video_kor.click()

# #CONTACT Page 접근
# contact_page = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/ul/li[5]/a[text()="CONTACT"]')
# contact_page.click()
# time.sleep(3)