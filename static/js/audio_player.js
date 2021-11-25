var currentLocation = window.location.hostname;
console.log(currentLocation)
var url = "http://"+ currentLocation + ":7006/?cb=" + new Date().getTime();
var audio = document.getElementById('audio_content');
audio.src = url;
console.log(url.status)
audio.addEventListener("warnings", event => {
    console.log('wait');
});
audio.onwaiting=function(){
    console.log('wait');
};
audio.addEventListener("canplaythrough", event => {
    /* the audio is now playable; play it if permissions allow */
    console.log("canplaythrough");
    audio.play();
});
audio.addEventListener("ended", event => {
    console.log("ended");
    audio.src = url;
    audio.addEventListener("waiting", event => {
        console.log('wait');
    });
});
audio.addEventListener("error", event=>{
    console.log("something",event);
//    location.reload();
})