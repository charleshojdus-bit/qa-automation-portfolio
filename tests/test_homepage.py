def test_homepage_loads(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"