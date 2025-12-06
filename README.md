# geaCal – Gaussian Easter Algorithm Calendar Tool

<p align="center">
  <img src="usr/share/geaCal/geaCal-Logo.jpeg" alt="geaCal logo" width="280">
</p>

geaCal is a small, modular Python tool for calculating
Easter and all dependent holidays.  
The calculation is performed using the classic **Gaussian Easter formula**
(Computus).

# 📁 The project consists of the following modules:
```bash
/opt/
├── geaCal/
│  	└── modules/
│       ├── geaCal_calendar_data_mod.py"
│       ├── geaCal_create_language_mod.py"
│       ├── geaCal_easter_mod.py"
│       ├── geaCal_holidays_mod.py"
│       ├── geaCal_odbc_server_mod.py"
│       ├── geaCal_utils_mod.py"
│       ├── geaCal_translator_mod.py"
│       ├── geaCal_web_provider_mod.py"
│       └── lang
│           ├── en.json   # Default lang english
│           ├── de.json   # Template can be generated with: geaCal --create-lang de
│           └── es.json   # Template can be generated with: geaCal --create-lang es
│                         # and then translated into the correct language
/usr/
├── local/
│   └── bin/
│       ├── geaCal              → CLI for the shell
│       └── geaCal-sql2csv-cli  → CLI for "geaCal -Q" ODBC Service
└── share/
    └── geaCal/
        └── geaCal-Logo.jpeg
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
chmod +x usr/local/bin/geaCal
sudo cp -r modules /usr/local/share/geaCal/
sudo cp usr/local/bin/geaCal /usr/local/bin/
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
geaCal --help
usage: geaCal [-h] [-y YEAR] [-l] [-e] [-j] [--lang LANG] [--create-lang CREATE_LANG] [command] [value1] [value2]

geaCal – Calendar / Holiday Tool

positional arguments:
  command               legacy commands: holiday, range, help
  value1                date or start year
  value2                end year

options:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  select year
  -l, --list            list holidays for a year
  -e, --easter          print Easter Sunday date
  -j, --json            JSON output
  --lang LANG           Override language (de, en, ...)
  --create-lang CREATE_LANG
                        Create new language file from English base

```

## Examples:
```bash
# Easter Sunday for the current year
geaCal --easter

# Dynamic holidays for 2030
geaCal --year 2030 --list

# Output as JSON for automated scripts
geaCal -y 2027 -l -j
```
# 📚 Background

The calculation is based on the classic Gaussian Easter formula from 1816, 
improved with the correction for century leap rules in the Gregorian calendar.

Further information
[WIKIPEDIA](https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Osterformel)

# 📝License

## Licensed under GPL-3.0-or-later

See: [LICENSE](https://www.gnu.org/licenses/#GPL)
