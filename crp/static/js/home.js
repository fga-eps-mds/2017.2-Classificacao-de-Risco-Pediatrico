$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

});

function changePadding(element) {
    if(element.style.paddingRight === "7px")
        element.style.paddingRight = "0px";
    else {
        element.style.paddingRight = "7px";
    }
}