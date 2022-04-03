// ==UserScript==
// @name         china_place combo
// @namespace    http://tampermonkey.net/
// @version      0.3
// @description  Userscript for r/china_place
// @author       china-place
// @updateURL    https://github.com/china-place/china-place-template/raw/main/userscript.user.js
// @downloadURL  https://github.com/china-place/china-place-template/raw/main/userscript.user.js
// @match        https://hot-potato.reddit.com/embed*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=reddit.com
// @grant        none
// ==/UserScript==
if (window.top !== window.self) {
  window.addEventListener(
    'load',
    () => {
      document
        .getElementsByTagName('mona-lisa-embed')[0]
        .shadowRoot.children[0].getElementsByTagName('mona-lisa-canvas')[0]
        .shadowRoot.children[0].appendChild(
          (() => {
            const i = document.createElement('img');
            i.src =
              'https://raw.githubusercontent.com/china-place/china-place-template/main/output.png';
            i.style =
              'position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 2000px;height: 1000px;';
            return i;
          })()
        );
    },
    false
  );
}
