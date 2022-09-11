menuArray = ["sectionOne", "sectionSecond", "sectionThird", "sectionFourth", "sectionFifth", "sectionSixth", "sectionSeventh", "sectionEighth", "sectionNinth"]
elementArray = ["menu-one", "menu-second", "menu-third", "menu-fourth", "menu-fifth", "menu-sixth", "menu-seventh", "menu-eighth", "menu-ninth"]

for(let i=0; i<9; i++) {
    const menu = document.getElementById(menuArray[i]);
    menu.addEventListener("mouseenter", event => {
        document.getElementById(elementArray[i]).style.fontWeight = "bold";}, false);
    menu.addEventListener("mouseleave", event => {
        document.getElementById(elementArray[i]).style.fontWeight = "normal";}, false);
    }
 