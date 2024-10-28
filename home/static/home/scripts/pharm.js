var initialpositionset;
var isDraggingsset;
var startPossset;

var initial6577et;

var containerboxset = document.querySelector('.online-pharmacist-section')
var containerid22et = document.getElementById('onpharm')
var contaiinerinnerset = document.querySelector('.online-pharmacist-wrapper')
var containeridset = document.getElementById('onpharm2')
  // disable default image drag
containerboxset.addEventListener('dragstart', (e) => e.preventDefault())
// pointer events
containerboxset.addEventListener('mousedown', pointerDown12552et)
containerboxset.addEventListener('touchstart', pointerDown12552et)
containerboxset.addEventListener('mouseup', pointerUp12552et)
containerboxset.addEventListener('mouseleave', pointerUp12552et)
containerboxset.addEventListener('mousemove', pointerMove12552et)
containerboxset.addEventListener('touchleave', pointerUp12552et)
containerboxset.addEventListener('touchmove', pointerMove12552et)

initialpositionset = containeridset.offsetLeft

// prevent menu popup on long press
window.oncontextmenu = function (event) {
    event.preventDefault()
    event.stopPropagation()
    return false
  }
  
// the touch or mousedown function
function pointerDown12552et (event) {
     event.preventDefault()
     //check if it's mouch clickec or touched clicked
    if (event.type == "touchstart") {
      posX12552et = event.touches[0].clientX;
    } else {
      posX12552et = event.clientX;
    }
    console.log("hey")
    startPossset = posX12552et - initialpositionset;
    console.log(startPossset)
    isDraggingsset = true
     
      
  }
  
  function pointerMove12552et(event) {
    if (event.type == "touchmove") {
    
      if (isDraggingsset) {
        event.preventDefault()
        const currentPosition122552et = event.touches[0].clientX;
        const dist22552et = currentPosition122552et - startPossset
        initialpositionset = dist22552et
        console.log(currentPosition122552et)
        console.log(dist22552et)
        contaiinerinnerset.style.left = `${dist22552et}px`;
        checkboundaries12552et()
        console.log("love")}
        
    } else {
      if (isDraggingsset) {
        event.preventDefault()
        const currentPosition122552et = event.clientX 
        const dist22552et = currentPosition122552et - startPossset
        initialpositionset = dist22552et
        console.log(currentPosition122552et)
        console.log(dist22552et)
        contaiinerinnerset.style.left = `${dist22552et}px`;
        checkboundaries12552et()
        console.log("love")
        
    }
   

    }
  }
  
  function pointerUp12552et() {
    
    isDraggingsset = false
    console.log("hee")
  
  }
  // to check end boundaries and ensure it's not crossed
function checkboundaries12552et(){
  let outermeaser22552et = containerboxset.getBoundingClientRect();
  let innermeaser22552et = contaiinerinnerset.getBoundingClientRect();
  if (parseInt(contaiinerinnerset.style.left) > 0){
    contaiinerinnerset.style.left = '0px';

  }
  else if(innermeaser22552et.right < outermeaser22552et.right){
    contaiinerinnerset.style.left = `-${innermeaser22552et.width - outermeaser22552e.width}px`
  }
}



