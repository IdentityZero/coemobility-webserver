const linkDiv = document.querySelector('.link-set-items');
const activeChild = linkDiv.querySelector('.active');
if (activeChild) {
  activeChild.classList.remove('active');
}

document.getElementById("profileLink-desktop").classList.add("active")
document.getElementById("profileLink-mobile").classList.add("active")
