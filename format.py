class Color:
    BLACK = 0, 0, 0
    DARK_GRAY = 50, 50, 50
    GRAY = 100, 100, 100
    WHITE = 255, 255, 255

    RED = 255, 0, 0
    PINK = 255, 105, 180
    ORANGE = 255, 165, 0

    GREEN = 0, 255, 0
    LIGHT_GREEN = 100, 230, 100

    LIGHT_BLUE = 100, 100, 255
    MEDIUM_BLUE = 50, 50, 255
    BLUE = 0, 0, 255

    CYAN = 0, 255, 255
    MAGENTA = 255, 0, 255
    YELLOW = 255, 255, 0
    GOLD = 255, 200, 20




def faded(col):
    r, g, b = col
    return r // 3 * 2, g // 3 * 2, b // 3 * 2


def color(col, text):
    r, g, b = col
    return f'\x1b[38;2;{r};{g};{b}m' + text + '\x1b[0m'


def skillness(value):
    if value <= 0.15:
        return color(Color.RED, 'pathetic')
    if value <= 0.25:
        return color(Color.RED, 'terrible')
    if value <= 0.35:
        return color(faded(Color.RED), 'unskilled')
    if value <= 0.45:
        return color(Color.YELLOW, 'able')
    if value <= 0.55:
        return color(Color.YELLOW, 'average')
    if value <= 0.65:
        return color(Color.YELLOW, 'good')
    if value <= 0.75:
        return color(faded(Color.GREEN), 'very good')
    if value <= 0.8:
        return color(faded(Color.GREEN), 'really good')
    if value <= 0.85:
        return color(faded(Color.GREEN), 'skilled')
    if value <= 0.975:
        return color(Color.GREEN, 'gifted')
    return color(Color.GREEN, 'god-tier')


def extremeness(value):
    if value <= 0.1:
        return color(Color.RED, 'not at all')
    if value <= 0.2:
        return color(Color.RED, 'not')
    if value <= 0.3:
        return color(faded(Color.RED), 'not very')
    if value <= 0.4:
        return color(Color.YELLOW, 'a bit')
    if value <= 0.5:
        return color(Color.YELLOW, 'somewhat')
    if value <= 0.6:
        return color(Color.YELLOW, 'very')
    if value <= 0.7:
        return color(faded(Color.GREEN), 'highly')
    if value <= 0.8:
        return color(faded(Color.GREEN), 'extremely')
    if value <= 0.95:
        return color(Color.GREEN, 'most')
    return color(Color.GREEN, 'absolute most')


def age_class(age):
    if age <= 2:
        return color(Color.LIGHT_BLUE, 'toddler')
    elif age <= 5:
        return color(Color.LIGHT_BLUE, 'preschool child')
    elif age <= 12:
        return color(Color.LIGHT_BLUE, 'child')
    elif age <= 18:
        return color(Color.MEDIUM_BLUE, 'teenager')
    elif age <= 24:
        return color(Color.MEDIUM_BLUE, 'young adult')
    elif age <= 45:
        return color(Color.MEDIUM_BLUE, 'adult')
    elif age <= 65:
        return color(Color.BLUE, 'middle aged')
    elif age <= 90:
        return color(Color.BLUE, 'aged')
    else:
        return color(Color.BLUE, 'ancient')


def is_non_average(value):
    return value < 0.35 or value > 0.65
