
print("""
              ______
             |      |
             |      |
    .========'      '========.
    |   _      xxxx      _   |
    |  /_;-.__ / _\  _.-;_\  |
    |     `-._`'`_/'`.-'     |
    '========.`\   /`========'
             | |  / |
             |/-.(  |
             |\_._\ |
             | \ \`;|
             |  > |/|
             | / // |
             | |//  |
             | \(\  |
             |  ``  |
             |      |
             |      |
             |      |
             |      |
 //// _  _/|| \//  |//_   _ \// _
^ `^`^ ^`` `^ ^` ``^^`  `^^` `^ `^

""")
print("Hosgeldin Master")
list = ["help, ip, detailed ip, ipv4, phonetrack about, exit"]
print("komutlar: ip, detailed ip, relax, phonetrack, IPv4, about, exit")

while True:
    cmd = input("Katzz> ").strip().lower()

    if cmd == "ip":
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print("Your local IP is:", local_ip)

    elif cmd == "detailed ip":
        ip = requests.get("https://api.ipify.org").text
        print(ip)
    elif cmd == "about":
        print("""
⠀⠀⠀⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣿⣿⣿⣿⣿⣿⣆⡀⠀⠀⠀⠀⣠⣴⣦⡄⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣶⣿⣿⣿⣿⡀⣽⡿⣶⣦⡀⠀⠀⠀⠀⠀
⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣿⣿⣿⣿⣆⠀⠀⠀⠀
⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣿⣿⣿⣿⣿⡿⢟⣿⣷⡀⠀
⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣿⣽⣿⣽⣾⣿⣿⣿⠛⠉⠉⠀⢈⣿⣿⡇⠀
⠀⠀⠀⢻⣿⣿⠛⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠡⠤⠄⠁⠀⠀⢻⣿⡇⠀
        ⠀⠀⠀⠘⣿⣿⠄⠀⠀⠀⠀⠀⣉⠙⠋⢿⣿⣯⠀⣰⣿⣿⡿⡃⠀
⠀⠀⠀⠀⢹⣿⣇⣀⠀⠈⠉⠉⠁⠀⣤⢠⣿⣿⣧⡆⣤⣤⡀⣾⣿⣿⣿⢠⡇⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣷⣤⠄⣀⣴⣧⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠇⠀
⠀⠀⠀⠀⠀⠸⣿⣯⠉⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡯⠁⡌⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⡄⢿⣿⣿⣿⣿⣿⣎⠙⠻⠛⣁⣼⣿⣿⡿⠛⠁⡸⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠉⣿⡿⣿⣿⣿⣿⣷⣬⣿⡿⠟⠋⢀⣴⡞⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠉⠉⠋⠉⠉⠁⠀⢀⣴⣿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⠿⢃⣴⣿⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
""")
        print("originally made by katzComm/2026")
    elif cmd == "ipv4":
        ipdot = input("ip girin: ")
        ipd = ipdata.IPData('f117640a321b4c8f58841a4cd52844f16f1f0ea20ebc1b8395bb9246')
        respond = ipd.lookup(ipdot)
        pprint(respond)
    elif cmd == "--help":
        print(list)
    elif cmd == "phonetrack":
        number = input("Phonenumber: ")
        try:

            parsed_number = phonenumbers.parse(number)
            location = geocoder.description_for_number(parsed_number, "en")
            operator = carrier.name_for_number(parsed_number, "en")
            timezones = timezone.time_zones_for_number(parsed_number)
            print(f"\n-----PhoneTracker Data-----")
            print(f"Location is: {location}")
            print(f"Carrier is: {operator}")
            print(f"Timezone is: {', '.join(timezones)}")
        except phonenumbers.NumberParseException:
            print("Wrong Number")
    elif cmd == "relax":
        print("""


        (  )   (   )  )
             ) (   )  (  (
             ( )  (    ) )
             _____________
            <_____________> ___
            |             |/ _ \
            |               | | |
            |               |_| |
         ___|             |\___/
        /    \___________/    /
        \_____________________/



relaxing playlist: https://open.spotify.com/playlist/4TpOvBy83VowmxvnLkuMyT?si=EpsPucbzSs-Aan1tN2Pztw&utm_source=copy-link&pi=J8ymQsufRROJ0



""")
    elif cmd == "exit":
        break
    else:
        print("Sorry, it looks like you wrote the command wrong or the module you wrote does not exist. Try using '--help' for commands")
