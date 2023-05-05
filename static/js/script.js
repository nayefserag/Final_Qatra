////////////////////  Scroll Animation  //////////////////////////
ScrollReveal({
     reset: true,
     distance: '80px',
     duration:2000,
     delay:200
});
ScrollReveal().reveal('.navbar , .video, .donation__prosess , .image , .steps_box ,.image_location ,.image_time , .prosess_box', { origin:'top' });
ScrollReveal().reveal('.content , .content_location , .content_time', { origin:'bottom' });
ScrollReveal().reveal('.donation__information ', { origin:'right' });
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

let icon = document.getElementById("icon");
icon.onclick = function()
{
     document.body.classList.toggle("dark-mode");
     if (document.body.classList.contains("dark-mode"))
     {
           icon.src = "/Login_Sginup/static/images/sun.png";

     }
     else
     {

           icon.src = "/Login_Sginup/static/images/moon.gif";

     }
};
