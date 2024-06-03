$(document).ready(function() {

    $(".card-img-top").click(function () {
        $(".id-card-body").slideToggle();
    });


    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
    
});