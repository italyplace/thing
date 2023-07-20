// ==UserScript==
// @name         Ritaly template
// @namespace    http://tampermonkey.net/
// @version      0.5
// @description  try to take over the canvas!
// @author       oralekin
// @match        https://garlic-bread.reddit.com/embed*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=reddit.com
// @grant        none
// ==/UserScript==
if (window.top !== window.self) {
    window.addEventListener('load', () => {
        debugger
            document.getElementsByTagName("garlic-bread-embed")[0].shadowRoot.children[0].getElementsByTagName("garlic-bread-canvas")[0].shadowRoot.children[0].appendChild(
        (function () {
            if (!Date.now) {
                Date.now = function() { return new Date().getTime(); }
            }
            const i = document.createElement("img");
            i.src = "https://github.com/italyplace/thing/raw/main/template.png?" + Date.now();
            i.style = "position: absolute;left: 0;top: 0px;image-rendering: pixelated;width: 1000px;height: 1000px;";
            i.id = "mcss-overlay"
            i.setAttribute("vis",1)
            console.log(i);
            return i;
        })())

            document.getElementsByTagName("body")[0].appendChild(
        (function () {
            const i = document.createElement("button");
            i.style = "position: fixed;left: 10px; background: #fff; top: 50%;width: 50px;height: 50px;";
            i.innerHTML = "T"
            i.onclick = function() {
                const img = document.getElementsByTagName("mona-lisa-embed")[0].shadowRoot.children[0].getElementsByTagName("mona-lisa-canvas")[0].shadowRoot.querySelector("#mcss-overlay")
                if (img.getAttribute("vis") == "1") {
                    img.setAttribute("vis",0)
                    img.style.opacity  = 0
                } else {

                    img.setAttribute("vis",1)
                    img.style.opacity  = 1
                }
            }
            console.log(i);
            return i;
        })())

    }, false);

}

