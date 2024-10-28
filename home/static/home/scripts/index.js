var dropdownshow = document.querySelector('.navdropdownshow');
var bttn = document.querySelector('#btttn');
var bttn2 = document.querySelector('#bttn23')

bttn.addEventListener('click', ()=>{
    dropdownshow.classList.toggle('active');
    dropdownshow.style.opacity = "1.0"
    console.log('hey')
});
bttn2.addEventListener('click', ()=>{
    dropdownshow.classList.toggle('active');
    dropdownshow.style.opacity = '0.0'
    
});

$(document).ready(function(){
    $('#plus1').on('click', function(){
        
        $('.ul1').show();
        $('#minus1').show();
        $('#plus1').hide();
    })
    $('#minus1').on('click', function(){
        $('.ul1').hide();
        $('#plus1').show();
        $('#minus1').hide();
    })
    $('#plus2').on('click', function(){
       
        $('.ul2').show();
        $('#minus2').show();
        $('#plus2').hide();
    })
    $('#minus2').on('click', function(){
        $('.ul2').hide();
        $('#plus2').show();
        $('#minus2').hide();
    })
    $('#plus3').on('click', function(){
      
        $('.ul3').show();
        $('#minus3').show();
        $('#plus3').hide();
    })
    $('#minus3').on('click', function(){
        $('.ul3').hide();
        $('#plus3').show();
        $('#minus3').hide();
    })
    $('#plus4').on('click', function(){
       
        $('.ul4').show();
        $('#minus4').show();
        $('#plus4').hide();
    })
    $('#minus4').on('click', function(){
        $('.ul4').hide();
        $('#plus4').show();
        $('#minus4').hide();
    })
    $('#plus5').on('click', function(){
       
        $('.ul5').show();
        $('#minus5').show();
        $('#plus5').hide();
    })
    $('#minus5').on('click', function(){
        $('.ul5').hide();
        $('#plus5').show();
        $('#minus5').hide();
    })
    $('#plus6').on('click', function(){
       
        $('.ul6').show();
        $('#minus6').show();
        $('#plus6').hide();
    })
    $('#minus6').on('click', function(){
        $('.ul6').hide();
        $('#plus6').show();
        $('#minus6').hide();
    })
})



var initialposi;
var isDraggings;
var startPoss;

var initial657;

var containerbox = document.querySelector('.pharmacist-section2')
var containerid2 = document.getElementById('pharmacistsection_id')
var contaiinerinner = document.querySelector('.pharmacist-wrapper2')
var containerid = document.getElementById('pharmacistwrapper_id')
  // disable default image drag
containerbox.addEventListener('dragstart', (e) => e.preventDefault())
// pointer events
containerbox.addEventListener('mousedown', pointerDown1255)
containerbox.addEventListener('touchstart', pointerDown1255)
containerbox.addEventListener('mouseup', pointerUp1255)
containerbox.addEventListener('mouseleave', pointerUp1255)
containerbox.addEventListener('mousemove', pointerMove1255)
containerbox.addEventListener('touchleave', pointerUp1255)
containerbox.addEventListener('touchmove', pointerMove1255)

initialposi = containerid.offsetLeft

// prevent menu popup on long press
window.oncontextmenu = function (event) {
    event.preventDefault()
    event.stopPropagation()
    return false
  }
  
// the touch or mousedown function
function pointerDown1255 (event) {
     event.preventDefault()
     //check if it's mouch clickec or touched clicked
    if (event.type == "touchstart") {
      posX1255 = event.touches[0].clientX;
    } else {
      posX1255 = event.clientX;
    }
    console.log("hey")
    startPoss = posX1255 - initialposi;
    console.log(startPoss)
    isDraggings = true
     
      
  }
  
  function pointerMove1255(event) {
    if (event.type == "touchmove") {
    
      if (isDraggings) {
        event.preventDefault()
        const currentPosition12255 = event.touches[0].clientX;
        const dist2255 = currentPosition12255 - startPoss
        initialposi = dist2255
        console.log(currentPosition12255)
        console.log(dist2255)
        contaiinerinner.style.left = `${dist2255}px`;
        checkboundaries1255()
        console.log("love")}
        
    } else {
      if (isDraggings) {
        event.preventDefault()
        const currentPosition12255 = event.clientX 
        const dist2255 = currentPosition12255 - startPoss
        initialposi = dist2255
        console.log(currentPosition12255)
        console.log(dist2255)
        contaiinerinner.style.left = `${dist2255}px`;
        checkboundaries1255()
        console.log("love")
        
    }
   

    }
  }
  
  function pointerUp1255() {
    
    isDraggings = false
    console.log("hee")
  
  }
  // to check end boundaries and ensure it's not crossed
function checkboundaries1255(){
  let outermeaser2255 = containerbox.getBoundingClientRect();
  let innermeaser2255 = contaiinerinner.getBoundingClientRect();
  if (parseInt(contaiinerinner.style.left) > 0){
    contaiinerinner.style.left = '0px';

  }
  else if(innermeaser2255.right < outermeaser2255.right){
    contaiinerinner.style.left = `-${innermeaser2255.width - outermeaser2255.width}px`
  }
}



  var nxtBtn1544 = document.querySelector('.preaa-btn5');
  var preBtn1544=  document.querySelector('.nxteaa-btn5');
  
  

  nxtBtn1544.addEventListener("click", () => switchSlide2255("next"));
  preBtn1544.addEventListener("click", () => switchSlide2255("prev"));

  function switchSlide2255(arg) {

      initial657 = containerid.offsetLeft;
    
      if (arg == "next") {
        contaiinerinner.style.left = `${initial657 + size}px`;
      
      } else {
        contaiinerinner.style.left = `${initial657 - size}px`;
      
      }
   checkboundaries1255()
   
  }

 







var initialpositions;
var isDraggingss;
var startPosss;

var initial6577;

var containerboxs = document.querySelector('.drug-section7')
var containerid22 = document.getElementById('drugsection_id')
var contaiinerinners = document.querySelector('.drug-wrapper5')
var containerids = document.getElementById('drugwrapper_id')
  // disable default image drag
containerboxs.addEventListener('dragstart', (e) => e.preventDefault())
// pointer events
containerboxs.addEventListener('mousedown', pointerDown12552)
containerboxs.addEventListener('touchstart', pointerDown12552)
containerboxs.addEventListener('mouseup', pointerUp12552)
containerboxs.addEventListener('mouseleave', pointerUp12552)
containerboxs.addEventListener('mousemove', pointerMove12552)
containerboxs.addEventListener('touchleave', pointerUp12552)
containerboxs.addEventListener('touchmove', pointerMove12552)

initialpositions = containerids.offsetLeft

// prevent menu popup on long press
window.oncontextmenu = function (event) {
    event.preventDefault()
    event.stopPropagation()
    return false
  }
  
// the touch or mousedown function
function pointerDown12552 (event) {
     event.preventDefault()
     //check if it's mouch clickec or touched clicked
    if (event.type == "touchstart") {
      posX12552 = event.touches[0].clientX;
    } else {
      posX12552 = event.clientX;
    }
    console.log("hey")
    startPosss = posX12552 - initialpositions;
    console.log(startPosss)
    isDraggingss = true
     
      
  }
  
  function pointerMove12552(event) {
    if (event.type == "touchmove") {
    
      if (isDraggingss) {
        event.preventDefault()
        const currentPosition122552 = event.touches[0].clientX;
        const dist22552 = currentPosition122552 - startPosss
        initialpositions = dist22552
        console.log(currentPosition122552)
        console.log(dist22552)
        contaiinerinners.style.left = `${dist22552}px`;
        checkboundaries12552()
        console.log("love")}
        
    } else {
      if (isDraggingss) {
        event.preventDefault()
        const currentPosition122552 = event.clientX 
        const dist22552 = currentPosition122552 - startPosss
        initialpositions = dist22552
        console.log(currentPosition122552)
        console.log(dist22552)
        contaiinerinners.style.left = `${dist22552}px`;
        checkboundaries12552()
        console.log("love")
        
    }
   

    }
  }
  
  function pointerUp12552() {
    
    isDraggingss = false
    console.log("hee")
  
  }
  // to check end boundaries and ensure it's not crossed
function checkboundaries12552(){
  let outermeaser22552 = containerboxs.getBoundingClientRect();
  let innermeaser22552 = contaiinerinners.getBoundingClientRect();
  if (parseInt(contaiinerinners.style.left) > 0){
    contaiinerinners.style.left = '0px';

  }
  else if(innermeaser22552.right < outermeaser22552.right){
    contaiinerinners.style.left = `-${innermeaser22552.width - outermeaser22552.width}px`
  }
}



  var nxtBtn15442 = document.querySelector('.preaa-btn22');
  var preBtn15442=  document.querySelector('.nxteaa-btn22');
  
  

  nxtBtn15442.addEventListener("click", () => switchSlide22552("next"));
  preBtn15442.addEventListener("click", () => switchSlide22552("prev"));

  function switchSlide22552(arg) {

      initial657 = containerid.offsetLeft;
    
      if (arg == "next") {
        contaiinerinner.style.left = `${initial657 + size}px`;
      
      } else {
        contaiinerinner.style.left = `${initial657 - size}px`;
      
      }
   checkboundaries12552()
   
  }









  
var initialpositionss;
var isDraggingsss;
var startPossss;

var initial6577s;

var containerboxss = document.querySelector('.drug-section8')
var containerid22s = document.getElementById('drug-section8_id')
var contaiinerinnerss = document.querySelector('.drug-wrapper8')
var containeridss = document.getElementById('drug-wrapper8_id')
  // disable default image drag
containerboxss.addEventListener('dragstart', (e) => e.preventDefault())
// pointer events
containerboxss.addEventListener('mousedown', pointerDown12552s)
containerboxss.addEventListener('touchstart', pointerDown12552s)
containerboxss.addEventListener('mouseup', pointerUp12552s)
containerboxss.addEventListener('mouseleave', pointerUp12552s)
containerboxss.addEventListener('mousemove', pointerMove12552s)
containerboxss.addEventListener('touchleave', pointerUp12552s)
containerboxss.addEventListener('touchmove', pointerMove12552s)

initialpositionss = containeridss.offsetLeft

// prevent menu popup on long press
window.oncontextmenu = function (event) {
    event.preventDefault()
    event.stopPropagation()
    return false
  }
  
// the touch or mousedown function
function pointerDown12552s (event) {
     event.preventDefault()
     //check if it's mouch clickec or touched clicked
    if (event.type == "touchstart") {
      posX12552s = event.touches[0].clientX;
    } else {
      posX12552s = event.clientX;
    }
    console.log("hey")
    startPossss = posX12552s - initialpositionss;
    console.log(startPossss)
    isDraggingsss = true
     
      
  }
  
  function pointerMove12552s(event) {
    if (event.type == "touchmove") {
    
      if (isDraggingsss) {
        event.preventDefault()
        const currentPosition122552s = event.touches[0].clientX;
        const dist22552s = currentPosition122552s - startPossss
        initialpositionss = dist22552s
        console.log(currentPosition122552s)
        console.log(dist22552s)
        contaiinerinnerss.style.left = `${dist22552s}px`;
        checkboundaries12552s()
        console.log("love")}
        
    } else {
      if (isDraggingsss) {
        event.preventDefault()
        const currentPosition122552s = event.clientX 
        const dist22552s = currentPosition122552s - startPossss
        initialpositionss = dist22552s
        console.log(currentPosition122552s)
        console.log(dist22552s)
        contaiinerinnerss.style.left = `${dist22552s}px`;
        checkboundaries12552s()
        console.log("love")
        
    }
   

    }
  }
  
  function pointerUp12552s() {
    
    isDraggingsss = false
    console.log("hee")
  
  }
  // to check end boundaries and ensure it's not crossed
function checkboundaries12552s(){
  let outermeaser22552s = containerboxss.getBoundingClientRect();
  let innermeaser22552s = contaiinerinnerss.getBoundingClientRect();
  if (parseInt(contaiinerinnerss.style.left) > 0){
    contaiinerinnerss.style.left = '0px';

  }
  else if(innermeaser22552s.right < outermeaser22552s.right){
    contaiinerinnerss.style.left = `-${innermeaser22552s.width - outermeaser22552s.width}px`
  }
}



  var nxtBtn15442s = document.querySelector('.preaa-btn22');
  var preBtn15442s=  document.querySelector('.nxteaa-btn22');
  
  

  nxtBtn15442s.addEventListener("click", () => switchSlide22552s("next"));
  preBtn15442s.addEventListener("click", () => switchSlide22552s("prev"));

  function switchSlide22552s(arg) {

      initial657s = containeridss.offsetLeft;
    
      if (arg == "next") {
        contaiinerinnerss.style.left = `${initial657s + size}px`;
      
      } else {
        contaiinerinnerss.style.left = `${initial657 - size}px`;
      
      }
   checkboundaries12552s()
   
  }













  
var initialpositionse;
var isDraggingsse;
var startPossse;

var initial6577e;

var containerboxse = document.querySelector('.drug-container22')
var containerid22e = document.getElementById('drug-container82_id')
var contaiinerinnerse = document.querySelector('.drug-wrapper102')
var containeridse = document.getElementById('drug_wrapper22_id')
  // disable default image drag
containerboxse.addEventListener('dragstart', (e) => e.preventDefault())
// pointer events
containerboxse.addEventListener('mousedown', pointerDown12552e)
containerboxse.addEventListener('touchstart', pointerDown12552e)
containerboxse.addEventListener('mouseup', pointerUp12552e)
containerboxse.addEventListener('mouseleave', pointerUp12552e)
containerboxse.addEventListener('mousemove', pointerMove12552e)
containerboxse.addEventListener('touchleave', pointerUp12552e)
containerboxse.addEventListener('touchmove', pointerMove12552e)

initialpositionse = containeridse.offsetLeft

// prevent menu popup on long press
window.oncontextmenu = function (event) {
    event.preventDefault()
    event.stopPropagation()
    return false
  }
  
// the touch or mousedown function
function pointerDown12552e (event) {
     event.preventDefault()
     //check if it's mouch clickec or touched clicked
    if (event.type == "touchstart") {
      posX12552e = event.touches[0].clientX;
    } else {
      posX12552e = event.clientX;
    }
    console.log("hey")
    startPossse = posX12552e - initialpositionse;
    console.log(startPossse)
    isDraggingsse = true
     
      
  }
  
  function pointerMove12552e(event) {
    if (event.type == "touchmove") {
    
      if (isDraggingsse) {
        event.preventDefault()
        const currentPosition122552e = event.touches[0].clientX;
        const dist22552e = currentPosition122552e - startPossse
        initialpositionse = dist22552e
        console.log(currentPosition122552e)
        console.log(dist22552e)
        contaiinerinnerse.style.left = `${dist22552e}px`;
        checkboundaries12552e()
        console.log("love")}
        
    } else {
      if (isDraggingsse) {
        event.preventDefault()
        const currentPosition122552e = event.clientX 
        const dist22552e = currentPosition122552e - startPossse
        initialpositionse = dist22552e
        console.log(currentPosition122552e)
        console.log(dist22552e)
        contaiinerinnerse.style.left = `${dist22552e}px`;
        checkboundaries12552e()
        console.log("love")
        
    }
   

    }
  }
  
  function pointerUp12552e() {
    
    isDraggingsse = false
    console.log("hee")
  
  }
  // to check end boundaries and ensure it's not crossed
function checkboundaries12552e(){
  let outermeaser22552e = containerboxse.getBoundingClientRect();
  let innermeaser22552e = contaiinerinnerse.getBoundingClientRect();
  if (parseInt(contaiinerinnerse.style.left) > 0){
    contaiinerinnerse.style.left = '0px';

  }
  else if(innermeaser22552e.right < outermeaser22552e.right){
    contaiinerinnerse.style.left = `-${innermeaser22552e.width - outermeaser22552e.width}px`
  }
}



  var nxtBtn15442e = document.querySelector('.preaa-btn22');
  var preBtn15442e=  document.querySelector('.nxteaa-btn22');
  
  

  nxtBtn15442e.addEventListener("click", () => switchSlide22552e("next"));
  preBtn15442e.addEventListener("click", () => switchSlide22552e("prev"));

  function switchSlide22552e(arg) {

      initial657e = containeride.offsetLeft;
    
      if (arg == "next") {
        contaiinerinnere.style.left = `${initial657e + size}px`;
      
      } else {
        contaiinerinnere.style.left = `${initial657e - size}px`;
      
      }
   checkboundaries12552e()
   
  }



var siebar = Array.from(document.querySelectorAll('.drug-sidebar'))
var siebar2 = Array.from(document.querySelectorAll('.drug-innersidebar'))
var sideinfo = Array.from(document.querySelectorAll('.drug-informations'))
var index;

siebar.forEach((number, index, arr) => {
  index=index
  $(sideinfo[index]).on('click', function(){
    if(number.style.display == 'none'){
      number.classList.add("showing");
      siebar2[index].classList.add("showing");
    $(siebar2[index]).show();
    $(number).show();
  }
  else{
    number.classList.remove("showing");
    siebar2[index].classList.remove("showing");
    $(siebar2[index]).hide();
    $(number).hide();
  }
   
  })
});


  $('.banner').on('click', function(){
    console.log('hey')
    siebar.forEach((number1, index)=>{
      index=index
    if(number1.style.display != 'none'){
    $(siebar2[index]).hide();
    $(number1).hide();}
  })
  
}
)

$('.drug-inner-div1').on('click', function(){
  console.log('hey')
  siebar.forEach((number1, index)=>{
    index=index
  if(number1.style.display != 'none'){
  $(siebar2[index]).hide();
  $(number1).hide();}
})

}
)



document.querySelectorAll('.room-name-submit').forEach(button => {
  button.onclick = function(e) {
      e.preventDefault();  // Prevent default button behavior
      const username = button.getAttribute('data-pharm-name');  // Get pharmacist name from data attribute
      
      // Construct the URL for the chat
      const roomName = "default";  // Use a default room name or handle as needed
      window.location.pathname = '/pharm_chat/chat/' + username + '/';  // Redirect to chat room
  };
});
