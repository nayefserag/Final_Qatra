////////////////////  Scroll Animation  //////////////////////////
ScrollReveal({
     reset: true,
     distance: '80px',
     duration:2000,
     delay:200
});
ScrollReveal().reveal('.navbar , .video, .donation__prosess , .image , .steps_box ', { origin:'top' });
ScrollReveal().reveal('.content', { origin:'bottom' });
ScrollReveal().reveal('.donation__information ', { origin:'right' });
// ScrollReveal().reveal('.footer__row', { origin:'left' });
////////////////////  pop Up Button  //////////////////////////
let popup = document.getElementById("popup");
function openPopup()
{
     popup.classList.add('open-popup');
     document.body.classList.add('blur-background');
}
function closePopup()
{
     popup.classList.remove('open-popup');
     document.body.classList.remove('blur-background');
}
////////////////////  scroll up btn  //////////////////////////
let scrollBtn = document.querySelector(".scrollBtn");
window.onscroll = function()
{
     console.log(this.scrollY);
     if (this.scrollY >= 576)
     {
          scrollBtn.classList.add("show");
     }
     else
     {
          scrollBtn.classList.remove("show");
     }
}
scrollBtn.onclick = function()
{
     window.scrollTo({
          top : 0 ,
          behavior : "smooth",
     });
};
////////////////////  scroll up btn  //////////////////////////