import requests

# Create a session object outside the loop
session = requests.Session()

while True:
    try:
        # Define the URLs
        url1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
        url2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideLastTwoDigitZIP=on"

        # Make the first request and store cookies in the session
        response1 = session.get(url1)

        # Make the second request using the same session
        response2 = session.get(url2)

        # Print the content of the second response
        # Commenting out the print for potential performance improvement
        # print(response2.text)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    finally:
        # Optionally, you can clear cookies after the second request if needed
        session.cookies.clear()

# Close the session outside the loop
session.close()
