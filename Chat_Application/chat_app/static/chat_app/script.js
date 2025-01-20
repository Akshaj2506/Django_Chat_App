document.getElementById("toggle-sidebar").addEventListener("click", () => {
   document.getElementById("user-menu-container").classList.toggle("collapsed")
   if (window.innerWidth >= 991) document.getElementById("chat-area").classList.toggle("collapsed")
   document.getElementById("right-area").classList.toggle("collapsed")
   document.getElementById("users-menu").classList.toggle("vanish")
})

function adjustPageSize() {
   const screenWidth = window.innerWidth;
   const body = document.body;

   body.style.transform = "";
   body.style.transformOrigin = "top left";

   if (screenWidth > 992 && screenWidth <= 1600) {
      body.style.transform = "scale(0.9)";
   } else if (screenWidth >= 768 && screenWidth <= 991) {
      body.style.transform = "scale(0.85)";
   } else if (screenWidth >= 700 && screenWidth <= 767) {
      body.style.transform = "scale(0.8)";
   } else if (screenWidth >= 600 && screenWidth < 700) {
      body.style.transform = "scale(1)";
      body.style.width = "75%";
   } else if (screenWidth <= 600) {
      body.style.transform = "scale(1)";
      body.style.width = "50%";
   }
}

window.addEventListener("resize", adjustPageSize);

adjustPageSize();
