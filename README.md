# CantemoPortalScripts
Simple Scripts for Cantemo Portal

1) catdv2portal.py

This script will take a full CatDV XML file and analyze it for all fields present.  It will then present the user with each field
and expect that the appropriate matched Cantemo Portal field_id is set.  When this is complete, it will register a new projection
named "CatDV" into Portal.

This script assumes your metadata group in Portal is named CatDV.

2) handler-multi.py

This is an example script for handling multiple assets using the Cantem Agent "Open With..." menu item with a simple Python GUI
