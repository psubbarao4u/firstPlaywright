from pom.validateText import validateText

def test_run(set_up) -> None:
    page=set_up

    #page.get_by_role("heading", name="Register Account").click()
    assert page.is_visible(validateText.header_text)
    assert page.is_visible(validateText.already_text)
    #page.get_by_text("If you already have an").click()

    page.get_by_placeholder("First Name").type("Subbu")
    page.get_by_placeholder("Last Name").type("Testing")
    page.get_by_placeholder("E-Mail").type("Testing@test123.com")
    page.get_by_placeholder("Telephone").type("4443334343")
    page.locator("//*[@id='input-password']").type("Password")
    page.locator("//*[@id='input-confirm']").type("Password")
    page.get_by_label("Yes").check()
    page.locator("//*[@id='content']/form/div/div/input[1]").check()