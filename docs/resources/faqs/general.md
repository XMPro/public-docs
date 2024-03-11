# General

Find answers to some of the most frequently asked general questions.

## Training

### Is there a training outline?

An end-to-end course can be found at [XMPro Courses](https://courses.xmpro.com/course-library/). It is broken down into 17 lessons - totaling 7 hours - covering an overview, Data Stream Designer, Recommendations, and App Designer.&#x20;

You can also find an extensive array of YouTube videos on various topics of interest on our YouTube channel [XMPro learning](https://www.youtube.com/channel/UCSnVNXaDqVizaoZHPjKhwRA).

### Are there any prerequisites for the training?

As XMPro is a no-code platform, there are no technical prerequisites.&#x20;

We do recommend the following to make your training more effective:

* Start with a Use Case/problem statement in mind
* Have access to an XMPro instance so you can practice and work out issues

## Session Timeout

### How does the XMPro sign-in process work?

When trying to sign in to XMPro Data Stream Designer or App Designer, you'll be redirected to the linked XMPro Subscription Manager's sign-in page. Here, enter your username and password to log in.

Upon signing in, you'll receive credentials as browser cookies for both Subscription Manager and the site you wish to access. Subscription Manager then redirects you back to the requested site, granting you an access token using those cookie credentials.

The access token is valid for the duration specified in the site's Session Timeout setting, while cookies last for longer periods (e.g., an hour). Cookies enable access to the website's pages and assets like _JavaScript_ and _images_, while the access token allows you to access the site's data, which is essential for navigating and saving changes.

### How long do I stay signed in?

When using XMPro App Designer, Data Stream Designer, or Subscription Manager and the access token nears its expiry time, the site will attempt a silent refresh of the credentials.&#x20;

If successful, a new token is granted, valid for the duration specified in the Session Timeout setting.&#x20;

If the refresh attempt is unsuccessful, the site will display a login expired warning with a prompt to sign in again. Clicking the button redirects you to Subscription Manager for credentials.&#x20;

If the Subscription Manager cookie is still valid, it will automatically issue a new access token and redirect back to the original site; otherwise, you'll be prompted to sign in again.&#x20;

Successful attempts through either path will refresh the cookie credentials if they're nearing expiry and meet refresh conditions. Refreshing the page will also update the credentials.
