from homeassistant.components.frontend import add_extra_js_url
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    # Add the resource URL
    add_extra_js_url(hass, "/hacsfiles/pflanzenmanager-card/pflanzenmanager-card.js")
    return True
