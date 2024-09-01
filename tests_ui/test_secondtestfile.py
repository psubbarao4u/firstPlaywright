from pom.validateText import validateText
import pytest

def test_adokati(set_up) -> None:
    page = set_up
    assert page.is_visible(validateText.header_text)
    assert page.is_visible(validateText.already_text)
    page.get_by_placeholder("First Name").type("UMA")
    page.get_by_placeholder("Last Name").type("Testing")
    page.get_by_placeholder("E-Mail").type("UMA@test222.com")
    page.get_by_placeholder("Telephone").type("1113334343")
    page.locator("//*[@id='input-password']").type("Password")
    page.locator("//*[@id='input-confirm']").type("Password")
    page.get_by_label("Yes").check()
    page.locator("//*[@id='content']/form/div/div/input[1]").check()

@pytest.mark.parametrize("FN,LN,email,phone,pwd",[("USB","Peddibhotla","test@tesdt123.com","123456789","test1234"),("USB","Peddibhotla","test@tesdt123.com","123456789","test1234"),("USB","Peddibhotla","test@tesdt123.com","123456789","test1234")])
def test_rendodhi(set_up,FN,LN,email,phone,pwd) -> None:
    page = set_up
    assert page.is_visible(validateText.header_text)
    assert page.is_visible(validateText.already_text)
    page.get_by_placeholder("First Name").type(FN)
    page.get_by_placeholder("Last Name").type(LN)
    page.get_by_placeholder("E-Mail").type(email)
    page.get_by_placeholder("Telephone").type(phone)
    page.locator("//*[@id='input-password']").type(pwd)
    page.locator("//*[@id='input-confirm']").type(pwd)
    page.get_by_label("Yes").check()
    page.locator("//*[@id='content']/form/div/div/input[1]").check()