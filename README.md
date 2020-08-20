<!-- @format -->

# py-led-game

Two player LED game run on a Raspberry Pi and a breadboard.

Author: Collin Kleest

Contact: [collinkleest@gmail.com](mailto:collinkleest@gmail.com)

## Materials

- Raspberry Pi
- Breadboard
- 9 GPIO JumperCables (female to male)
- 6 Leds
- 2 Buttons

## Quick Usage

Make sure you you have a [python interperator](https://www.python.org/downloads/) installed.

```bash
sudo apt-get install -y python3-gpiozero
# or
pip3 install python3-gpiozero
```

Clone and change directory to repo

```bash
git clone https://github.com/collinkleest/py-led-game
cd py-led-game/
```

Install dependencies

```bash
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
```

Make sure you configure the leds and buttons with the BCM board pin numbers, json file is loacted in `src/config/gpio-config.json`

**Make sure the first element in the ledArray is the closest to the p1Btn, and the last element in the ledArray is closest to the p2Btn**

```json
{
  "ledArray": [5, 6, 13, 19, 12, 26],
  "p1Btn": 23,
  "p2Btn": 24
}
```

Change directory into `src/` then run App.

```bash
cd src/
python3 App.py
```

[LICENSE](./LICENSE)
