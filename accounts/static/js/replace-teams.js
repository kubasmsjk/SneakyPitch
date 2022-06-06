window.onload = function() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const home_team = urlParams.get('home_team')
    const away_team = urlParams.get('away_team')
    th = document.getElementsByTagName('th')[0].innerHTML = home_team;
    th = document.getElementsByTagName('th')[2].innerHTML = away_team;

}





