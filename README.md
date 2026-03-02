# spin
Install Linus Torvalds' favorite distro on your Pi!
# How to install?
You will need:
* Docker
* Raw image writer (balena etcher etc.)
Run `sh setup.sh` to create the container and produce the build artifact (image.raw).
# Misc Information
* Installer only installs ext4.
* Bluetooth MAC address is the same with the ethernet MAC. (uses glob `e*0`, workaround bluez problem)
* Plymouth is not enabled. (assuming bug in custom rpi kernel, not fixing)
* GPU overlays are switched between Pi 4/5 (`-pi5`)
* Uses stable versions of everything.
* GPU artifacting may happen in some GNOME terminals, use Alacritty for best performance.