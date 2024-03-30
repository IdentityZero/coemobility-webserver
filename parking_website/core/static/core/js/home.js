const linkDiv = document.querySelector('.link-set-items');
const activeChild = linkDiv.querySelector('.active');
if (activeChild) {
  activeChild.classList.remove('active');
}

document.getElementById("homeLink-desktop").classList.add("active")
document.getElementById("homeLink-mobile").classList.add("active")

async function fetchData(url, maxRetries = 3, retryDelay = 1000) {
    for (let retry = 0; retry < maxRetries; retry++) {
      try {
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      } catch (error) {
        console.error(`Fetch error (retry ${retry + 1}/${maxRetries}):`, error);
        if (retry < maxRetries - 1) {
          console.log(`Retrying in ${retryDelay}ms...`);
          await new Promise(resolve => setTimeout(resolve, retryDelay));
        } else {
          console.error('Max retries exceeded, giving up.');
          return null;
        }
      }
    }
  }

function formatParkingData(role, vehicle_category, available_value, date,max=null){
    var set_id = `${role}-${vehicle_category}`
    var parentDiv = document.getElementById(set_id);

    var date_container = parentDiv.querySelector('p[name="date"]');
    var available_container = parentDiv.querySelector('h2[name="available-value"]');
    
    date_container.innerHTML = `As of: ${date}`
    available_container.innerHTML = available_value

    if (max !== null){
        var max_space_container = parentDiv.querySelector('p[name="max"]');
        max_space_container.innerHTML = `Max space: ${max}`
    }
}

function setParkingData(roles, vehicle_categories, parking_data){
    roles.forEach(role => {
        vehicle_categories.forEach(vehicle_category => {

            var max_space_value = parking_data[role][vehicle_category]["max"]
            var date_value = parking_data[role][vehicle_category]["date"]
            var available_value = parking_data[role][vehicle_category]["available"]

            const date = new Date(date_value);

            // Format the date as desired
            const formattedDate = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`;
            const formattedTime = `${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}:${date.getSeconds().toString().padStart(2, '0')}`;
            const formattedDateTime = formattedDate + formattedTime

            formatParkingData(role, vehicle_category,available_value, formattedDateTime, max_space_value)

        })
    });
}

function updateParkingData(role,vehicle_category, action, date){
    console.log(role,vehicle_category,action)
    var set_id = `${role}-${vehicle_category}`
    var parentDiv = document.getElementById(set_id);

    var availableValue = parseInt(parentDiv.querySelector('h2[name="available-value"]').textContent)

    if (action === "EXIT" || action ==="exit"){
        availableValue += 1
      } else if (action === "ENTRANCE" || action === "entry"){
        availableValue -=1
    }

    formatParkingData(role,vehicle_category,availableValue,date)
}

function formatDate(date){
    const options = { month: 'long', day: 'numeric', year: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit' };
    return date.toLocaleDateString('en-US', options);
}

const dataServerDomainName = 'http://122.248.192.233'
// const dataServerDomainName = 'http://192.168.55.105:8000'

function setCoveredParkingSpace(area, area_id, state){
    var parkingSpaceContainer = document.getElementById(`${area}-${area_id}`)
    var parkingSpace = parkingSpaceContainer.children[0]

    if (state){
        parkingSpace.classList.add("parking-space-available");
    } else{
        parkingSpace.classList.remove("parking-space-available");
    }
}

const parkingStatusURL = `${dataServerDomainName}/webapi/parking/status/`;
(async () => {
    const data = await fetchData(parkingStatusURL);
    if (data) {
        // Unpack
        var roles = data.roles
        var vehicle_categories = data.vehicle_categories
        var parking_data = data.parking_data

        setParkingData(roles,vehicle_categories, parking_data)

    } else {
        var errorMsg = document.getElementById("message")
        errorMsg.innerHTML = "Try reconnecting to the page"
        console.log('Failed to fetch data');
    }
})();

const coveredParkingStatusAreasURL = `${dataServerDomainName}/api/covered_parking/areas/`;
const coveredParkingStatusURL = `${dataServerDomainName}/api/covered_parking/`;
(async() =>{
    const areaNames = await fetchData(coveredParkingStatusAreasURL)
    areaNames.forEach(areaName =>{
        var parkingAreaContainer = document.getElementById(areaName.area_name)
        parkingAreaContainer.querySelector('h5[name="title"]').innerHTML = areaName.area_name
        
    })

    const parkingData = await fetchData(coveredParkingStatusURL)
    parkingData.forEach(element =>{
        var area = element.area
        var area_id = element.id_area
        var occupied = element.state
        setCoveredParkingSpace(area,area_id,occupied);

    })
})();

const parkingStatusSSE = new EventSource(`${dataServerDomainName}/webapi/parking/status/sse/`);
parkingStatusSSE.addEventListener('message', function(event) {
    const parkingData = JSON.parse(event.data);
    if (parkingData['topic'] == "parking"){
        role = parkingData['data']['role']
        vehicle_category = parkingData['data']['vehicle_category']
        action = parkingData['data']['action']
        date = parkingData['data']['date'].split(".")[0]

        updateParkingData(role,vehicle_category,action,date)
    } else if (parkingData['topic'] =="covered_parking"){
        var area = parkingData.data.area
        var area_id = parkingData.data.id_area
        var state = parkingData.data.state

        setCoveredParkingSpace(area, area_id, state)
    }
});

const userID = document.getElementById("user-id").value
const latestRecordContainer = document.getElementById("collapseStatus")
const latestRecordBody = latestRecordContainer.querySelector(".card-body")

const userLatestRecordURL = `${dataServerDomainName}/webapi/parking/records/${userID}`;
(async() =>{
    const parkingRecord = await fetchData(userLatestRecordURL)
    if (parkingRecord.vehicle === null){
        latestRecordBody.innerHTML = `
        <p>You haven't registered your vehicle! </p>
        <div class="row justify-content-center align-items-center pb-2">
            <div class="col-auto">
                <a class="btn btn-secondary" id="register-home-url-anchor">Register now</a>
            </div>
        </div>
        `;

        var anchor = document.getElementById("register-home-url-anchor");
        var anchorURL = document.getElementById("register-home-url").value;
        anchor.setAttribute('href', anchorURL)

        console.log("No cars yet")
        return
    }

    parkingRecordVehicles = parkingRecord.vehicle
    latestRecordBody.innerHTML = ""
    parkingRecordVehicles.forEach( vehicle =>{
        
        if (vehicle.rfid === false){
            latestRecordBody.innerHTML += `
            <p class='mt-1 mb-1'>Your vehicle ${vehicle.plate_number} does not have COE registered RFID tag!</p>
            ` 
        } else{

            var formattedEntry = "No data"
            var formattedExit = "No data"

            if (vehicle.latest_record.entry !== null){
                formattedEntry = formatDate(new Date(vehicle.latest_record.entry))
            }

            if (vehicle.latest_record.exit !== null){
                formattedExit = formatDate(new Date(vehicle.latest_record.exit))
            }

            latestRecordBody.innerHTML += `
            <p>Using vehicle with plate ${vehicle.plate_number}</p>
            <div class="status-container mt-1">
                <p>Entrance: </p>
                <h5>${formattedEntry}</h5>
                </div>
            <div class="status-container mb-1">
                <p>Exit: </p>
                <h5>${formattedExit}</h5>
            </div>
            `
        }
    })

})();


