////////////////////  Scroll Animation  //////////////////////////
ScrollReveal({
     reset: true,
     distance: '80px',
     duration:2000,
     delay:200
});
ScrollReveal().reveal('.navbar , .video, .donation__prosess , .image , .steps_box ,.image_location ,.image_time , .prosess_box', { origin:'top' });
ScrollReveal().reveal('.content , .content_location , .content_time', { origin:'bottom' });
ScrollReveal().reveal('.donation__information', { origin:'right' });
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