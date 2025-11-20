# geaCal – Gaussian Easter Algorithm Calendar Tool

geaCal is a small, modular Python tool for calculating
Easter and all dependent holidays.  
The calculation is performed using the classic **Gaussian Easter formula**
(Computus).

# 📁 The project consists of the following modules:
```bash
modules/
│
├── easter.py → Berechnet Ostersonntag mittels Gauß-Formel
├── holidays.py → Leitet dynamische Feiertage aus Ostern ab
├── calendar_data.py → Enthält Utility-Funktionen für Kalendarium
└── utils.py → Hilfsfunktionen: Argument-Parsing, Datumshandling
usr/local/bin/geaCalCli → CLI für die Shell
LICENSE
README.md
```
---

# 📦 Installation

Clone the repository:

```bash
git clone git@github.com:GhostCoder74/GaussEasterAlgorithm.git
```

## Option A – Make it directly executable

```bash
chmod +x usr/local/bin/geaCalCli
sudo cp -r modules /usr/local/share/geaCal/
sudo cp usr/local/bin/geaCalCli /usr/local/bin/
```
---

## Option B – Install via Makefile
```bash
sudo make install
```
### Zum Entfernen:
```bash
sudo make uninstall
```

# 🧪 Usage:
```bash
# Easter Sunday for the current year
geaCalCli --easter

# Dynamic holidays for 2030
geaCalCli --year 2030 --list

# Output as JSON for automated scripts
geaCalCli -y 2027 -l -j
```
# 📝License

## Licensed under GPL-3.0-or-later

See: [LICENSE](https://www.gnu.org/licenses/#GPL)
