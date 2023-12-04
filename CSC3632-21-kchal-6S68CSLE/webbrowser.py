import webbrowser
import browser_cookie3

def clear_cookies_for_url(url):
    # Open the URL in the default web browser
    webbrowser.open(url)

    # Clear cookies for the specified URL
    browser_cookie3.clear(domain=url)

# Replace 'https://example.com' with the URL for which you want to clear cookies
url_one = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
url_two = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideMonthDoB=on&hideDayDoB=on&hideLastFiveDigitZIP=on&hideGender=on"

# Call the function to clear cookies for the specified URL
while True:
    clear_cookies_for_url(url_to_clear_cookies)
