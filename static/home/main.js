var f=document.querySelector('.f');
var t=document.querySelector('.t');
var mfrom=document.getElementById('mfrom');
var fromm=document.getElementById('fromm')
var too=document.getElementById('too')
var to=document.getElementById('to');
var mto=document.getElementById('mto');
var fcities=document.querySelectorAll('.from-card div span')
var tcities=document.querySelectorAll('.to-card div span')
var rotate=document.querySelector('.fa-arrows-rotate')
var date=document.getElementById('date')
var calendar=document.querySelector('.fa-calendar')
mfrom.addEventListener('click',function(){
    f.classList.toggle('hide')
    t.classList.add('hide')
})
mto.addEventListener('click',()=>{
    t.classList.toggle('hide')
    f.classList.add('hide')
})

rotate.addEventListener('click',()=>{

        mf2=mto.innerHTML
        mto.innerHTML=mfrom.innerHTML
        mfrom.innerHTML=mf2


})
fcities.forEach((fcity)=>{
    fcity.addEventListener('click',()=>{
        mfrom.innerHTML=fcity.innerText
        f.classList.add('hide')
        fromm.innerText=fcity.innerText
        if(mfrom.innerHTML==mto.innerHTML){
            alert("From and to can't be same")
            mfrom.innerHTML="From"
        }
    })
})

tcities.forEach((tcity)=>{
    tcity.addEventListener('click',()=>{
        mto.innerHTML=tcity.innerText
        t.classList.add('hide')
        too.innerText=tcity.innerText
       if(mto.innerHTML==mfrom.innerHTML){
        alert("From and to can't be same")
        mto.innerHTML="To"
    }
    })
    
})


