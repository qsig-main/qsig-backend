// function toggleDivP() {
//     var itemContainerDiv = document.querySelector('.item-container-p'); 
//     if (itemContainerDiv.style.display === 'flex') {
//       itemContainerDiv.style.display = 'none'; 
//       itemContainerDiv.style.maxHeight = '0px';
//     } else {
//       itemContainerDiv.style.display = 'flex'; 
//       itemContainerDiv.style.maxHeight = itemContainerDiv.scrollHeight + 'px';
//     }
// }


// function toggleDivP() {
//   var itemContainerDiv = document.querySelector('.item-container-p'); 
//   if (itemContainerDiv.style.maxHeight === '0px') {
//     itemContainerDiv.style.maxHeight = itemContainerDiv.scrollHeight + 'px';
//   } else {
//     itemContainerDiv.style.maxHeight = '0px';
//   }
// }

function toggleDivP() {
  var itemContainerDiv = document.querySelector('.item-container-p'); 
  itemContainerDiv.classList.toggle('show');
}


function toggleDivPi() {
    var itemContainerDiv = document.querySelector('.item-container-pi'); 
    itemContainerDiv.classList.toggle('show');
}

function toggleDivR() {
    var itemContainerDiv = document.querySelector('.item-container-r'); 
    itemContainerDiv.classList.toggle('show');
}

function toggleDivRi() {
    var itemContainerDiv = document.querySelector('.item-container-ri'); 
    itemContainerDiv.classList.toggle('show');
}

function toggleDivM() {
    var itemContainerDiv = document.querySelector('.item-container-m'); 
    itemContainerDiv.classList.toggle('show');
}
  

function toggleDivCC() {
    var itemContainerDiv = document.querySelector('.item-container-cc'); 
    itemContainerDiv.classList.toggle('show');
}
  