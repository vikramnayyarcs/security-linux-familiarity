import requests

while True:
    # Make a session object
    session = requests.Session()

    # Define the URLs
    url1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
    url2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideLastTwoDigitZIP=on"

    # Make the first request and store cookies in the session
    response1 = session.get(url1)

    # Make the second request using the same session
    response2 = session.get(url2)

    # Print the content of the second response
    if "solution" in response2.text:
        print(response2.text)
        session.cookies.clear()
        break 
    else:
        print("GOING AGAIN")

    # Optionally, you can clear cookies after the second request if needed
    session.cookies.clear()



