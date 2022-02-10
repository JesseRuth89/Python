def sun_angle(time):
    # Splitting the string into a list
    h, m = time.split(":")
    # Converting the base 60 min to a float
    time = float(h) + float(m) * (1/60)
    print(time)
    # only return when the sun is between 6am and 6pm
    if time < 6 or time > 18:
        return "I don't see the sun!"
    else:
        # Math... 360 degrees total, with 24 hours total, minus the 90 degree offset
        angle = time / 24 * 360 - 90
        return round(angle, 2)


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")



