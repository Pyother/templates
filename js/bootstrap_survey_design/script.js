menuArray = ["sectionOne", "sectionSecond", "sectionThird", "sectionFourth", "sectionFifth", "sectionSixth"]
elementArray = ["menu-one", "menu-second", "menu-third", "menu-fourth", "menu-fifth", "menu-sixth"]

for(let i=0; i<6; i++) {
    const menu = document.getElementById(menuArray[i]);
    menu.addEventListener("mouseenter", event => {
        document.getElementById(elementArray[i]).style.fontWeight = "bold";}, false);
    menu.addEventListener("mouseleave", event => {
        document.getElementById(elementArray[i]).style.fontWeight = "normal";}, false);
    }
