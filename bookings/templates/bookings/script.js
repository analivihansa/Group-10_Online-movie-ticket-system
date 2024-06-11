const container = document.querySelector('.seat-selection');
const seats = document.querySelectorAll('.row .seat:not(.occupied)');
const count = document.getElementById('count');
const total = document.getElementById('total');
const movieSelect = document.getElementById('movie');

let ticketPrice = +movieSelect.value;

// Update total and count
function updateSelectedCount() {
    const selectedSeats = document.querySelectorAll('.row .seat.selected');
    const selectedSeatsCount = selectedSeats.length;

    count.innerText = selectedSeatsCount;
    total.innerText = selectedSeatsCount * ticketPrice;
}

// Movie select event
movieSelect.addEventListener('change', (e) => {
    ticketPrice = +e.target.value;
    updateSelectedCount();
});

// Seat click event
container.addEventListener('click', (e) => {
    if (e.target.classList.contains('seat') && !e.target.classList.contains('occupied')) {
        e.target.classList.toggle('selected');

        updateSelectedCount();
    }
});



document.addEventListener('DOMContentLoaded', function () {
    const seats = document.querySelectorAll('.seat');
    const selectedSeatsInput = document.getElementById('selected-seats');
    const selectedSeatsDisplay = document.getElementById('selected-seats-display');

    seats.forEach(seat => {
        seat.addEventListener('click', () => {
            if (!seat.classList.contains('occupied')) {
                seat.classList.toggle('selected');
                updateSelectedSeats();
            }
        });
    });

    function updateSelectedSeats() {
        const selectedSeats = document.querySelectorAll('.seat.selected');
        const selectedSeatIds = Array.from(selectedSeats).map(seat => seat.id);
        selectedSeatsInput.value = selectedSeatIds.join(',');
        selectedSeatsDisplay.textContent = selectedSeatIds.join(', ');
    }
});
