sensor_name = data.get('sensor_name')
plant_name_parts = sensor_name.split('_')
plant_name = " ".join(plant_name_parts[2:-1]).title()
existing_sensors = hass.states.entity_ids('sensor')

index = 1
while f"sensor.wachstum_tage_{plant_name.lower().replace(' ', '_')}_{index}" in existing_sensors:
    index += 1

new_sensor_id = f"sensor.wachstum_tage_{plant_name.lower().replace(' ', '_')}_{index}"
new_sensor_name = f"{plant_name} {index}#"

hass.states.set(new_sensor_id, 0, {
    'friendly_name': new_sensor_name,
    'unit_of_measurement': 'days',
    'icon': 'mdi:leaf'
})

