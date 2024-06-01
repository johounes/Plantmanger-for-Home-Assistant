# Plantmanger-for-Home-Assistant
keep track of the Plants and their age in your (indoor) garden 
## English Below

# Pflanzenmanager für Home Assistant

[![Open your Home Assistant instance and show the add integration dialog with a specific integration pre-filled.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start?domain=pflanzenmanager)

**Pflanzenmanager** ist ein Home Assistant-Plugin, das es Ihnen ermöglicht, das Wachstum und die Pflege Ihrer Pflanzen zu verwalten. Mit diesem Plugin können Sie Mutterpflanzen hinzufügen, Stecklinge schneiden und sowohl Mutterpflanzen als auch Stecklinge löschen.

## Funktionen

- **Hinzufügen von Mutterpflanzen**: Fügen Sie neue Mutterpflanzen mit einem Namen und einem Startalter hinzu.
- **Schneiden von Stecklingen**: Schneiden Sie Stecklinge von vorhandenen Mutterpflanzen und verfolgen Sie deren Wachstum.
- **Löschen von Pflanzen**: Entfernen Sie Mutterpflanzen und Stecklinge, die nicht mehr benötigt werden.
- **Automatische Anzeige**: Zeigt dynamisch alle Pflanzen und deren Stecklinge an.

## Installation

### Voraussetzungen

- Home Assistant muss installiert und konfiguriert sein.
- HACS (Home Assistant Community Store) muss installiert sein, um benutzerdefinierte Karten hinzuzufügen.

### Schritt-für-Schritt-Anleitung

1. **HACS-Integration hinzufügen**

    Öffnen Sie HACS in Ihrem Home Assistant Dashboard und klicken Sie auf "Frontend". Suchen Sie nach "Pflanzenmanager" und installieren Sie die Integration.

2. **Hinzufügen der Lovelace-Ressource**

    Fügen Sie die folgende Ressource zu Ihrer `configuration.yaml` hinzu:

    ```yaml
    lovelace:
      resources:
        - url: /hacsfiles/pflanzenmanager-card/pflanzenmanager-card.js
          type: module
    ```

3. **Aktivierung des Plugins**

    Gehen Sie zu **Einstellungen** > **Integrationen** > **Pflanzenmanager** und folgen Sie dem Konfigurationsfluss, um die Integration zu aktivieren.

4. **Home Assistant neu starten**

    Starten Sie Home Assistant neu, um sicherzustellen, dass alle Änderungen übernommen werden.

5. **Karte hinzufügen und testen**

    Fügen Sie die neue Karte Ihrem Lovelace-Dashboard hinzu:

    ```yaml
    type: 'custom:pflanzenmanager-card'
    ```

    Testen Sie, ob die Mutterpflanzen und Stecklinge wie erwartet hinzugefügt, angezeigt und gelöscht werden können.

## Dokumentation und Unterstützung

Wenn Sie Fragen oder Probleme haben, öffnen Sie bitte ein Issue auf GitHub oder wenden Sie sich an die Community.


## English Instructions 

Pflanzenmanager for Home Assistant

Pflanzenmanager is a Home Assistant plugin that allows you to manage the growth and care of your plants. With this plugin, you can add mother plants, cuttings, and delete both mother plants and cuttings.
Features

    Add Mother Plants: Add new mother plants with a name and starting age.
    Cut Cuttings: Cut cuttings from existing mother plants and track their growth.
    Delete Plants: Remove mother plants and cuttings that are no longer needed.
    Automatic Display: Dynamically displays all plants and their cuttings.

Installation
Prerequisites

    Home Assistant must be installed and configured.
    HACS (Home Assistant Community Store) must be installed to add custom cards.

Step-by-Step Guide

    Add HACS Integration

    Open HACS in your Home Assistant dashboard, click on "Frontend", search for "Pflanzenmanager", and install the integration.

    Add Lovelace Resource

    Add the following resource to your configuration.yaml:

    yaml

lovelace:
  resources:
    - url: /hacsfiles/pflanzenmanager-card/pflanzenmanager-card.js
      type: module

Activate the Plugin

Go to Settings > Integrations > Pflanzenmanager and follow the configuration flow to activate the integration.

Restart Home Assistant

Restart Home Assistant to ensure all changes are applied.

Add Card and Test

Add the new card to your Lovelace dashboard:

yaml

    type: 'custom:pflanzenmanager-card'

    Test if the mother plants and cuttings can be added, displayed, and deleted as expected.

Documentation and Support

If you have any questions or issues, please open an issue on GitHub or reach out to the community.



