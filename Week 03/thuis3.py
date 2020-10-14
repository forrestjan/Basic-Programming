def is_schrikkeljaar(jaartal):
    if jaartal % 4 == 0 and jaartal % 100 != 0:
        # Alle jaartallen deelbaar door 4 maar geen eeuw
        return True
    elif jaartal % 400 == 0:
        # alle eeuwen deelbaar door 400
        return True
    else:
        # alle andere jaren zijn geen schrikkeljaar.
        return False
# 2 jaren opvragen en de schrikkeljaren ertussen afdrukken


def print_jaartallen(start_jaartal, stop_jaartal):
    for jaar in range(start_jaartal, stop_jaartal + 1):
        if is_schrikkeljaar(jaar) == True:
            print(f"{jaar}")


print_jaartallen(1900, 2020)
#input instellen van jaartallen 