# Energenie Demo

A fork of the Python game 'Memory Puzzle' used to demonstrate the [Energenie board](https://energenie4u.co.uk/index.php/catalogue/product/ENER002-2PI)

- [energenie.py](energenie.py) is a module containing functions to switch plug sockets on and off
- [energenie-demo.py](energenie-demo.py) is a basic demonstration of switching power switches on and off with Python
- [memorypuzzle.py](memorypuzzle.py) is a modified version of a game which plays music and turns on a power switch when the player wins

Usage of the `energenie` module:

```python
from energenie import switch_on, switch_off
from time import sleep

# turn a plug socket on and off by number
switch_on(1)
switch_off(1)

switch_on(3)
switch_off(3)

# turn all plug sockets on and off
switch_on(0)
switch_off(0)

# turn some plug sockets on, then turn them off after 10 seconds
switch_on(1)
switch_on(4)
sleep(10)
switch_off(1)
switch_off(4)
```

See a video of the memory puzzle game demonstration at http://vimeo.com/99159077
