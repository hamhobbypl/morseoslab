# Interfejs klucza telegraficznego do MorseOSLAB

[Polski](#polski) · [English](#english) · [Deutsch](#deutsch)

## Polski

Moduł pozwala podłączyć fizyczny klucz telegraficzny do iPhone’a z aplikacją MorseOSLAB na iOS. Dzięki temu możesz ćwiczyć nadawanie alfabetem Morse’a na własnym kluczu, korzystając z ćwiczeń i dekodowania w aplikacji.

Mam dostępne płytki PCB do tego projektu. Jeśli wolisz wykonać moduł samodzielnie, w repozytorium znajdziesz schemat, pliki produkcyjne i gotowe oprogramowanie. Przy przygotowanych elementach sam montaż zajmuje kilka minut, a koszt modułu jest niewielki.

## Zawartość repozytorium

| Plik | Zawartość |
| --- | --- |
| [MorseOSLAB-sch_V1.png](MorseOSLAB-sch_V1.png) | Schemat połączeń interfejsu w wersji V1. |
| [MorseOSLAB-board-V1.png](MorseOSLAB-board-V1.png) | Podgląd projektu płytki PCB. |
| [MorseOSLAB_GERBERS_V1.zip](MorseOSLAB_GERBERS_V1.zip) | Pliki Gerber i pliki wierceń potrzebne do zamówienia płytki. |
| [MorseOSLAB-FIRMWARE_V1.uf2](MorseOSLAB-FIRMWARE_V1.uf2) | Gotowe oprogramowanie interfejsu do wgrania na RP2040. |
| [modul.jpg](modul.jpg), [modul_b.jpg](modul_b.jpg) | Zdjęcia zmontowanego modułu. |
| [Diy.jpg](Diy.jpg), [Diy2.jpg](Diy2.jpg) | Zdjęcia przykładowego wykonania DIY. |

## Montaż i uruchomienie

1. Przygotuj elementy i połącz je zgodnie ze schematem. Jeśli zamawiasz PCB, użyj plików produkcyjnych z archiwum ZIP.
2. Podłącz RP2040 do komputera przewodem USB, trzymając przycisk **BOOTSEL**. Skopiuj plik `MorseOSLAB-FIRMWARE_V1.uf2` na dysk **RPI-RP2**. Płytka uruchomi się ponownie.
3. Podłącz klucz do modułu, a moduł przewodem USB z transmisją danych do iPhone’a z MorseOSLAB. W aplikacji wybierz interfejs w **Settings → General → Key input** i uruchom ćwiczenie **Free keying**, żeby sprawdzić nadawanie.

## English

This interface connects a physical Morse key to an iPhone running the MorseOSLAB app for iOS. Use your own key to practise sending Morse code and see what the app decodes.

PCBs for this project are available from me. You can also build the interface yourself at low cost using the schematic, manufacturing files and ready-to-flash firmware in this repository. Once you have the parts ready, assembly takes just a few minutes.

| File | Contents |
| --- | --- |
| [MorseOSLAB-sch_V1.png](MorseOSLAB-sch_V1.png) | V1 wiring schematic. |
| [MorseOSLAB-board-V1.png](MorseOSLAB-board-V1.png) | Preview of the PCB layout. |
| [MorseOSLAB_GERBERS_V1.zip](MorseOSLAB_GERBERS_V1.zip) | Gerber and drill files for PCB fabrication. |
| [MorseOSLAB-FIRMWARE_V1.uf2](MorseOSLAB-FIRMWARE_V1.uf2) | Ready-to-flash RP2040 firmware. |
| [modul.jpg](modul.jpg), [modul_b.jpg](modul_b.jpg) | Photos of the assembled module. |
| [Diy.jpg](Diy.jpg), [Diy2.jpg](Diy2.jpg) | Photos of an example DIY build. |

### Assembly and setup

1. Gather the parts and connect them as shown in the schematic. If ordering a PCB, use the manufacturing files from the ZIP archive.
2. Hold **BOOTSEL** while connecting the RP2040 to your computer over USB. Copy `MorseOSLAB-FIRMWARE_V1.uf2` to the **RPI-RP2** drive. The board will restart.
3. Connect the Morse key to the module, then connect the module to your iPhone with a USB data cable. Select the interface in **Settings → General → Key input** and open **Free keying** to test sending.

## Deutsch

Mit diesem Interface kannst du eine Morsetaste an ein iPhone mit der iOS-App MorseOSLAB anschließen. Damit kannst du das Geben von Morsezeichen mit deiner eigenen Taste üben und sehen, welche Zeichen die App dekodiert.

Platinen für dieses Projekt sind bei mir erhältlich. Du kannst das Interface auch mit geringem Kostenaufwand selbst bauen. Schaltplan, Fertigungsdateien und die fertige Firmware findest du in diesem Repository. Wenn alle Bauteile bereitliegen, dauert der Zusammenbau nur wenige Minuten.

| Datei | Inhalt |
| --- | --- |
| [MorseOSLAB-sch_V1.png](MorseOSLAB-sch_V1.png) | Schaltplan des Interfaces in Version V1. |
| [MorseOSLAB-board-V1.png](MorseOSLAB-board-V1.png) | Vorschau des Platinenlayouts. |
| [MorseOSLAB_GERBERS_V1.zip](MorseOSLAB_GERBERS_V1.zip) | Gerber- und Bohrdateien für die Platinenfertigung. |
| [MorseOSLAB-FIRMWARE_V1.uf2](MorseOSLAB-FIRMWARE_V1.uf2) | Fertige Firmware für den RP2040. |
| [modul.jpg](modul.jpg), [modul_b.jpg](modul_b.jpg) | Fotos des fertig aufgebauten Moduls. |
| [Diy.jpg](Diy.jpg), [Diy2.jpg](Diy2.jpg) | Fotos eines beispielhaften Selbstbaus. |

### Aufbau und Inbetriebnahme

1. Lege die Bauteile bereit und verbinde sie gemäß dem Schaltplan. Wenn du eine Platine bestellst, verwende die Fertigungsdateien aus dem ZIP-Archiv.
2. Halte **BOOTSEL** gedrückt, während du den RP2040 per USB an den Computer anschließt. Kopiere `MorseOSLAB-FIRMWARE_V1.uf2` auf das Laufwerk **RPI-RP2**. Die Platine startet anschließend neu.
3. Schließe die Morsetaste an das Modul an und verbinde das Modul per USB-Datenkabel mit deinem iPhone. Wähle das Interface unter **Settings → General → Key input** und teste das Geben in **Free keying**.
