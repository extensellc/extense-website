
<?xml version="1.0" encoding="UTF-8"?>
<!--
  Extense LLC — Branded TOC / Navigation Override
  Renders sidebar TOC with collapsible topichead groups as top-level sections.
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                version="3.0"
                exclude-result-prefixes="xs">

  <!-- Wrap TOC in sidebar nav -->
  <xsl:template match="nav">
    <nav class="toc sidebar-toc" role="navigation" aria-label="Table of Contents">
      <xsl:apply-templates select="@* | node()"/>
    </nav>
  </xsl:template>

  <!-- Render each li with data-level for depth-aware styling -->
  <xsl:template match="li">
    <li data-level="{count(ancestor::li)+1}">
      <xsl:choose>
        <!-- If first child is topichead, render as collapsible heading -->
        <xsl:when test="*[contains(@class,' map/topichead ')]">
          <span>
            <xsl:apply-templates select="*[contains(@class,' map/topichead ')]/*[contains(@class,' topic/title ')]"/>
          </span>
          <xsl:apply-templates select="*[not(contains(@class,' map/topichead '))]"/>
        </xsl:when>
        <!-- Otherwise, render normally -->
        <xsl:otherwise>
          <xsl:apply-templates select="@* | node()"/>
        </xsl:otherwise>
      </xsl:choose>
    </li>
  </xsl:template>

  <!-- Render topichead title as plain text -->
  <xsl:template match="*[contains(@class,' map/topichead ')]/*[contains(@class,' topic/title ')]">
    <xsl:value-of select="."/>
  </xsl:template>

</xsl:stylesheet>
