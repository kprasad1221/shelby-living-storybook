/* Supplied clips play on the settled page. Other pages retain their stills. */
function pauseStoryMedia() {
  document.querySelectorAll('video').forEach(video=>video.pause());
}
function attachStoryMedia(surface, page) {
  const replay = document.getElementById('replayClip');
  replay.hidden = !page.video;
  replay.onclick = null;
  replay.textContent = 'Play clip';
  if (!page.video) return;
  const video = document.createElement('video');
  video.src=page.video;
  video.poster=page.poster;
  video.muted=true;
  video.defaultMuted=true;
  video.setAttribute('muted','');
  video.playsInline=true;
  video.setAttribute('playsinline','');
  video.preload='metadata';
  video.loop=page.playback==='loop';
  const [x,y,w,h]=page.mediaRect;
  Object.assign(video.style,{left:x*100+'%',top:y*100+'%',width:w*100+'%',height:h*100+'%'});
  video.setAttribute('aria-label',page.alt);
  surface.append(video);
  const play=()=>{
    if(!video.isConnected || document.hidden) return;
    video.play().then(()=>{
      if(video.isConnected) replay.textContent='Replay clip';
    }).catch(()=>{
      if(video.isConnected) replay.textContent='Play clip';
    });
  };
  replay.onclick=()=>{video.currentTime=0;play();};
  video.addEventListener('error',()=>{
    if(!video.isConnected) return;
    video.remove();replay.hidden=true;
    document.getElementById('sbHint').textContent='The clip could not load. The still illustration is shown.';
  });
  if(!matchMedia('(prefers-reduced-motion: reduce)').matches) play();
  else replay.textContent='Play clip';
}
// The original curl uses image-backed strips. Turns and the loupe use the
// supplied poster; each clip starts when its page has settled.
function stillMediaInLoupe(container) {
  container.querySelectorAll('video').forEach(video=>{
    const still=new Image();still.src=video.poster;still.alt='';
    still.style.cssText=video.style.cssText;
    still.style.position='absolute';still.style.objectFit='contain';
    video.replaceWith(still);
  });
}
document.addEventListener('visibilitychange',()=>{
  if(document.hidden)pauseStoryMedia();
  else document.querySelectorAll('#sbBook video').forEach(v=>{
    if(!v.ended&&!matchMedia('(prefers-reduced-motion: reduce)').matches)v.play().catch(()=>{});
  });
});
