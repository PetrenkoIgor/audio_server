var url = "http://0.0.0.0:7006/?cb=" + new Date().getTime();
var audio = document.getElementById('audio_content');
audio.src = url;
audio.addEventListener("waiting", event => {
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
