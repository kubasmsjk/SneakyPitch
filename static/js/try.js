function myFunction() {
  var iframe = document.getElementById("frame");
  var elmnt = iframe.contentWindow.document.getElementsByTagName("H1")[0];
  elmnt.style.display = "none";
}