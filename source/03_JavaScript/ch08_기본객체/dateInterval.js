Date.prototype.getIntervalDay = function(otherday){
    var intervalMilliSec = Math.abs(this.getTime() - otherday.getTime());
    let day = intervalMilliSec / (1000*60*60*24);
    return Math.trunc(day); // Math.trunc(내림) Math.round(반올림) Math.ceil(올림)
};
// var now = new Date();
// var openday = new Date(2025, 3, 7, 9, 30, 0);
// console.log(now.getIntervalDay(openday), '일');
// console.log(openday.getIntervalDay(now), '일');