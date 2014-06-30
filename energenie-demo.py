from energenie import switch_on, switch_off

print("Sockets 1-4 or 0 for all")

while True:
    socket = int(raw_input('Turn socket on: '))
    switch_on(socket)
    socket = int(raw_input("Turn socket off: "))
    switch_off(socket)
