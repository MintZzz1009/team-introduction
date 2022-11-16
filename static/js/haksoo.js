document.addEventListener('DOMContentLoaded', () => {

  const cards = document.querySelectorAll(".card")
  for(const card of cards) {
    card.addEventListener("click", flipper)
  }
  
    function flipper (event) {
      const target = event.currentTarget
      target.style.transform = "rotateY(180deg)"
      target.addEventListener("click", innerFlipper)
    }

    function innerFlipper (event) {
      const target = event.currentTarget
      target.style.transform = "rotateY(0deg)"
      target.addEventListener("click", flipper)
      target.removeEventListener("click", innerFlipper)
    }
})