const gradel_list=document.querySelectorAll("#grad");
const binel_list=document.querySelectorAll('#bin');
function bintext(val){
  if(val==='0'){
    return 'Not as Expected';
  }
  else {
    return 'Excellent';
  }
};
function gradedtext(val){
  if(val==='0'){
    return 'Not as Expected';
  }
  else if(val==='1'){
    return 'Slight Non-Compliance';
  }
  else if(val==='2'){
    return 'Largely Compliant';
  }
  else {
    return 'Excellent';
  }
};

var gradels_array = [...gradel_list]; // converts NodeList to Array
gradels_array.forEach(gradel => {
  gradel.addEventListener('mouseover',() =>{
    let textel=gradel.parentElement.nextElementSibling.firstChild;
    textel.style.opacity=1;
  });
  gradel.addEventListener('input',() =>{
    let textel=gradel.parentElement.nextElementSibling.firstChild;
    textel.innerHTML=gradedtext(gradel.value);
    textel.style.opacity=1;
  });
  gradel.addEventListener('mouseout',() =>{
    let textel=gradel.parentElement.nextElementSibling.firstChild;
    textel.style.opacity=0;
  });

});

var binel_array = [...binel_list];
binel_array.forEach(binel => {
  
  binel.addEventListener('mouseover',() =>{
    let textel=binel.parentElement.nextElementSibling.firstChild;
    textel.style.opacity=1;
  });
  binel.addEventListener('input',() =>{
    let textel=binel.parentElement.nextElementSibling.firstChild;
    textel.innerHTML=bintext(binel.value);
    textel.style.opacity=1;
  });
  binel.addEventListener('mouseout',() =>{
    let textel=binel.parentElement.nextElementSibling.firstChild;
    textel.style.opacity=0;
  });
  
});

function navtochapter(id){
  search_query=new URLSearchParams(window.location.search);
  search_query.set('chapter',id);
  let pageurl=window.location.href;
  let baseurl=pageurl.substring(0,pageurl.indexOf('?'));
  let newurl=baseurl+'?'+search_query.toLocaleString();
  window.location.href=newurl;
};

const chapters_list=document.querySelectorAll(".chapter-div");
const chapters_array=[...chapters_list];
chapters_array.forEach(chapter => {
  chapter.addEventListener('click',() => navtochapter(chapter.id));
});



