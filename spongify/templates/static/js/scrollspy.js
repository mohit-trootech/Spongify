/**Scrolls Py */
document.addEventListener("DOMContentLoaded", function () {
  const sections = document.querySelectorAll("section");
  const navLinks = document.querySelectorAll("nav a");

  const handleScroll = () => {
    let currentSection = null;
    sections.forEach((section) => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      if (window.pageYOffset >= sectionTop - sectionHeight / 3) {
        currentSection = section.id;
      }
    });

    navLinks.forEach((link) => {
      link.classList.remove("btn-primary");
      if (link.getAttribute("href") === `#${currentSection}`) {
        link.classList.add("btn-primary");
      }
    });
  };

  window.addEventListener("scroll", handleScroll);
  handleScroll();
});
