function MyFunction(a,b){
    th = document.getElementsByTagName('th')[0].innerHTML =a;
    th = document.getElementsByTagName('th')[2].innerHTML =b;
    window.history.replaceState({}, null, '/accounts/%5Eenter_results/admin/'+a+'/'+b);
    sessionStorage.setItem("reloading", "true");
    sessionStorage.setItem("a", a);
    sessionStorage.setItem("b", b);
    document.location.reload()

}
window.onload = function() {
    var reloading = sessionStorage.getItem("reloading");
     var a = sessionStorage.getItem("a");
      var b = sessionStorage.getItem("b");
    if (reloading) {
        sessionStorage.removeItem("reloading");
        th = document.getElementsByTagName('th')[0].innerHTML = a;
        th = document.getElementsByTagName('th')[2].innerHTML = b;
    }
}





