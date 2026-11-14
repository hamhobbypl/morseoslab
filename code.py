"""Swapped paddles GP5/GP4-GND -> USB MIDI channel 1, notes 69/70.

CircuitPython 10.3.1, Raspberry Pi Pico build. No extra libraries.
Debounce both edges for 1 ms. USB MIDI writes retry partial messages.
"""
import board
import digitalio
import supervisor
import time
import usb_midi

keys = [digitalio.DigitalInOut(pin) for pin in (board.GP5, board.GP4)]
for key in keys:
    key.switch_to_input(pull=digitalio.Pull.UP)
midi = usb_midi.ports[1]
note_on = [bytes((0x90, note, 100)) for note in (69, 70)]
note_off = [bytes((0x80, note, 0)) for note in (69, 70)]
panic = bytes((0xB0, 123, 0))


def send(message):
    offset = 0
    while offset < len(message):
        if not supervisor.runtime.usb_connected:
            return False
        written = midi.write(message[offset:])
        if written:
            offset += written
    return True


raw_down = [False, False]
stable_down = [False, False]
sent_down = [False, False]
raw_since = [time.monotonic_ns(), time.monotonic_ns()]
connected_before = False
print("MorseOSLAB ready: GP5/GP4-GND (swapped), channel 1, notes 69/70")
try:
    while True:
        now = time.monotonic_ns()
        for i, key in enumerate(keys):
            down = not key.value
            if down != raw_down[i]:
                raw_down[i] = down
                raw_since[i] = now
            if raw_down[i] != stable_down[i] and now - raw_since[i] >= 1_000_000:
                stable_down[i] = raw_down[i]
        connected = supervisor.runtime.usb_connected
        if not connected:
            connected_before = False
            sent_down = [False, False]
        else:
            if not connected_before:
                send(panic)
                sent_down = [False, False]
                connected_before = True
            for i in range(2):
                if stable_down[i] != sent_down[i]:
                    if send(note_on[i] if stable_down[i] else note_off[i]):
                        sent_down[i] = stable_down[i]
finally:
    for message in note_off:
        send(message)
    send(panic)
    for key in keys:
        key.deinit()
