# Plantmanger-for-Home-Assistant
keep track of the Plants and their age in your (indoor) garden 

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

Weitere Informationen und eine detaillierte Dokumentation finden Sie auf [example.com](https://example.com).

Wenn Sie Fragen oder Probleme haben, öffnen Sie bitte ein Issue auf GitHub oder wenden Sie sich an die Community.
