from booking import Booking

# inst=Booking()
# inst.lend_first_page()
try:
    with Booking(teardown=False) as bot: # using context manager for closing browser after tests execution
        bot.lend_first_page()
        bot.change_language()
        bot.change_currency()
        bot.select_place_to_go("New York")
        print('Exiting...')
        bot.select_dates(check_in_date="2022-10-03", check_out_date="2022-10-16")
        bot.select_adults(5)
        bot.submit_search()
        bot.apply_filtration(3)
except Exception as e:
    if 'in Path' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise