/*
    This code hides expired notices in the homepage.
*/

let now = Math.floor(new Date().getTime() / 1000);

/* Check for if with style queries support */
if (CSS.supports("at-rule(@container)")) {
    /* CSS rule injected before the articles (no flashing content) */
    let sheet = new CSSStyleSheet();
    sheet.replaceSync(`
        #notices {
            --now: ${now};

            .article-wrapper {
                container-name: notice;
            }
        }

        /* Hide expired notices */
        @container notice style(--now > --expiry) {
            article {
                display: none;
            }
        }

        /* Hide future notices */
        @container notice style(--now < --date) {
            article {
                display: none;
            }
        }
    `);
    document.adoptedStyleSheets.push(sheet);
} else {
    /* Javascript fallback (flashes briefly if notice is set to disappear) */
    window.addEventListener('DOMContentLoaded', function() {
        document.querySelectorAll("#notices .article-wrapper").forEach(item => {
            /* Hide expired notices */
            let expiry = item.getAttribute("data-expirydate");
            if (expiry) {
                if (now > expiry) {
                    item.hidden = true;
                }
            }

            /* Hide future notices */
            let date = item.getAttribute("data-fromdate");
            if (date) {
                if (now < date) {
                    item.hidden = true;
                }
            }
        });
    });
}
