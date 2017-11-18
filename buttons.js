$(window).load(function(){
  var totalBottom = $('#plane').height() + $('#plane').offset().top + 20;
  $('#buttonsContain').css({"top":totalBottom + "px","visibility":"visible"});
  console.log($('#plane').height());
  console.log($('#plane').offset().top);});
$(window).resize(function(){
  var totalBottom = $('#plane').height() + $('#plane').offset().top + 20;
  $('#buttonsContain').css("top",totalBottom + "px");});
  var NorthButton = document.getElementById('north');
  var EastButton = document.getElementById('east');
  var WestButton = document.getElementById('west');
  var SouthButton = document.getElementById('south');
