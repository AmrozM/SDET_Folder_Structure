from playwright.sync_api import expect
from pages.MIS_login_Team5 import LoginPage
from pages.navigateToStudents import goToStudents
from config.config import BASE_URL, SCHOOL_ID, USERNAME, PASSWORD
from utils.logger import get_logger

def test_Login_MIS_Team5(page):
    log = get_logger("TestLogin")
    log.info("Starting MIS login test")
    login = LoginPage(page)
    login.open(BASE_URL)
    login.login(SCHOOL_ID, USERNAME, PASSWORD)
    navigator = goToStudents(page)
    page.wait_for_load_state("load")
    expect(navigator.student_module).to_be_attached()
    #page.wait_for_timeout(10000)    
    navigator.go_to_student_module()
    navigator.select_student()
    navigator.click_view_button()
    page.wait_for_timeout(10000)
    new_tab = navigator.click_view_button()
    #assert "https://mis-hotfix.bromcom.dev/Nucleus/UI/Areas/People/StudentList.aspx" in new_tab.url  ---> Use this if page open in new tab.
    assert f"{BASE_URL}Nucleus/UI/Areas/People/StudentList.aspx" in page.url, "Url seems to be different"
    log.info("MIS Login test completed successfully")