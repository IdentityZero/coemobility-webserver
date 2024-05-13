const linkDiv = document.querySelector('.link-set-items');
const activeChild = linkDiv.querySelector('.active');
if (activeChild) {
  activeChild.classList.remove('active');
}

document.getElementById("aboutUsLink-desktop").classList.add("active")
document.getElementById("aboutUsLink-mobile").classList.add("active")

