
window.onload=function(){

    const targets = document.querySelectorAll('.target');

    targets.forEach(target => {
      target.addEventListener('mouseover', function handleHover(event) {
        console.log('target hovered over', event);
    
        target.setAttribute('style', 'background-color: yellow;');
      });
    });
        
    }