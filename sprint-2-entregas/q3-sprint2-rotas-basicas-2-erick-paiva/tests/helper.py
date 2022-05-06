from datetime import datetime as dt


def unprocessed_data():
    curr_hour = dt.now().hour
    msg = "Boa noite!"

    if curr_hour < 12:
        msg = "Bom dia!"

    elif curr_hour < 18:
        msg = "Boa tarde!"

    return (dt.now().strftime("%d/%m/%Y"), dt.now().strftime("%I:%M:%S %p"), msg)
