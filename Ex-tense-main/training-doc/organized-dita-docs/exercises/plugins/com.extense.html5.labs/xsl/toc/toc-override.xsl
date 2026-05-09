<?xml version="1.0" encoding="UTF-8"?>
<!--
  TOC Override Stylesheet — Lab 4: Collapsible sidebar TOC
  
  This file overrides the default HTML5 navigation/TOC generation.
  Uncomment the templates below after completing Labs 1-3.
  
  Pair with:
    - brand.css  (.sidebar-toc styles)
    - A toggle button in JS for mobile collapse
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="3.0">

  <!-- Import the default HTML5 TOC transform -->
  <xsl:import href="plugin:org.dita.html5:xsl/nav.xsl"/>


  <!-- ================================================================== -->
  <!-- LAB 4: Collapsible sidebar TOC                                      -->
  <!-- Goal: Wrap TOC in a sidebar nav with level indicators               -->
  <!--                                                                     -->
  <!-- Uncomment after completing Labs 1-3.                                -->
  <!-- ================================================================== -->

  <!--
  <xsl:template match="nav">
    <nav class="sidebar-toc" aria-label="Table of Contents">
      <button class="sidebar-toc__toggle" type="button" aria-expanded="true">
        ☰ Contents
      </button>
      <div class="sidebar-toc__body">
        <xsl:apply-templates select="@* | node()"/>
      </div>
    </nav>
  </xsl:template>

  <xsl:template match="li">
    <li data-level="{count(ancestor::li)+1}">
      <xsl:apply-templates select="@* | node()"/>
    </li>
  </xsl:template>
  -->

</xsl:stylesheet>
