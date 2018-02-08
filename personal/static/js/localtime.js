monthList = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"];
function displayTime(){
    var d = new Date(),
        myMonth = monthList[d.getMonth()],
        myDay = d.getDate(),
        myYear = d.getFullYear(),
        myHour = d.getHours(),
        myMinute = d.getMinutes(),
        mySecond = d.getSeconds();
    myMinute = checkTime(myMinute);
    mySecond = checkTime(mySecond);
    document.getElementById("time").innerHTML = myMonth + " " + myDay + ", " + myYear + ", " + myHour + ":" + myMinute + ":" + mySecond;
    var t = setTimeout(displayTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};
    return i;
}