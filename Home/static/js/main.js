document.addEventListener('DOMContentLoaded', function() {
    // Access the book appointment button in the home page
    let bookAppointmentBtn = document.getElementById("bookAppointmentBtn");

    bookAppointmentBtn.addEventListener("click", function() {
        window.location.href = "/Home/booking_form.html/";
    });

    // Function for the small slider
    const smallSlider = document.querySelector('.small-slider .slider');
    let smallCounter = 1;

    function smallSlide() {
        smallSlider.style.transition = 'transform 0.5s ease-in-out';
        smallSlider.style.transform = 'translateX(' + (-smallCounter * 100) + '%)';
        smallCounter++;

        if (smallCounter >= smallSlider.children.length - 1) {
            setTimeout(() => {
                smallCounter = 1;
                smallSlider.style.transition = '';
                smallSlider.style.transform = 'translateX(' + (-smallCounter * 100) + '%)';
            }, 500);
        }
    }

    setInterval(smallSlide, 3000);

    // Function for the large slider
    const largeSlider = document.querySelector('.slider-container .slider');
    let largeCounter = 1;

    function largeSlide() {
        largeSlider.style.transition = 'transform 0.5s ease-in-out';
        largeSlider.style.transform = 'translateX(' + (-largeCounter * 100) + '%)';
        largeCounter++;

        if (largeCounter >= largeSlider.children.length - 1) {
            setTimeout(() => {
                largeCounter = 1;
                largeSlider.style.transition = '';
                largeSlider.style.transform = 'translateX(' + (-largeCounter * 100) + '%)';
            }, 500);
        }
    }

    setInterval(largeSlide, 3000);
});
