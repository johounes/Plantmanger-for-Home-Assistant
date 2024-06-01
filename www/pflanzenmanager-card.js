class PflanzenmanagerCard extends HTMLElement {
  set hass(hass) {
    if (!this.content) {
      this.innerHTML = `
        <style>
          /* Ihre CSS-Stile */
        </style>
        <div id="content">
          <h1>Pflanzenmanager</h1>
          <input type="text" id="plantName" placeholder="Name der Pflanze">
          <input type="number" id="plantAge" placeholder="Alter in Tagen">
          <button id="addPlant">Mutterpflanze hinzufügen</button>
          <div id="plantList"></div>
        </div>
      `;
      this.content = this.querySelector('#content');
      this.addPlantButton = this.querySelector('#addPlant');
      this.plantNameInput = this.querySelector('#plantName');
      this.plantAgeInput = this.querySelector('#plantAge');
      this.plantList = this.querySelector('#plantList');

      this.addPlantButton.addEventListener('click', () => {
        const plantName = this.plantNameInput.value;
        const plantAge = parseInt(this.plantAgeInput.value, 10);
        hass.callService('pflanzenmanager', 'add_plant', {
          name: plantName,
          age: plantAge
        });
      });
    }

    // Aktualisieren Sie die Anzeige basierend auf den aktuellen Home Assistant Daten
    const entities = hass.states;
    this.plantList.innerHTML = '';
    for (let entity_id in entities) {
      if (entity_id.startsWith('sensor.wachstum_tage_')) {
        const plant = entities[entity_id];
        const plantDiv = document.createElement('div');
        plantDiv.innerHTML = `
          <p>${plant.attributes.friendly_name}: ${plant.state} Tage</p>
          <button class="cuttingButton" data-entity="${entity_id}">Steckling geschnitten</button>
          <button class="deleteButton" data-entity="${entity_id}">Pflanze löschen</button>
        `;
        plantDiv.querySelector('.cuttingButton').addEventListener('click', () => {
          hass.callService('pflanzenmanager', 'cut_cutting', {
            entity_id: entity_id
          });
        });
        plantDiv.querySelector('.deleteButton').addEventListener('click', () => {
          hass.callService('pflanzenmanager', 'delete_plant', {
            entity_id: entity_id
          });
        });
        this.plantList.appendChild(plantDiv);
      }
    }
  }

  setConfig(config) {
    this.config = config;
  }

  getCardSize() {
    return 3;
  }
}

customElements.define('pflanzenmanager-card', PflanzenmanagerCard);
