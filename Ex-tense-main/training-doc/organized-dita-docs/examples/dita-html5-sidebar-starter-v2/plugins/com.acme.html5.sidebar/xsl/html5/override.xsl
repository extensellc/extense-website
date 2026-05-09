<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                version="3.0"
                exclude-result-prefixes="xs">

  <!-- Import default HTML5 transform -->
  <xsl:import href="plugin:org.dita.html5:xsl/dita2html5.xsl"/>

  <!-- Inject site JS into <head> -->
  <xsl:template name="gen-user-head">
    <xsl:next-match/>
    <script src="{concat($PATH2PROJ, 'js/site.js')}"></script>
  </xsl:template>

  <!-- Standardize topic wrapper across all topic types -->
  <xsl:template match="*[contains(@class,' topic/topic ')]">
    <article class="dita-topic" data-topic-type="{local-name()}">
      <xsl:apply-templates select="*[contains(@class,' topic/title ')]"/>
      <xsl:apply-templates select="*[contains(@class,' topic/shortdesc ')]"/>
      <main class="dita-body">
        <xsl:apply-templates
          select="*[contains(@class,' topic/body ')]
                | *[contains(@class,' concept/conbody ')]
                | *[contains(@class,' task/taskbody ')]
                | *[contains(@class,' reference/refbody ')]"/>
      </main>
      <xsl:apply-templates select="*[contains(@class,' topic/related-links ')]"/>
    </article>
  </xsl:template>

  <!-- Title -->
  <xsl:template match="*[contains(@class,' topic/title ')]">
    <header class="topic-header">
      <h1 class="topic-title"><xsl:apply-templates/></h1>
    </header>
  </xsl:template>

  <!-- Shortdesc -->
  <xsl:template match="*[contains(@class,' topic/shortdesc ')]">
    <p class="topic-lead"><xsl:apply-templates/></p>
  </xsl:template>

  <!-- Paragraph hooks -->
  <xsl:template match="*[contains(@class,' topic/p ')]">
    <p class="dita-p" data-dita-class="{normalize-space(@class)}">
      <xsl:apply-templates/>
    </p>
  </xsl:template>

  <!-- Notes as callouts -->
  <xsl:template match="*[contains(@class,' topic/note ')]">
    <aside class="callout{if (@type) then concat(' callout-', @type) else ''}">
      <xsl:if test="@type">
        <div class="callout-title"><xsl:value-of select="upper-case(@type)"/></div>
      </xsl:if>
      <div class="callout-body"><xsl:apply-templates/></div>
    </aside>
  </xsl:template>

  <!-- Responsive wrappers for tables -->
  <xsl:template match="*[contains(@class,' topic/table ')]">
    <div class="table-wrap"><xsl:next-match/></div>
  </xsl:template>

  <xsl:template match="*[contains(@class,' topic/simpletable ')]">
    <div class="simpletable-wrap"><xsl:next-match/></div>
  </xsl:template>

  <!-- Code blocks with Copy button -->
  <xsl:template match="*[contains(@class,' topic/codeblock ')]">
    <div class="codeblock">
      <button class="copy-btn" type="button">Copy</button>
      <pre><code><xsl:apply-templates/></code></pre>
    </div>
  </xsl:template>

  <!-- Task steps anchors + data-step -->
  <xsl:template match="*[contains(@class,' task/steps ')]">
    <ol class="steps"><xsl:apply-templates/></ol>
  </xsl:template>

  <xsl:template match="*[contains(@class,' task/step ')]">
    <li class="task-step"
        data-step="{count(preceding-sibling::*[contains(@class,' task/step ')]) + 1}">
      <xsl:if test="@id">
        <xsl:attribute name="id" select="@id"/>
      </xsl:if>
      <xsl:apply-templates/>
    </li>
  </xsl:template>

  <xsl:template match="*[contains(@class,' task/cmd ')]">
    <div class="step-cmd"><xsl:apply-templates/></div>
  </xsl:template>

  <xsl:template match="*[contains(@class,' task/substeps ')]">
    <ol class="substeps"><xsl:apply-templates/></ol>
  </xsl:template>

  <!-- Add a class to nav so it can be styled as a sidebar (works for embedded nav-toc) -->
  <xsl:template match="nav">
    <nav class="sidebar-toc">
      <xsl:apply-templates select="@* | node()"/>
    </nav>
  </xsl:template>


  <!-- ============================================================
       Additional common-element overrides (production-style hooks)
       - phrasing content (ph)
       - xref/link (preserve default, add hooks)
       - figure/image
       - lists (li)
       - definition lists (dl/dlentry/dt/dd)
       - draft comments
       - hazard statements
       ============================================================ -->

  <!-- ph (generic phrasing content) -->
  <xsl:template match="*[contains(@class,' topic/ph ')]">
    <span class="dita-ph{if (@outputclass) then concat(' ', @outputclass) else ''}"
          data-dita-class="{normalize-space(@class)}">
      <xsl:apply-templates/>
    </span>
  </xsl:template>

  <!-- xref: preserve default rendering, then add consistent classes/data hooks
       This pattern captures the default output (usually an <a/>) and re-emits it with
       additional attributes. -->
  <xsl:template match="*[contains(@class,' topic/xref ')]">
    <xsl:variable name="out" as="node()*">
      <xsl:next-match/>
    </xsl:variable>

    <xsl:for-each select="$out">
      <xsl:choose>
        <xsl:when test="self::a">
          <xsl:variable name="isExternal"
                        select="starts-with(@href,'http') or @target='_blank'"/>
          <a>
            <!-- preserve existing attributes -->
            <xsl:copy-of select="@*"/>
            <!-- ensure rel/target for external -->
            <xsl:if test="$isExternal">
              <xsl:attribute name="target">_blank</xsl:attribute>
              <xsl:attribute name="rel">noopener noreferrer</xsl:attribute>
            </xsl:if>
            <!-- merge/append CSS class -->
            <xsl:attribute name="class"
              select="normalize-space(string-join((@class, 'dita-xref', if ($isExternal) then 'external' else ()), ' '))"/>
            <xsl:attribute name="data-dita-class"
              select="normalize-space(../@class)"/>
            <xsl:apply-templates select="node()"/>
          </a>
        </xsl:when>
        <xsl:otherwise>
          <xsl:sequence select="."/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:for-each>
  </xsl:template>

  <!-- fig + fig/title -->
  <xsl:template match="*[contains(@class,' topic/fig ')]">
    <figure class="dita-fig" data-dita-class="{normalize-space(@class)}">
      <xsl:apply-templates/>
    </figure>
  </xsl:template>

  <xsl:template match="*[contains(@class,' topic/fig/title ')]">
    <figcaption class="dita-figcaption"><xsl:apply-templates/></figcaption>
  </xsl:template>

  <!-- image -->
  <xsl:template match="*[contains(@class,' topic/image ')]">
    <img class="dita-image"
         data-dita-class="{normalize-space(@class)}"
         src="{@href}">
      <xsl:if test="@alt">
        <xsl:attribute name="alt" select="@alt"/>
      </xsl:if>
    </img>
  </xsl:template>

  <!-- list items -->
  <xsl:template match="*[contains(@class,' topic/li ')]">
    <li class="dita-li" data-dita-class="{normalize-space(@class)}">
      <xsl:apply-templates/>
    </li>
  </xsl:template>

  <!-- definition lists -->
  <xsl:template match="*[contains(@class,' topic/dl ')]">
    <dl class="dita-dl" data-dita-class="{normalize-space(@class)}">
      <xsl:apply-templates/>
    </dl>
  </xsl:template>

  <xsl:template match="*[contains(@class,' topic/dlentry ')]">
    <!-- HTML <dl> should contain dt/dd pairs; do not wrap dlentry in extra block elements -->
    <xsl:apply-templates/>
  </xsl:template>

  <xsl:template match="*[contains(@class,' topic/dt ')]">
    <dt class="dita-dt" data-dita-class="{normalize-space(@class)}"><xsl:apply-templates/></dt>
  </xsl:template>

  <xsl:template match="*[contains(@class,' topic/dd ')]">
    <dd class="dita-dd" data-dita-class="{normalize-space(@class)}"><xsl:apply-templates/></dd>
  </xsl:template>

  <!-- draft comments (often filtered out in production via DITAVAL) -->
  <xsl:template match="*[contains(@class,' topic/draft-comment ')]">
    <aside class="draft-comment" data-dita-class="{normalize-space(@class)}" aria-label="Draft comment">
      <div class="draft-comment-label">DRAFT</div>
      <div class="draft-comment-body"><xsl:apply-templates/></div>
    </aside>
  </xsl:template>

  <!-- hazard statements (safety content) -->
  <xsl:template match="*[contains(@class,' hazard-d/hazardstatement ')]">
    <section class="hazardstatement" data-dita-class="{normalize-space(@class)}" aria-label="Hazard statement">
      <xsl:apply-templates/>
    </section>
  </xsl:template>

  <xsl:template match="*[contains(@class,' hazard-d/hazardtype ')]">
    <div class="hazardtype"><xsl:apply-templates/></div>
  </xsl:template>

  <xsl:template match="*[contains(@class,' hazard-d/consequence ')]">
    <div class="hazard-consequence"><strong>Consequence:</strong> <xsl:apply-templates/></div>
  </xsl:template>

  <xsl:template match="*[contains(@class,' hazard-d/howtoavoid ')]">
    <div class="hazard-howtoavoid"><strong>How to avoid:</strong> <xsl:apply-templates/></div>
  </xsl:template>

</xsl:stylesheet>
