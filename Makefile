# -----------------------------------------------------------------------------
# Project:        GaussEasterAlgorithm
# File:           Makefile
# Author:         Christian Klose
# Email:          ghostcoder@gmx.de
# GitHub:         https://github.com/GhostCoder74/Set-Project-Headers (GhostCoder74)
# Copyright (c) 2025 Christian Klose
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This file is part of GaussEasterAlgorithm.
# Do not remove this header.
# Header added by https://github.com/GhostCoder74/Set-Project-Headers
# -----------------------------------------------------------------------------

# ============================================================
# geaCal – Makefile (enhanced)
# Installs:
#   /opt/geaCal/modules/*
#   /opt/geaCal/modules/lang/*
#   /opt/geaCal/README.md
#   /opt/geaCal/LICENSE
#   /usr/local/bin/geaCal
# ============================================================

PREFIX       := /
OPT_DIR      := $(PREFIX)opt/geaCal
MODULE_DIR   := modules
LANG_DIR     := $(MODULE_DIR)/lang
BIN_DIR      := $(PREFIX)usr/local/bin

LOGO_DIR     := usr/share/geaCal
LOGO_FILE    := geaCal-Logo.jpeg

INSTALL_BIN  := install -m 0755
INSTALL_FILE := install -m 0644
PYTEST       := pytest -q

PKG_NAME     := geacal
PKG_VERSION  := 1.0.0
DEB_DIR      := $(CURDIR)/pkg
DEB_BUILD    := $(DEB_DIR)/$(PKG_NAME)_$(PKG_VERSION)

.PHONY: all install uninstall show tree test create-lang package clean

all:
	@echo "Use: make install | uninstall | test | create-lang CODE | package"

# ------------------------------------------------------------
install:
	@echo "📦 Installing geaCal..."
	@mkdir -vp "$(OPT_DIR)/modules"
	@mkdir -vp "$(OPT_DIR)/modules/lang"
	@mkdir -vp "$(BIN_DIR)"
	@mkdir -vp "$(PREFIX)$(LOGO_DIR)"

	# copy modules
	@cp -vr $(MODULE_DIR)/*.py "$(OPT_DIR)/modules/" || true

	# copy lang dir
	@cp -vr $(LANG_DIR)/* "$(OPT_DIR)/modules/lang/" || true

	# copy README and LICENSE
	$(INSTALL_FILE) README.md "$(OPT_DIR)/"
	$(INSTALL_FILE) LICENSE "$(OPT_DIR)/"

	# copy logo
	$(INSTALL_FILE) "$(LOGO_DIR)/$(LOGO_FILE)" "$(PREFIX)$(LOGO_DIR)/$(LOGO_FILE)"
	$(INSTALL_FILE) "$(LOGO_DIR)/$(LOGO_FILE)" "$(PREFIX)$(LOGO_DIR)/"

	# install CLI(s)
	$(INSTALL_BIN) usr/local/bin/geaCal "$(BIN_DIR)/geaCal"

	@echo "✔ Installation complete!"

# ------------------------------------------------------------
uninstall:
	@echo "🗑 Removing geaCal..."
	@rm -vrf "$(OPT_DIR)"
	@rm -vf  "$(BIN_DIR)/geaCal"
	@rm -vrf  "$(PREFIX)$(LOGO_DIR)/"
	@echo "✔ Uninstalled."

# ------------------------------------------------------------
show:
	@echo "."
	@echo "├── opt"
	@echo "│   └── geaCal"
	@echo "│       ├── README.md"
	@echo "│       ├── LICENSE"
	@echo "│       └── modules"
	@echo "│           ├── easter.py"
	@echo "│           ├── holidays.py"
	@echo "│           ├── calendar_data.py"
	@echo "│           ├── utils.py"
	@echo "│           ├── translator.py"
	@echo "│           ├── create_language.py"
	@echo "│           └── lang/*.json"
	@echo "├── usr"
	@echo "│   └── local"
	@echo "│       └── bin"
	@echo "│           └── geaCal"
	@echo "└── usr"
	@echo "    └── share"
	@echo "        └── geaCal"
	@echo "            └── geaCal-Loagp.jpeg"

# ------------------------------------------------------------
tree:
	@echo "$(PREFIX)"
	@echo "├── opt"
	@echo "│   └── geaCal"
	@echo "│       ├── README.md"
	@echo "│       ├── LICENSE"
	@echo "│       └── modules"
	@echo "│           ├── easter.py"
	@echo "│           ├── holidays.py"
	@echo "│           ├── calendar_data.py"
	@echo "│           ├── utils.py"
	@echo "│           ├── translator.py"
	@echo "│           ├── create_language.py"
	@echo "│           └── lang"
	@echo "│               ├── en.json"
	@echo "│               └── de.json"
	@echo "├── usr"
	@echo "│   └── local"
	@echo "│       └── bin"
	@echo "│           └── geaCal"
	@echo "└── usr"
	@echo "    └── share"
	@echo "        └── geaCal"
	@echo "            └── geaCal-Loagp.jpeg"

# ------------------------------------------------------------
test:
	@echo "Running pytest..."
	$(PYTEST)

# ------------------------------------------------------------
# create a new language file based on en.json
# usage: make create-lang CODE=de
# ------------------------------------------------------------
create-lang:
ifndef CODE
	$(error CODE is required. Usage: make create-lang CODE=de)
endif
	python3 modules/create_language.py $(CODE)

# ------------------------------------------------------------
# build a simple Debian package (deb)
# produces: pkg/geacal_1.0.0.deb
# ------------------------------------------------------------
package: clean
	@echo "Building deb package..."
	@rm -rf $(DEB_DIR)
	@mkdir -p $(DEB_BUILD)/opt/geaCal/modules
	@mkdir -p $(DEB_BUILD)/usr/local/bin
	@mkdir -p $(DEB_BUILD)/usr/share/geaCal

	# copy files to package tree
	@cp -r $(MODULE_DIR)/*.py $(DEB_BUILD)/opt/geaCal/modules/
	@cp -r $(LANG_DIR) $(DEB_BUILD)/opt/geaCal/modules/
	@cp README.md $(DEB_BUILD)/opt/geaCal/
	@cp LICENSE $(DEB_BUILD)/opt/geaCal/
	@cp usr/local/bin/geaCal $(DEB_BUILD)/usr/local/bin/geaCal
	@cp usr/share/geaCal/*.jpeg $(DEB_BUILD)/usr/share/geaCal/

	# create DEBIAN control
	@mkdir -p $(DEB_BUILD)/DEBIAN
	@printf "Package: $(PKG_NAME)\nVersion: $(PKG_VERSION)\nSection: utils\nPriority: optional\nArchitecture: all\nMaintainer: Ghostcoder <ghostcoder@example.org>\nDescription: geaCal - Gaussian Easter Algorithm Calendar Tool\nDepends: python3\n" > $(DEB_BUILD)/DEBIAN/control

	@dpkg-deb --build $(DEB_BUILD) $(DEB_DIR)/$(PKG_NAME)_$(PKG_VERSION).deb
	@echo "Deb package created: $(DEB_DIR)/$(PKG_NAME)_$(PKG_VERSION).deb"

# ------------------------------------------------------------
clean:
	@rm -rf pkg
	@echo "clean done"

