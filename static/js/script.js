// User Profile Dropdown 
const userProfileIcon = document.querySelectorAll('.profile-icon');
const userProfileDropDown = document.querySelectorAll('.user-profile-drop-down-menu'); 

for (let i = 0; i < userProfileIcon.length; i++) {
    userProfileIcon[i].addEventListener("click", function() {
        for (let i = 0; i < userProfileDropDown.length; i++) {
            userProfileDropDown[i].classList.toggle("profile-active");    
        }
    })
}

// Main Navigation

const navButtonSkin = document.querySelectorAll(".js-nav-button-skincare");
const navDropDownSkin = document.querySelector(".skincare-container");

for(let i = 0; i < navButtonSkin.length; i++) {
    navButtonSkin[i].addEventListener("mousemove", () => {
        navDropDownSkin.classList.add("main-nav-js");
    })
}

window.addEventListener("mouseout", () => {
    navDropDownSkin.classList.remove("main-nav-js");
})

const navButtonBrand = document.querySelectorAll(".js-nav-button-brands");
const navDropDownBrand = document.querySelector(".brands-container");

for(let i = 0; i < navButtonBrand.length; i++) {
    navButtonBrand[i].addEventListener("mousemove", () => {
        navDropDownBrand.classList.add("main-nav-js");
    })
}

window.addEventListener("mouseout", () => {
    navDropDownBrand.classList.remove("main-nav-js");
})


const navButtonSkinType = document.querySelectorAll(".js-nav-button-skin-type");
const navDropDownSkinType = document.querySelector(".skin-type-container");

for(let i = 0; i < navButtonSkinType.length; i++) {
    navButtonSkinType[i].addEventListener("mousemove", () => {
        navDropDownSkinType.classList.add("main-nav-js");
    })
}

window.addEventListener("mouseout", () => {
    navDropDownSkinType.classList.remove("main-nav-js");
})

const navButtonSkinConcern = document.querySelectorAll(".js-nav-button-skin-concern");
const navDropDownSkinConcern = document.querySelector(".skin-concern-container");

for(let i = 0; i < navButtonSkinConcern.length; i++) {
    navButtonSkinConcern[i].addEventListener("mousemove", () => {
        navDropDownSkinConcern.classList.add("main-nav-js");
    })
}

window.addEventListener("mouseout", () => {
    navDropDownSkinConcern.classList.remove("main-nav-js");
})


// Mobile Navigation Dropdown 
const hamburger = document.querySelector(".burger-menu"); 
const navMenu = document.querySelector(".mobile-navigation-container"); 

hamburger.addEventListener("click", () => {
    navMenu.classList.toggle("mobile-nav-active");
})

// Mobile Serach Bar Dropdown 
const searchIcon = document.querySelector(".search-bar-mobile"); 
const search = document.querySelector(".mobile-serach-bar-container");

searchIcon.addEventListener("click", () =>{
    search.classList.toggle("search-active");
})

//Carousel 
// let i = 0; 
// let slides = []; 
// let slideFade = 6000; 

//Slide Images 
// slides[0] = "media/ample_n.webp"; 
// slides[1] = "media/banila_co.webp"; 
// slides[2] = "media/beauty_of_joseon.webp";
// slides[3] = "media/benton.jpeg";
// slides[4] = "media/by_wishtrend.webp"; 

//Slide Fade 
// function slideChange() {
//     document.slide.src = slides[i]; 
//     if(i < slides.length - 1) {
//         i++; 
//     }else{
//         i = 0; 
//     }
//     setTimeout("slideChange()", slideFade);
// }
// window.onload = slideChange; 