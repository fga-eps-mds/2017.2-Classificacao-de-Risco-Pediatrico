$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

});

function changeGradientWidth(element) {
    var containerBox = element.parentNode.parentNode;

    if(containerBox.style.paddingRight === "7px")
        containerBox.style.paddingRight = "0px";
    else {
        containerBox.style.paddingRight = "7px";
    }
}