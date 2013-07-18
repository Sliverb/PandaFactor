$(document).ready(function(){
  // Autohides the placeholder whenever a textbox has content.
  $(".textboxWithPlaceholder").bind( "input", function(){
    var inputLength = $(this).val().length;
    if (inputLength > 0)
        $(this).siblings(".textboxPlaceholder").hide();
    else 
        $(this).siblings(".textboxPlaceholder").show();
  });
});
