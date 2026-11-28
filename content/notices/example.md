+++
title = 'Example notice'
date = 2026-01-01T00:00:00-00:00
expiryDate = 2026-01-01T00:00:00-00:00
[Params]
    showTitle = false
    showDate = false
    showDateFormat = "02/01/2006"
    hideBeforeDate = true
+++

This is an example notice to use as a template.

<!--

Notices appear at the top of the homepage.

Note that:
- notices won't get rendered as actual pages (the notices sections has render = never)
- they will only appear on the homepage if the expiryDate is in the past at the time of rendering
- they get rendered inline so only simple content will show as intended. Keep it brief!

You can also add links inside notices, for example:
[Test link](/news/sloppapocalypse/)

-->