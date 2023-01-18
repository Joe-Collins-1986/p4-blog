

// window.onload is optional since it depends on the way in which you fire events
window.onload=function(){

    // selecting the elements for which we want to add a tooltip
    const target = document.getElementById("target");
    const prompt = document.getElementById("prompt");
    
    // change display to 'block' on mouseover
    target.addEventListener('mouseover', () => {
      prompt.style.display = 'block';
    }, false);
    
    // change display to 'none' on mouseleave
    target.addEventListener('mouseleave', () => {
      prompt.style.display = 'none';
    }, false);
    
    }