const linkDiv = document.querySelector('.link-set-items');
const activeChild = linkDiv.querySelector('.active');
if (activeChild) {
  activeChild.classList.remove('active');
}

document.getElementById("aboutUsLink-desktop").classList.add("active")
document.getElementById("aboutUsLink-mobile").classList.add("active")

function copyNumberToClickBoard(i){
  // 09xx-yyy-zzzz
  const numbers = [
    ["60", "307", "2300"], // Dave - 0.
    ["10", "741", "0447"], // Ayson - 1
    ["61", "956", "4471"], // She - 2
    ["98", "266", "3810"], // Jasser - 3
    ["56", "814", "3850"], // Lorence - 4
    ["16", "683", "8638"], // Lj - 5
    ["60", "869", "5030"] // Carlo - 6
  ]
  
  var n = numbers[i];
  var toCopy = `09${n[0]}${n[1]}${n[2]}`

  navigator.clipboard.writeText(toCopy).then(function() {
    console.log('Text copied to clipboard');
    alert("Number copied to clipboard");
  }).catch(function(error) {
    console.error('Error copying text: ', error);
    alert("Cannot copy Phone Number");
  });
}



