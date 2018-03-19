$(document).ready(function(){
    var windowHeight;
    function addHiddenClass(){
        //console.log( "loader ready!" );
        $(this).addClass( "uk-hidden" );
        $(this).remove( "#loader" );
    };
    function removeHiddenClass(){
        //console.log( "wrapper ready!" );
        $(this).contents().unwrap();;
        $(this).remove( "#body-wrapper" );
    };
    $( "#loader" ).delay(5000).fadeOut(addHiddenClass);
    $( "#body-wrapper" ).delay(5000).fadeIn(removeHiddenClass);
    $('#scroll').click(function(){$(window).animate().scrollTop(700);});
    // $('#newsletterSubmit').css().click(submitForm);
    windowHeight = $( window ).height();
});