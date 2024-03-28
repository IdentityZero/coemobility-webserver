// Navigation
var sideBarButton = document.getElementById("checkBox")
var sideBar = document.getElementById("mobile-sidebar")

function openSideBar(){
    if (sideBarButton.checked){
        sideBar.style.left = 0;
    }
}

function closeSideBar(){
    sideBar.style.left = "-100vw"
    sideBarButton.checked = false
}