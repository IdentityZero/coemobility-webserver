const linkDiv = document.querySelector('.link-set-items');
const activeChild = linkDiv.querySelector('.active');
if (activeChild) {
  activeChild.classList.remove('active');
}

document.getElementById("recordsLink-desktop").classList.add("active")
document.getElementById("recordsLink-mobile").classList.add("active")

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

// const dataServerDomainName = 'http://localhost'
const dataServerDomainName = 'http://47.129.54.22:8000'
const userID = document.getElementById("user-id").value
const parkingRecordsURL = `${dataServerDomainName}/webapi/parking/records/${userID}/all/`;

function formatDate(api_date){
    if (api_date === null){
        return ["No data", "No data"]
    }
    var dateObject = new Date(api_date);

    var date = dateObject.toDateString(); // Convert to a more readable date format
    var time = dateObject.toLocaleTimeString(); // Get the time in a readable format
    return [date, time]
}

function tableTemplate(plateNumber, timein, timeout){
    var tr = document.createElement("tr")

    var th_plateNumber = document.createElement("th")
    th_plateNumber.textContent = plateNumber
    th_plateNumber.setAttribute('scope', 'row');

    var formattedDate = formatDate(timein)
    
    var td_timeInDate = document.createElement("td")
    td_timeInDate.setAttribute('class', 'text-center');
    td_timeInDate.textContent = formattedDate[0]
    
    var td_timeInTime = document.createElement("td")
    td_timeInTime.setAttribute('class', 'text-center');
    td_timeInTime.textContent = formattedDate[1]

    var formattedDate = formatDate(timeout)

    var td_timeOutDate = document.createElement("td")
    td_timeOutDate.setAttribute('class', 'text-center');
    td_timeOutDate.textContent = formattedDate[0]
    
    var td_timeOutTime = document.createElement("td")
    td_timeOutTime.setAttribute('class', 'text-center');
    td_timeOutTime.textContent = formattedDate[1]

    tr.appendChild(th_plateNumber)
    tr.appendChild(td_timeInDate)
    tr.appendChild(td_timeInTime)
    tr.appendChild(td_timeOutDate)
    tr.appendChild(td_timeOutTime)

    return tr
}

const parkingDataContainer = document.getElementById("parking-data-body");

(async () => {
    const data = await fetchData(parkingRecordsURL);
    var parkingData = JSON.parse(data.parking_data);
    parkingData.forEach(element => {
        plateNumber = element.vehicle_plate_number
        timeIn = element.time_in
        timeOut = element.time_out

        parkingDataContainer.appendChild(tableTemplate(plateNumber, timeIn, timeOut))

    });
})();

// Sorting plates
let ascending_text = true;
let counter = 0

function sortText() {
    var table = document.getElementById("parking-data-table");
    var tbody = table.getElementsByTagName("tbody")[0];
    var rows = Array.from(tbody.getElementsByTagName("tr"));

    rows.sort((a, b) => {
        console.log(counter)
        counter += 1
        var nameA = a.getElementsByTagName("th")[0].innerText.toUpperCase();
        var nameB = b.getElementsByTagName("th")[0].innerText.toUpperCase();
        console.log(nameA)
        console.log(nameB)
        if (nameA < nameB) {
            return ascending_text ? -1 : 1;
        }
        if (nameA > nameB) {
            return ascending_text ? 1 : -1;
        }
        return 0;
    });

    for (var i = 0; i < rows.length; i++) {
        tbody.appendChild(rows[i]);
    }

    ascending_text = !ascending_text;
}


var table = document.getElementById('parking-data-table');
var hasContents = table.rows.length > 1;
const downloadRecordsButton = document.getElementById("download-records-btn")

if (!hasContents) {
    downloadRecordsButton.disabled=true
    console.log("No contents")
}

const downloadRecordsURL = `${dataServerDomainName}/webapi/parking/records/${userID}/download/`;

document.getElementById('download-records-btn').addEventListener('click', () => {
    fetch(downloadRecordsURL, {
    method: 'GET',
  })
  .then(response => {
    // Check if the response is successful
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    
    // Create a blob from the response
    return response.blob();
  })
  .then(blob => {
    // Create a URL for the blob object
    const url = URL.createObjectURL(blob);
    
    // Create a link element
    const a = document.createElement('a');
    a.href = url;
    a.download = 'myrecords.csv'; // Set the desired file name
    document.body.appendChild(a);
    
    // Click the link to trigger the download
    a.click();
    
    // Remove the link element
    document.body.removeChild(a);
  })
  .catch(error => {
    console.error('There was a problem with your fetch operation:', error);
  });
});
  

