// Initialize
document.getElementById("id_vehicle_classification").required = true

var vehicleInstanceCounter = 0

function createNewFormBlock(rowNumber){
    var node = document.createElement("div")
    node.className = "row"
    node.id = `row${rowNumber}`

    // Line for spacing
    var line = document.createElement("div")
    line.className = "line"
    node.appendChild(line)

    // Delete Button
    var deleteButtonContainer = document.createElement("div")
    deleteButtonContainer.className = "deleteButtonContainer"
    node.appendChild(deleteButtonContainer)

    var deleteButton = document.createElement("button")
    deleteButton.type = "button"
    deleteButton.onclick = function(){
        console.log("Hello world", rowNumber)
        node.remove()
    }

    deleteButton.textContent = "DELETE"
    deleteButton.className = "btn btn-danger "
    deleteButtonContainer.appendChild(deleteButton)
    
    return node
}

function createFormTemplate(inputField, inputLabel, fieldErrorID){
    
    var fieldLabel = document.createElement("div")
    fieldLabel.className = "field-label"
    fieldLabel.textContent = inputLabel

    var fieldInput = document.createElement("div")
    fieldInput.className = "field-input"
    fieldInput.appendChild(inputField)

    var fieldError = document.createElement("div")
    fieldError.className = "field-error"
    fieldError.id = fieldErrorID

    var formField = document.createElement("div")
    formField.className = "form-field"
    formField.appendChild(fieldLabel)
    formField.appendChild(fieldInput)
    formField.appendChild(fieldError)
    
    var mainNode = document.createElement("div")
    mainNode.className = "col-12 col-md-6"
    mainNode.appendChild(formField)
    
    return mainNode
}

// Get all the inputs
var originalInput_vehiclePlateNumber = document.getElementById("id_vehicle_plate_number");
var orginalSelect_vehicleClassification = document.getElementById("id_vehicle_classification");
var originalInput_vehicleImage = document.getElementById("id_vehicle_image");
var originalInput_vehicleModel = document.getElementById("id_vehicle_model");

function addAnotherVehicle(){

    // Clone the inputs
    var clonedInput_vehiclePlateNumber = originalInput_vehiclePlateNumber.cloneNode(true);
    var clonedSelect_vehicleClassification = orginalSelect_vehicleClassification.cloneNode(true);
    var clonedInput_vehicleImage = originalInput_vehicleImage.cloneNode(true);
    var clonedInput_vehicleModel = originalInput_vehicleModel.cloneNode(true);
    
    // Change the ID and name attributes of the cloned select element
    var clonedInput_vehiclePlateNumber_id = `id_vehicle_plate_number${vehicleInstanceCounter}`;
    clonedInput_vehiclePlateNumber.id = clonedInput_vehiclePlateNumber_id;
    clonedInput_vehiclePlateNumber.name = `vehicle_plate_number${vehicleInstanceCounter}`;
    var clonedInput_vehiclePlateNumber_template = createFormTemplate(clonedInput_vehiclePlateNumber,"Plate Number", clonedInput_vehiclePlateNumber_id)

    var clonedSelect_vehicleClassification_id = `id_vehicle_classification${vehicleInstanceCounter}`;
    clonedSelect_vehicleClassification.id = clonedSelect_vehicleClassification_id;
    clonedSelect_vehicleClassification.name = `vehicle_classification${vehicleInstanceCounter}`;
    clonedSelect_vehicleClassification.setAttribute("required", "required");
    var clonedSelect_vehicleClassification_template = createFormTemplate(clonedSelect_vehicleClassification, "Classification", clonedSelect_vehicleClassification_id)

    var clonedInput_vehicleImage_id = `id_vehicle_image${vehicleInstanceCounter}`;
    clonedInput_vehicleImage.id = clonedInput_vehicleImage_id;
    clonedInput_vehicleImage.name = `vehicle_image${vehicleInstanceCounter}`;
    var clonedInput_vehicleImage_template = createFormTemplate(clonedInput_vehicleImage, "Vehicle Image",clonedInput_vehicleImage_id)
    
    var clonedInput_vehicleModel_id = `id_vehicle_model${vehicleInstanceCounter}`;
    clonedInput_vehicleModel.id = clonedInput_vehicleModel_id
    clonedInput_vehicleModel.name = `vehicle_model${vehicleInstanceCounter}`;
    var clonedInput_vehicleModel_template = createFormTemplate(clonedInput_vehicleModel, "Model", clonedInput_vehicleModel_id)

    newFormBlock = createNewFormBlock(vehicleInstanceCounter)
    newFormBlock.appendChild(clonedInput_vehiclePlateNumber_template)
    newFormBlock.appendChild(clonedSelect_vehicleClassification_template)
    newFormBlock.appendChild(clonedInput_vehicleModel_template)
    newFormBlock.appendChild(clonedInput_vehicleImage_template)


    var container = document.getElementById("additional");
    container.appendChild(newFormBlock)

    vehicleInstanceCounter++;
}

