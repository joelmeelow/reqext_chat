const slides = Array.from(document.querySelectorAll('.products-product-div'));
const prevBtn = document.getElementById('prea-btn2');
const nextBtn = document.getElementById('nxta-btn2');
const dots = document.querySelectorAll('.dot')




// add our event listeners
slides.forEach((slide, index) => {
  const slideImage = slide.querySelector('img')
  // disable default image drag
  slideImage.addEventListener('dragstart', (e) => e.preventDefault())
  // pointer events

})

// prevent menu popup on long press
window.oncontextmenu = function (event) {
  event.preventDefault()
  event.stopPropagation()
  return false
}




let index = 0;

// Adding opacity to first dot on first time

dots[0].style.opacity ='1'

// positioning the slides

slides.forEach((slide,index)=>{
  slide.style.left=`${index*100}%`
});


// move slide function

const moveSlide = () =>{
  slides.forEach((slide)=>{
    slide.style.transform=`translateX(-${index*100}%)`;
  });
}

// remove dots opacity 1 from all dots

const removeDotsOpacity = () =>{
  dots.forEach((dot)=>{
    dot.style.opacity='.2';
  });
}

dots.forEach((dot,i)=>{
  dot.addEventListener("click",(e)=>{
    index=i;
    removeDotsOpacity();
    e.target.style.opacity='1'
    moveSlide();
  })
});

// show the previous slide

prevBtn.addEventListener('click',()=>{
  if(index===0) return index;
  index--;
  removeDotsOpacity();
  dots[index].style.opacity='1'
  moveSlide();
});

// show the next slide

nextBtn.addEventListener('click',()=>{
  if(index===slides.length-1) return index;
  index++;
  removeDotsOpacity();
  dots[index].style.opacity='1'
  moveSlide();
});

// auto play slide

const autoPlaySlide = () =>{
  removeDotsOpacity();
  if(index===slides.length-1) index= -1;
  index++;
  dots[index].style.opacity='1'
  moveSlide();
}

window.onload=()=>{
  setInterval(autoPlaySlide,6000);
}










let boxcont  = document.querySelector('.product_category3')
const boxcont2 = document.getElementById('productcat')
console.log(boxcont2.offsetLeft)
boxcont.addEventListener('click', (e) =>{
  console.log(e)
})
console.log(boxcont.offsetleft)
let cateContain = document.querySelector('.category_container2')
const cateContain2 = document.getElementById('categorycontainer')
console.log(cateContain2.offsetLeft)

// set up our state
let isDragging1 = false
let startPos123 = 0
let offrem;
let size = 200;
let initial2 = cateContain2.offsetLeft;
let initial23;

  // disable default image drag
  boxcont.addEventListener('dragstart', (e) => e.preventDefault())
  // pointer events
  boxcont.addEventListener('mousedown', pointerDown)
  boxcont.addEventListener('touchstart', pointerDown)
  boxcont.addEventListener('mouseup', pointerUp)
  boxcont.addEventListener('mouseleave', pointerUp)
  boxcont.addEventListener('mousemove', pointerMove)
  boxcont.addEventListener('touchleave', pointerUp)
  boxcont.addEventListener('touchmove', pointerMove)
  



// prevent menu popup on long press
window.oncontextmenu = function (event) {
    event.preventDefault()
    event.stopPropagation()
    return false
  }
  cateContain.addEventListener('click', (e) =>{
    console.log(e)
    offrem = e.target.offsetleft;
  
  })
  console.log(offrem)
/// the touch or mousedown function
function pointerDown (event) {
  event.preventDefault()
  //check if it's mouch clickec or touched clicked
 if (event.type == "touchstart") {
   posX12 = event.touches[0].clientX;
 } else {
   posX12 = event.clientX;
 }
 console.log("hey")
 startPos123 = posX12 - initial2;
 console.log(startPos123)
 isDragging1 = true
  
   
}

function pointerMove(event) {
 if (event.type == "touchmove") {
 
   if (isDragging1) {
     event.preventDefault()
     const currentPosition1 = event.touches[0].clientX;
     const dist = currentPosition1 - startPos123
     initial2 = dist
     console.log(currentPosition1)
     console.log(dist)
     cateContain .style.left = `${dist}px`;
     checkboundaries()
     console.log("love")}
     
 } else {
   if (isDragging1) {
     event.preventDefault()
     const currentPosition1 = event.clientX 
     const dist = currentPosition1 - startPos123
     initial2 = dist
     console.log(currentPosition1)
     console.log(dist)
     cateContain .style.left = `${dist}px`;
     checkboundaries()
     console.log("love")
     
 }


 }
}

function pointerUp() {
 
 isDragging1 = false
 console.log("hee")

}
// to check end boundaries and ensure it's not crossed
  function checkboundaries(){
    let outermeaser = boxcont2.getBoundingClientRect();
    let innermeaser = cateContain2.getBoundingClientRect();
    if (parseInt(cateContain.style.left) > 0){
      cateContain.style.left = '0px';

    }
    else if(innermeaser.right < outermeaser.right){
      cateContain.style.left = `-${innermeaser.width - outermeaser.width}px`
    }
  }
  


  var nxtBtn2 = document.querySelector('.preaa-btn');
  var preBtn2=  document.querySelector('.nxteaa-btn');
  
 
  

  nxtBtn2.addEventListener("click", () => switchSlide2("next"));
  preBtn2.addEventListener("click", () => switchSlide2("prev"));

function switchSlide2(arg) {

  
    initial23 = cateContain2.offsetLeft;
   
    if (arg == "next") {
      cateContain.style.left = `${initial2 + size}px`;
     
    } else {
      cateContain.style.left = `${initial2 - size}px`;
    
    }
   checkboundaries()
  
  }














  



  
// set up our state
let initialposition1;
let isDragging122 = false
let startPos124 = 0


let initial6;




let boxprod12  = document.querySelector('.product4')
const boxprod2 = document.getElementById('product_id')


const prodContain22 = document.getElementById('container_id')
console.log(prodContain22.offsetLeft)
let prodcontainer2 = document.querySelector('.producttainer')

initialposition1 = prodContain22.offsetLeft;

  // disable default image drag
boxprod12.addEventListener('dragstart', (e) => e.preventDefault())
// pointer events
boxprod12.addEventListener('mousedown', pointerDown12)
boxprod12.addEventListener('touchstart', pointerDown12)
boxprod12.addEventListener('mouseup', pointerUp12)
boxprod12.addEventListener('mouseleave', pointerUp12)
boxprod12.addEventListener('mousemove', pointerMove12)
boxprod12.addEventListener('touchleave', pointerUp12)
boxprod12.addEventListener('touchmove', pointerMove12)



// prevent menu popup on long press
window.oncontextmenu = function (event) {
    event.preventDefault()
    event.stopPropagation()
    return false
  }
  
// the touch or mousedown function
function pointerDown12 (event) {
     event.preventDefault()
     //check if it's mouch clickec or touched clicked
    if (event.type == "touchstart") {
      posX12 = event.touches[0].clientX;
    } else {
      posX12 = event.clientX;
    }
    console.log("hey")
    startPos124 = posX12 - initialposition1;
    console.log(startPos124)
    isDragging122 = true
     
      
  }
  
  function pointerMove12(event) {
    if (event.type == "touchmove") {
    
      if (isDragging122) {
        event.preventDefault()
        const currentPosition122 = event.touches[0].clientX;
        const dist22 = currentPosition122 - startPos124
        initialposition1 = dist22
        console.log(currentPosition122)
        console.log(dist22)
        prodcontainer2.style.left = `${dist22}px`;
        checkboundaries12()
        console.log("love")}
        
    } else {
      if (isDragging122) {
        event.preventDefault()
        const currentPosition122 = event.clientX 
        const dist22 = currentPosition122 - startPos124
        initialposition1 = dist22
        console.log(currentPosition122)
        console.log(dist22)
        prodcontainer2.style.left = `${dist22}px`;
        checkboundaries12()
        console.log("love")
        
    }
   

    }
  }
  
  function pointerUp12() {
    
    isDragging122 = false
    console.log("hee")
  
  }
  // to check end boundaries and ensure it's not crossed
function checkboundaries12(){
  let outermeaser22 = boxprod2.getBoundingClientRect();
  let innermeaser22 = prodContain22.getBoundingClientRect();
  if (parseInt(prodcontainer2.style.left) > 0){
    prodcontainer2.style.left = '0px';

  }
  else if(innermeaser22.right < outermeaser22.right){
    prodcontainer2.style.left = `-${innermeaser22.width - outermeaser22.width}px`
  }
}



  var nxtBtn15 = document.querySelector('.btnpre');
  var preBtn15=  document.querySelector('.ptnnxt');
  
  

  nxtBtn15.addEventListener("click", () => switchSlide22("next"));
  preBtn15.addEventListener("click", () => switchSlide22("prev"));

function switchSlide22(arg) {

    initial6 = prodContain22.offsetLeft;
   
    if (arg == "next") {
      prodcontainer2.style.left = `${initial6 + size}px`;
     
    } else {
      prodcontainer2.style.left = `${initial6 - size}px`;
    
    }
   checkboundaries12()
   
  }

 









  
  
// set up our state
let initialposition12;
let isDragging1222 = false
let startPos1244 = 0


let initial66;




let boxprod122  = document.querySelector('.product3')
const boxprod22 = document.getElementById('product_product2')


const prodContain222 = document.getElementById('products_containers')
console.log(prodContain222.offsetLeft)
let prodcontainer22 = document.querySelector('.productbox')

initialposition12 = prodContain222.offsetLeft;

  // disable default image drag
boxprod122.addEventListener('dragstart', (e) => e.preventDefault())
// pointer events
boxprod122.addEventListener('mousedown', pointerDown122)
boxprod122.addEventListener('touchstart', pointerDown122)
boxprod122.addEventListener('mouseup', pointerUp122)
boxprod122.addEventListener('mouseleave', pointerUp122)
boxprod122.addEventListener('mousemove', pointerMove122)
boxprod122.addEventListener('touchleave', pointerUp122)
boxprod122.addEventListener('touchmove', pointerMove122)



// prevent menu popup on long press
window.oncontextmenu = function (event) {
    event.preventDefault()
    event.stopPropagation()
    return false
  }
  
// the touch or mousedown function
function pointerDown122 (event) {
     event.preventDefault()
     //check if it's mouch clickec or touched clicked
    if (event.type == "touchstart") {
      posX122 = event.touches[0].clientX;
    } else {
      posX122 = event.clientX;
    }
    console.log("hey")
    startPos1244 = posX122 - initialposition12;
    console.log(startPos1244)
    isDragging1222 = true
     
      
  }
  
  function pointerMove122(event) {
    if (event.type == "touchmove") {
    
      if (isDragging1222) {
        event.preventDefault()
        const currentPosition1222 = event.touches[0].clientX;
        const dist222 = currentPosition1222 - startPos1244
        initialposition12 = dist222
        console.log(currentPosition1222)
        console.log(dist222)
        prodcontainer22.style.left = `${dist222}px`;
        checkboundaries122()
        console.log("love")}
        
    } else {
      if (isDragging1222) {
        event.preventDefault()
        const currentPosition1222 = event.clientX 
        const dist222 = currentPosition1222 - startPos1244
        initialposition12 = dist222
        console.log(currentPosition1222)
        console.log(dist222)
        prodcontainer22.style.left = `${dist222}px`;
        checkboundaries122()
        console.log("love")
        
    }
   

    }
  }
  
  function pointerUp122() {
    
    isDragging1222 = false
    console.log("hee")
  
  }
  // to check end boundaries and ensure it's not crossed
function checkboundaries122(){
  let outermeaser222 = boxprod22.getBoundingClientRect();
  let innermeaser222 = prodContain222.getBoundingClientRect();
  if (parseInt(prodcontainer22.style.left) > 0){
    prodcontainer22.style.left = '0px';

  }
  else if(innermeaser222.right < outermeaser222.right){
    prodcontainer22.style.left = `-${innermeaser222.width - outermeaser222.width}px`
  }
}



  var nxtBtn152 = document.querySelector('.pre-btn1');
  var preBtn152=  document.querySelector('.nxt-btn1');
  
  

  nxtBtn152.addEventListener("click", () => switchSlide222("next"));
  preBtn152.addEventListener("click", () => switchSlide222("prev"));

function switchSlide222(arg) {

    initial66 = prodContain222.offsetLeft;
   
    if (arg == "next") {
      prodcontainer22.style.left = `${initial66 + size}px`;
     
    } else {
      prodcontainer22.style.left = `${initial66 - size}px`;
    
    }
   checkboundaries122()
   
  }

 


 

