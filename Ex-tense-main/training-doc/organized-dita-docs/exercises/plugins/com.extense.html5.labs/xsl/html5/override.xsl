<?xml version="1.0" encoding="UTF-8"?>
<!--
  HTML5 Topic Override Stylesheet — XSLT Lab Exercises
  
  This file is the main XSLT override for Labs 1-3.
  Each lab adds templates progressively. Start with Lab 1 and uncomment
  successive sections as you complete each lab.
  
  Import chain: this stylesheet imports the default HTML5 transform,
  so any template you define here takes precedence via XSLT import rules.
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="3.0">

  <!-- Import the default HTML5 transform (always keep this first) -->
  <xsl:import href="plugin:org.dita.html5:xsl/dita2html5.xsl"/>


  <!-- ================================================================== -->
  <!-- LAB 1: Callout note styling                                         -->
  <!-- Goal: Style <note> elements as colored callout boxes with icons     -->
  <!--                                                                     -->
  <!-- Uncomment the template below and build to see callout boxes.        -->
  <!-- Pair with brand.css .callout styles for visual effect.              -->
  <!-- ================================================================== -->

  <!--
  <xsl:template match="*[contains(@class,' topic/note ')]">
    <div class="callout callout-{@type}" data-dita-class="{normalize-space(@class)}">
      <xsl:apply-templates/>
    </div>
  </xsl:template>
  -->


  <!-- ================================================================== -->
  <!-- LAB 2: Step anchors with URL hash highlighting                      -->
  <!-- Goal: Add id anchors to task steps for deep linking                 -->
  <!--                                                                     -->
  <!-- Uncomment after completing Lab 1.                                   -->
  <!-- Pair with js/step-highlight.js for scroll+highlight behavior.       -->
  <!-- ================================================================== -->

  <!--
  <xsl:template match="*[contains(@class,' task/step ')]">
    <li class="task-step" id="step-{position()}" data-step="{position()}">
      <xsl:apply-templates/>
    </li>
  </xsl:template>
  -->


  <!-- ================================================================== -->
  <!-- LAB 3: Custom meta tag injection                                    -->
  <!-- Goal: Add custom <meta> tags to every page's <head>                 -->
  <!--                                                                     -->
  <!-- Uncomment after completing Lab 2.                                   -->
  <!-- Override the empty gen-user-head named template — DITA-OT calls    -->
  <!-- this from within chapterHead specifically for user customizations.  -->
  <!-- No xsl:next-match needed — just add your meta tags directly.        -->
  <!-- ================================================================== -->

  <!--
  <xsl:template name="gen-user-head">
    <meta name="generator" content="DITA-OT + com.extense.html5.labs"/>
    <meta name="dita-class" content="{normalize-space(/*/@class)}"/>
  </xsl:template>
  -->

</xsl:stylesheet>
