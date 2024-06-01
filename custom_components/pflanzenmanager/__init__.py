import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "pflanzenmanager"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    _LOGGER.info("Setting up Pflanzenmanager component")

    # Register services
    hass.services.async_register(DOMAIN, 'add_plant', add_plant)
    hass.services.async_register(DOMAIN, 'cut_cutting', cut_cutting)
    hass.services.async_register(DOMAIN, 'delete_plant', delete_plant)

    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    _LOGGER.info("Setting up Pflanzenmanager entry")
    return True

async def add_plant(service: ServiceCall):
    name = service.data.get('name')
    age = service.data.get('age')

    if name is None or age is None:
        _LOGGER.error("Missing data: name or age not provided")
    else:
        sensor_id = f"sensor.wachstum_tage_{name.lower().replace(' ', '_')}_1"
        hass.states.async_set(sensor_id, age, {
            'friendly_name': f"{name} Growth",
            'unit_of_measurement': 'days',
            'icon': 'mdi:leaf'
        })

async def cut_cutting(service: ServiceCall):
    sensor_name = service.data.get('sensor_name')
    plant_name_parts = sensor_name.split('_')
    plant_name = " ".join(plant_name_parts[2:-1]).title()
    existing_sensors = hass.states.async_entity_ids('sensor')

    index = 1
    while f"sensor.wachstum_tage_{plant_name.lower().replace(' ', '_')}_{index}" in existing_sensors:
        index += 1

    new_sensor_id = f"sensor.wachstum_tage_{plant_name.lower().replace(' ', '_')}_{index}"
    new_sensor_name = f"{plant_name} {index}#"

    hass.states.async_set(new_sensor_id, 0, {
        'friendly_name': new_sensor_name,
        'unit_of_measurement': 'days',
        'icon': 'mdi:leaf'
    })

async def delete_plant(service: ServiceCall):
    entity_id = service.data.get('entity_id')
    hass.states.async_remove(entity_id)
