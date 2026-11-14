"""USB identity for the local MorseOSLAB prototype."""
import supervisor
import usb_hid
import usb_midi

supervisor.set_usb_identification(manufacturer="MorseOSLAB", product="MorseOSLAB")
usb_hid.disable()
usb_midi.enable()
usb_midi.set_names(streaming_interface_name="MorseOSLAB MIDI",
                   audio_control_interface_name="MorseOSLAB",
                   in_jack_name="IN", out_jack_name="OUT")
