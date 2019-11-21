// Begin of the glider
$(document).ready(function () {
	$('.glide').owlCarousel({
		center: true,
		items:2,
		loop:false,
		margin:10,
		responsive:{
			600:{
				items:4
			}
		}
	});
})

// $(document).ready(function () {
// 	myGlide.on("move.after", function() {
// 		var currentSlide = $(".glide__slide")[myGlide.index];
// 		console.log(currentSlide)

// 		var currentImg = $("." + currentSlide.classList[0] + " img:first-of-type")[0];

// 		var accountInfo = $("account_info");

// 		// Display current account selected information
// 		for (var item of accountInfo) {
// 			var sectionPk = item.attr("data-pk");

// 			if (sectionPk == currentImg.attr("data-pk")) {
// 				item.css("display", "block")
// 			} else {
// 				item.css("display", "none")
// 			}
// 		}

// 		let dot = $(".dot");

// 		for(let index in dot) {
// 			if (index === myGlide.index) {
// 				dot.eq(index).addClass("active");
// 			} else {
// 				dot.eq(index).removeClass("active");
// 			}
// 		}

// 	});

// 	document.getElementById("rightArrow").addEventListener("click", function() {
// 		myGlide.go(">");
// 	});
// 	document.getElementById("leftArrow").addEventListener("click", function() {
// 		myGlide.go("<");
// 	});

// 	let dots = document.querySelectorAll(".dot");
// 	let activeButton = document.querySelector(".active");

// 	dots.forEach((element, index) => {
// 		element.addEventListener("click", () => {
// 			console.log(activeButton);
// 			if (activeButton) {
// 				activeButton.classList.remove("active");
// 			}

// 			element.classList.add("active");
// 			activeButton = element;

// 			myGlide.go("=" + index);
// 		});
// 	});

// 	myGlide.mount();
// 	console.log(myGlide)

// 	// End of the glide
// })
