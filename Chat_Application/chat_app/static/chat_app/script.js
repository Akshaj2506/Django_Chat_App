document.getElementById("toggle-sidebar").addEventListener("click", () => {
   document.getElementById("user-menu-container").classList.toggle("collapsed")
   document.getElementById("chat-area").classList.toggle("collapsed")
   document.getElementById("right-area").classList.toggle("collapsed")
   document.getElementById("users-menu").classList.toggle("vanish")
})