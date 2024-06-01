name = data.get('name')
age = data.get('age')

if name is None or age is None:
    logger.error("Fehlende Daten: name oder age nicht vorhanden")
else:
    sensor_id = f"sensor.wachstum_tage_{name.lower().replace(' ', '_')}_1"
    hass.states.set(sensor_id, age, {
        'friendly_name': f"{name} Wachstum",
        'unit_of_measurement': 'days',
        'icon': 'mdi:leaf'
    })
