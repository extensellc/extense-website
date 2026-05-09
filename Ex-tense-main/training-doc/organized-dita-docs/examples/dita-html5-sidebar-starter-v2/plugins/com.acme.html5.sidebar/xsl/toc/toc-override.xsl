<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="3.0">
  <!-- Optional TOC override. If your OT minor version uses a different path, update this import. -->
  <xsl:import href="plugin:org.dita.html5:xsl/toc.xsl"/>

  <xsl:template match="nav">
    <nav class="sidebar-toc">
      <xsl:apply-templates select="@* | node()"/>
    </nav>
  </xsl:template>

  <xsl:template match="li">
    <li data-level="{count(ancestor::li)+1}">
      <xsl:apply-templates select="@* | node()"/>
    </li>
  </xsl:template>
</xsl:stylesheet>
