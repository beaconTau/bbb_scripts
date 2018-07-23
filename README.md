# bbb_scripts 
startup / random scripts for beaglebone black SBC on the phased array controller board

On startup, user needs to run

```
sudo ./export_all_gpios.sh
```
to enable GPIOs used in the system and set initial values. GPIOs mapping are found in the script comments

A few other scripts included, most self-explanatory.

Of note:

```status.py``` is used to read board temperatures and currents of the on-board electronic fuses (efuses), which distribute power to the system.

```fuse.py``` allows the user to manually turn on/off individual efuses. For example: 
```python fuse.py fe on``` turns the 2nd stage amps on
```python fuse.py all off``` turns all subsystems off. Running ```python fuse.py``` shows fuse names.


