---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<style>
  .cv-page {
    max-width: 980px;
    margin: 0 auto;
  }

  .cv-page .cv-download-links {
    margin-bottom: 1rem;
  }

  .cv-page .cv-viewer {
    border: 1px solid var(--global-border-color);
    border-radius: 0.6rem;
    overflow: hidden;
    background: var(--global-bg-color);
  }

  .cv-page .cv-viewer iframe {
    display: block;
    width: 100%;
    height: 78vh;
    min-height: 760px;
    border: 0;
  }

  @media (max-width: 768px) {
    .cv-page .cv-viewer iframe {
      height: 72vh;
      min-height: 560px;
    }
  }
</style>

<div class="cv-page">
  <div class="cv-download-links">
    <a href="{{ base_path }}/files/cv.pdf" class="btn btn--primary">Download CV as PDF</a>
  </div>

  <div class="cv-viewer">
    <iframe src="{{ base_path }}/files/cv.pdf#view=FitH">
      This browser does not support PDFs. Please download the CV using the button above.
    </iframe>
  </div>
</div>
