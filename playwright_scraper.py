from playwright.sync_api import sync_playwright
from parser import parse


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://testing-www.codefellows.org")

        # Click the course calendar link
        page.get_by_text("Course Calendar").click()

        # XPath Selector
        page.click("//label[text()='400: Advanced']")

        # Tracks are selected by default
        # So let's deselect all expect the ones we want

        courses = {
            "java": "Code 401: Java",
            "javascript": "Code 401: JavaScript",
            ".net": "Code 401: ASP.NET",
            "python": "Code 401: Python",
            "cybersecurity": "Ops 401: Cybersecurity",
        }

        course_key = "python"
        for course in courses:
            if course != course_key:
                course_label = courses[course]
                page.click(f"//label[text() = '{course_label}']")

        markup = page.content()

        results = parse(markup)

        print(results)

        browser.close()


if __name__ == '__main__':
    main()
