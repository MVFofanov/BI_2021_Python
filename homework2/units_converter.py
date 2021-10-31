converter = {'m': 1, 'km': 1000, 'dm': 0.1, 'cm': 0.01, 'mm': 0.001, 'mcm': 0.000001, 'nm': 0.000000001,
             'lea': 4828.032, 'mi': 1609.344, 'yd': 0.9144,
             'ft': 0.3048, 'in': 0.0254, 'ln': 0.0021666666666, 'cl': 0.000254, 'nl': 5556, 'nmi': 1852,
             'ftm': 1.8288,
             'kg': 1, 'g': 0.001, 'mg': 0.000001, 'mcg': 0.000000001, 'ng': 0.000000000001, 'q': 100,
             't': 1000, 'ct': 0.0002, 'lb': 0.45359237,
             'm2': 1, 'km2': 1000000, 'ha': 10000, 'a': 100, 'yd2': 0.83612736, 'ft2': 0.09290304,
             'm3': 1, 'dm3': 0.001, 'cm3': 0.000001, 'mm3': 0.000000001, 'l': 0.001, 'ml': 0.000001,
             'mcl': 0.000000001, 'yd3': 0.764554857984, 'ft3': 0.028316846592, 'bl': 0.16365924,
             'bbl': 0.158987, 'gal': 0.00378541, 'qt': 0.000946353, 'pt': 0.000568261,
             'oz': 0.000028349523125,
             'm/s': 1, 'km/s': 1000, 'km/h': 0.277778, 'm/min': 0.0166667, 'km/min': 16.6667,
             'c': None, 'k': None, 'f': None,
             }

units = ({'m', 'km', 'dm', 'cm', 'mm', 'mcm', 'nm', 'lea', 'mi', 'yd', 'ft', 'in', 'ln', 'cl', 'nl', 'nmi', 'ftm'},
         {'kg', 'g', 'mg', 'mcg', 'ng', 'q', 't', 'ct', 'lb'},
         {'m2', 'km2', 'ha', 'a', 'yd2', 'ft2'},
         {'m3', 'dm3', 'cm3', 'mm3', 'l', 'ml', 'mcl', 'yd3', 'ft3', 'bl', 'bbl', 'gal', 'qt', 'pt', 'oz'},
         {'m/s', 'km/s', 'km/h', 'm/min', 'km/min'},
         {'c', 'k', 'f'})

history = []


def get_help():
    help_message = '''
    Program: units_converter.py
    Version: 1.0

    Usage                           Type your request in this format: number unit1 unit2
                                    number - unit1 amount
                                    unit1 - first physical quantity used to convert from
                                    unit2 - second physical quantity used to convert to

                                    units format corresponds to the inernational classification
                                    and indicated in the brackets after units below

    Example                         to convert 451 degrees Fahrenheit to degrees Celsius type one of this example
                                    commands, which perform equally:
                                    451 f c
                                    or
                                    451 f to c
                                    or even something like that:
                                    451 f should be converted from degrees fahrenheit to degrees celsius c

    Currently available commands:

    e or exit                       quit the programm
    q or quit                       quit the programm
    history or print                print current session results history on the screen
    h or help                       get this help page
    save                            print current session results history in file

    Currently available units:

    distance                        meter (m), kilometer (km), decimeter (dm), centimetre (cm), millimeter (mm),
                                    micrometer (mcm), nanometer (nm), league (lea), mile (mi), yard (yd)
                                    foot (ft), inch (in), line (ln), caliber (cl), nautical league (nl),
                                    nautical mile (nmi), fathom (ftm)

    weight                          kilogram (kg), gram (g), milligram (mg), microgram (mcg), nanogram (ng),
                                    centner (q), ton (t), carat (ct), pound (lb)

    square                          square meter (m2), square kilometer (km2), hectare (ha), are (a), square yard (yd2),
                                    square foot (ft2)

    volume                          cubic meter (m3), cubic decimeter (dm3), cubic centimeter (cm3), liter (l),
                                    cubic millimeter (mm3), liter (l), milliliter (ml), microliter (mcl),
                                    cubic yard (yd3), cubic foot (ft3), barrel (bl), oil barrel (bbl), gallon (gal),
                                    quart (qt), pint (pt), ounce (oz)

    speed                           meter per second (m/s), kilometer per second (km/s), kilometer per hour (km/h),
                                    meter per minute (m/min), kilometer per minute (km/min)

    temperature                     degrees celsius (c), degrees kelvin (k), degrees fahrenheit (f)


    Contacts:
    Mikhail Fofanov                 mikhail.v.fofanov@gmail.com
    '''
    return help_message


def greeting_message():
    print('''
    To convert some unit to another, type your request in this format: number unit1 unit2
    Units should be denoted as its short names: 'm' for metres or 'g' for grams
    For example, to convert 451 degrees Fahrenheit to degrees Celsius type: 451 f c
    You will know the truth, and the truth will set you free. 'h' or 'help'
    ''')


def save_results_in_file(history):
    output_file = input('Type a name of file with results and desired file extension. e.g. results.txt: ')
    with open(output_file, 'w') as w:
        for i in history:
            w.write(i + '\n')


def is_value_a_number(value):
    try:
        float(value) + 42
    except ValueError:
        return False
    return True


def are_units_correct(unit1, unit2):
    for units_group in units:
        if {unit1, unit2}.issubset(units_group):
            return True
    return False


def convert_temperature_to_Celsius(unit1, value):
    if unit1 == 'k':
        return value - 273.15
    if unit1 == 'f':
        return (value - 32) * 5 / 9
    if unit1 == 'c':
        return value


def convert_temperature_from_Celsius(unit2, value):
    if unit2 == 'k':
        return value + 273.15
    if unit2 == 'f':
        return value * (9 / 5) + 32
    if unit2 == 'c':
        return value


def convert_to_si(unit1, value):
    return value * converter[unit1]


def convert_from_si(unit2, value):
    return value / converter[unit2]


def get_result(result, value, unit1, unit2):
    print(f'Result: {result} {unit2}\n')
    history.append(f'{value} {unit1} was converted to {result} {unit2}')


greeting_message()

while True:
    command = input('Enter command: ').lower()
    if command in {'exit', 'e', 'q', 'quit'}:
        print('Good luck\n')
        break
    elif command in {'help', 'h'}:
        print(get_help())
    elif command in {'print', 'history'}:
        print(*history, sep='\n')
        print()
    elif command in {'save'}:
        save_results_in_file(history)
        print()
    else:
        if len(tuple(command.split())) < 3:
            print('Wrong input format. Try again!\n')
        else:
            value, unit1, *more, unit2 = command.split()
            if not {unit1, unit2}.issubset(converter.keys()):
                print(f"This tools doesn't support convertation of {unit1} to {unit2}\n")
            elif not are_units_correct(unit1, unit2):
                print(f"Your units are from different groups. You can't convert {unit1} to {unit2}\n")
            elif not is_value_a_number(value):
                print(f'Value {value} is not a number. Try again!\n')
            elif float(value) < 0:
                er = f'Value {value} is negative. Enter a positive number to save the world from falling into chaos!\n'
                print(er)
            elif {unit1, unit2}.issubset({'c', 'k', 'f'}):
                result = convert_temperature_from_Celsius(unit2, convert_temperature_to_Celsius(unit1, float(value)))
                get_result(result, value, unit1, unit2)
            else:
                result = convert_from_si(unit2, convert_to_si(unit1, float(value)))
                get_result(result, value, unit1, unit2)
