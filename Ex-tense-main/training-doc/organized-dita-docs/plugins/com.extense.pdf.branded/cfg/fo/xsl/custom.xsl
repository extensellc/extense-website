<?xml version="1.0" encoding="UTF-8"?>
<!--
  Extense LLC — Branded PDF XSL Overrides
  
  Overrides PDF2 templates for:
  • Branded cover page with navy background, gold/green accents
  • Custom headers: "Extense LLC | <heading> | <page>"
  • Custom footers: "DITA Documentation & Training Guide | <page>"
  • Back cover with company info
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:fo="http://www.w3.org/1999/XSL/Format"
                xmlns:opentopic="http://www.idiominc.com/opentopic"
                exclude-result-prefixes="opentopic"
                version="3.0">

  <xsl:variable name="map" select="//opentopic:map"/>

  <!-- ═══════════════════════════════════════════════════════════════
       COVER PAGE — Navy background, gold title, green accents
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:template name="createFrontCoverContents">

    <!-- Navy background block covering full page -->
    <fo:block-container absolute-position="fixed"
                        top="0mm" left="0mm" right="0mm" bottom="0mm"
                        background-color="#1D397C">
      <fo:block>&#xA0;</fo:block>
    </fo:block-container>

    <!-- Decorative gold accent bar at top -->
    <fo:block-container absolute-position="fixed"
                        top="0mm" left="0mm" right="0mm" height="6mm"
                        background-color="#E9AC15">
      <fo:block>&#xA0;</fo:block>
    </fo:block-container>

    <!-- Green accent stripe -->
    <fo:block-container absolute-position="fixed"
                        top="6mm" left="0mm" right="0mm" height="2mm"
                        background-color="#0ACB8B">
      <fo:block>&#xA0;</fo:block>
    </fo:block-container>

    <!-- Company name at top -->
    <fo:block space-before="30mm"
              font-family="Helvetica, Arial, sans-serif"
              font-size="14pt"
              font-weight="bold"
              color="#0ACB8B"
              text-align="center"
              letter-spacing="3pt">
      EXTENSE LLC
    </fo:block>

    <!-- Main Title -->
    <fo:block space-before="35mm"
              font-family="Helvetica, Arial, sans-serif"
              font-size="32pt"
              font-weight="bold"
              color="#E9AC15"
              text-align="center"
              line-height="140%">
      <xsl:choose>
        <xsl:when test="$map//*[contains(@class,' bookmap/mainbooktitle ')][1]">
          <xsl:apply-templates select="$map//*[contains(@class,' bookmap/mainbooktitle ')][1]"/>
        </xsl:when>
        <xsl:when test="$map/*[contains(@class,' topic/title ')][1]">
          <xsl:apply-templates select="$map/*[contains(@class,' topic/title ')][1]"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="//*[contains(@class, ' map/map ')]/@title"/>
        </xsl:otherwise>
      </xsl:choose>
    </fo:block>

    <!-- Subtitle -->
    <xsl:if test="$map//*[contains(@class,' bookmap/booktitlealt ')][1]">
      <fo:block space-before="10mm"
                font-family="Helvetica, Arial, sans-serif"
                font-size="16pt"
                font-weight="normal"
                color="#FFFFFF"
                text-align="center"
                line-height="140%">
        <xsl:apply-templates select="$map//*[contains(@class,' bookmap/booktitlealt ')][1]"/>
      </fo:block>
    </xsl:if>

    <!-- Gold divider line -->
    <fo:block space-before="15mm" text-align="center">
      <fo:leader leader-length="100mm"
                 leader-pattern="rule"
                 rule-thickness="1.5pt"
                 color="#E9AC15"/>
    </fo:block>

    <!-- Version / Edition info -->
    <fo:block space-before="10mm"
              font-family="Helvetica, Arial, sans-serif"
              font-size="12pt"
              color="#CCCCCC"
              text-align="center">
      Comprehensive Training Guide
    </fo:block>

    <!-- Bottom section with metadata -->
    <fo:block-container absolute-position="fixed"
                        bottom="30mm" left="20mm" right="20mm" height="40mm">
      <!-- Green line above metadata -->
      <fo:block text-align="center" space-after="8pt">
        <fo:leader leader-length="60mm"
                   leader-pattern="rule"
                   rule-thickness="1pt"
                   color="#0ACB8B"/>
      </fo:block>

      <!-- Organization -->
      <fo:block font-family="Helvetica, Arial, sans-serif"
                font-size="11pt"
                color="#FFFFFF"
                text-align="center"
                space-after="4pt">
        <xsl:choose>
          <xsl:when test="$map//*[contains(@class,' bookmap/organization ')][1]">
            <xsl:apply-templates select="$map//*[contains(@class,' bookmap/organization ')][1]"/>
          </xsl:when>
          <xsl:otherwise>Extense LLC</xsl:otherwise>
        </xsl:choose>
      </fo:block>

      <!-- Copyright year -->
      <fo:block font-family="Helvetica, Arial, sans-serif"
                font-size="10pt"
                color="#999999"
                text-align="center">
        <xsl:text>&#xA9; </xsl:text>
        <xsl:choose>
          <xsl:when test="$map//*[contains(@class,' topic/copyryear ')]/@year">
            <xsl:value-of select="$map//*[contains(@class,' topic/copyryear ')]/@year"/>
          </xsl:when>
          <xsl:when test="$map//*[contains(@class,' bookmap/copyrfirst ')]">
            <xsl:value-of select="$map//*[contains(@class,' bookmap/copyrfirst ')]"/>
          </xsl:when>
          <xsl:otherwise>2026</xsl:otherwise>
        </xsl:choose>
        <xsl:text> Extense LLC. All rights reserved.</xsl:text>
      </fo:block>
    </fo:block-container>

    <!-- Bottom gold bar -->
    <fo:block-container absolute-position="fixed"
                        bottom="0mm" left="0mm" right="0mm" height="4mm"
                        background-color="#E9AC15">
      <fo:block>&#xA0;</fo:block>
    </fo:block-container>
  </xsl:template>

  <!-- ═══════════════════════════════════════════════════════════════
       BACK COVER
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:template name="createBackCoverContents">
    <!-- Navy background -->
    <fo:block-container absolute-position="fixed"
                        top="0mm" left="0mm" right="0mm" bottom="0mm"
                        background-color="#1D397C">
      <fo:block>&#xA0;</fo:block>
    </fo:block-container>

    <!-- Center content -->
    <fo:block space-before="100mm"
              font-family="Helvetica, Arial, sans-serif"
              font-size="18pt"
              font-weight="bold"
              color="#E9AC15"
              text-align="center"
              letter-spacing="2pt">
      EXTENSE LLC
    </fo:block>

    <fo:block space-before="8mm"
              font-family="Helvetica, Arial, sans-serif"
              font-size="11pt"
              color="#CCCCCC"
              text-align="center">
      Technology Consulting &amp; Training Solutions
    </fo:block>

    <fo:block space-before="6mm" text-align="center">
      <fo:leader leader-length="50mm"
                 leader-pattern="rule"
                 rule-thickness="1pt"
                 color="#0ACB8B"/>
    </fo:block>

    <fo:block space-before="6mm"
              font-family="Helvetica, Arial, sans-serif"
              font-size="10pt"
              color="#999999"
              text-align="center">
      www.extense.com
    </fo:block>

    <!-- Bottom gold bar -->
    <fo:block-container absolute-position="fixed"
                        bottom="0mm" left="0mm" right="0mm" height="4mm"
                        background-color="#E9AC15">
      <fo:block>&#xA0;</fo:block>
    </fo:block-container>
  </xsl:template>

  <!-- ═══════════════════════════════════════════════════════════════
       BODY HEADERS — Extense LLC | <heading> | page#
       Override to inject company name directly instead of using
       the prodname variable (which may be empty).
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:template name="insertBodyOddHeader">
    <fo:static-content flow-name="odd-body-header">
      <fo:block xsl:use-attribute-sets="__body__odd__header">
        <fo:inline font-weight="bold" color="#1D397C">Extense LLC</fo:inline>
        <xsl:text> &#xA0;|&#xA0; </xsl:text>
        <fo:inline xsl:use-attribute-sets="__body__odd__header__heading">
          <fo:retrieve-marker retrieve-class-name="current-header"/>
        </fo:inline>
        <fo:leader leader-pattern="space"/>
        <fo:inline xsl:use-attribute-sets="__body__odd__header__pagenum">
          <fo:page-number/>
        </fo:inline>
      </fo:block>
    </fo:static-content>
  </xsl:template>

  <xsl:template name="insertBodyEvenHeader">
    <fo:static-content flow-name="even-body-header">
      <fo:block xsl:use-attribute-sets="__body__even__header">
        <fo:inline xsl:use-attribute-sets="__body__even__header__pagenum">
          <fo:page-number/>
        </fo:inline>
        <fo:leader leader-pattern="space"/>
        <fo:inline xsl:use-attribute-sets="__body__even__header__heading">
          <fo:retrieve-marker retrieve-class-name="current-header"/>
        </fo:inline>
        <xsl:text> &#xA0;|&#xA0; </xsl:text>
        <fo:inline font-weight="bold" color="#1D397C">Extense LLC</fo:inline>
      </fo:block>
    </fo:static-content>
  </xsl:template>

  <xsl:template name="insertBodyFirstHeader">
    <fo:static-content flow-name="first-body-header">
      <fo:block xsl:use-attribute-sets="__body__first__header">
        <!-- Intentionally empty on first page of each chapter -->
      </fo:block>
    </fo:static-content>
  </xsl:template>

  <!-- ═══════════════════════════════════════════════════════════════
       BODY FOOTERS — "DITA Training Guide" left, page# right
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:template name="insertBodyOddFooter">
    <fo:static-content flow-name="odd-body-footer">
      <fo:block xsl:use-attribute-sets="__body__odd__footer">
        <fo:inline color="#999999" font-size="7pt">DITA Guide</fo:inline>
        <fo:leader leader-pattern="space"/>
        <fo:inline xsl:use-attribute-sets="__body__odd__footer__pagenum">
          <fo:page-number/>
        </fo:inline>
      </fo:block>
    </fo:static-content>
  </xsl:template>

  <xsl:template name="insertBodyEvenFooter">
    <fo:static-content flow-name="even-body-footer">
      <fo:block xsl:use-attribute-sets="__body__even__footer">
        <fo:inline xsl:use-attribute-sets="__body__even__footer__pagenum">
          <fo:page-number/>
        </fo:inline>
        <fo:leader leader-pattern="space"/>
        <fo:inline color="#999999" font-size="7pt">DITA Guide</fo:inline>
      </fo:block>
    </fo:static-content>
  </xsl:template>

  <xsl:template name="insertBodyFirstFooter">
    <fo:static-content flow-name="first-body-footer">
      <fo:block xsl:use-attribute-sets="__body__first__footer">
        <fo:inline color="#999999" font-size="7pt">DITA Guide</fo:inline>
        <fo:leader leader-pattern="space"/>
        <fo:inline xsl:use-attribute-sets="__body__first__footer__pagenum">
          <fo:page-number/>
        </fo:inline>
      </fo:block>
    </fo:static-content>
  </xsl:template>

  <!-- ═══════════════════════════════════════════════════════════════
       TOC HEADERS & FOOTERS
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:template name="insertTocOddHeader">
    <fo:static-content flow-name="odd-toc-header">
      <fo:block xsl:use-attribute-sets="__toc__odd__header">
        <fo:inline font-weight="bold" color="#1D397C">Extense LLC</fo:inline>
        <xsl:text> &#xA0;|&#xA0; </xsl:text>
        <fo:inline>Contents</fo:inline>
        <fo:leader leader-pattern="space"/>
        <fo:inline xsl:use-attribute-sets="__toc__odd__header__pagenum">
          <fo:page-number/>
        </fo:inline>
      </fo:block>
    </fo:static-content>
  </xsl:template>

  <xsl:template name="insertTocEvenHeader">
    <fo:static-content flow-name="even-toc-header">
      <fo:block xsl:use-attribute-sets="__toc__even__header">
        <fo:inline xsl:use-attribute-sets="__toc__even__header__pagenum">
          <fo:page-number/>
        </fo:inline>
        <fo:leader leader-pattern="space"/>
        <fo:inline>Contents</fo:inline>
        <xsl:text> &#xA0;|&#xA0; </xsl:text>
        <fo:inline font-weight="bold" color="#1D397C">Extense LLC</fo:inline>
      </fo:block>
    </fo:static-content>
  </xsl:template>

  <xsl:template name="insertTocOddFooter">
    <fo:static-content flow-name="odd-toc-footer">
      <fo:block xsl:use-attribute-sets="__toc__odd__footer">
        <fo:inline color="#999999" font-size="7pt">DITA Guide</fo:inline>
        <fo:leader leader-pattern="space"/>
        <fo:inline xsl:use-attribute-sets="__toc__odd__footer__pagenum">
          <fo:page-number/>
        </fo:inline>
      </fo:block>
    </fo:static-content>
  </xsl:template>

  <xsl:template name="insertTocEvenFooter">
    <fo:static-content flow-name="even-toc-footer">
      <fo:block xsl:use-attribute-sets="__toc__even__footer">
        <fo:inline xsl:use-attribute-sets="__toc__even__footer__pagenum">
          <fo:page-number/>
        </fo:inline>
        <fo:leader leader-pattern="space"/>
        <fo:inline color="#999999" font-size="7pt">DITA Guide</fo:inline>
      </fo:block>
    </fo:static-content>
  </xsl:template>

  <!-- Enable back cover generation -->
  <xsl:variable name="generate-back-cover" select="true()"/>

  <!-- ═══════════════════════════════════════════════════════════════
       NOTE TYPE DIFFERENTIATION
       Color-coded borders and backgrounds for tip, warning, caution,
       danger, important, and default note types.
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:template match="*[contains(@class, ' topic/note ')]" priority="1">
    <xsl:variable name="note-type" select="if (@type) then @type else 'note'"/>
    <xsl:variable name="border-color">
      <xsl:choose>
        <xsl:when test="$note-type = 'tip'">#0ACB8B</xsl:when>
        <xsl:when test="$note-type = ('warning', 'caution', 'attention')">#E67E22</xsl:when>
        <xsl:when test="$note-type = 'danger'">#C0392B</xsl:when>
        <xsl:when test="$note-type = ('important', 'remember')">#E9AC15</xsl:when>
        <xsl:otherwise>#1D397C</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="bg-color">
      <xsl:choose>
        <xsl:when test="$note-type = 'tip'">#EDFAF5</xsl:when>
        <xsl:when test="$note-type = ('warning', 'caution', 'attention')">#FEF5EC</xsl:when>
        <xsl:when test="$note-type = 'danger'">#FDEDED</xsl:when>
        <xsl:when test="$note-type = ('important', 'remember')">#FDF8ED</xsl:when>
        <xsl:otherwise>#EBF0FA</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="label-text">
      <xsl:choose>
        <xsl:when test="$note-type = 'tip'">Tip</xsl:when>
        <xsl:when test="$note-type = 'warning'">Warning</xsl:when>
        <xsl:when test="$note-type = 'caution'">Caution</xsl:when>
        <xsl:when test="$note-type = 'attention'">Attention</xsl:when>
        <xsl:when test="$note-type = 'danger'">DANGER</xsl:when>
        <xsl:when test="$note-type = 'important'">Important</xsl:when>
        <xsl:when test="$note-type = 'remember'">Remember</xsl:when>
        <xsl:when test="$note-type = 'notice'">Notice</xsl:when>
        <xsl:when test="$note-type = 'restriction'">Restriction</xsl:when>
        <xsl:when test="$note-type = 'trouble'">Troubleshooting</xsl:when>
        <xsl:otherwise>Note</xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <fo:block xsl:use-attribute-sets="note">
      <xsl:attribute name="border-start-color" select="$border-color"/>
      <xsl:attribute name="background-color" select="$bg-color"/>
      <fo:block font-weight="bold" font-size="9pt" space-after="3pt">
        <xsl:attribute name="color" select="$border-color"/>
        <xsl:value-of select="$label-text"/>
      </fo:block>
      <fo:block>
        <xsl:apply-templates/>
      </fo:block>
    </fo:block>
  </xsl:template>

  <!-- ═══════════════════════════════════════════════════════════════
       YELLOW HIGHLIGHT — for before/after comparison callouts
       Matches <ph outputclass="hi-yellow"> in codeblocks and body text
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:template match="*[contains(@class,' topic/ph ')][@outputclass='hi-yellow']">
    <fo:inline background-color="#FFFACD" padding-start="1pt" padding-end="1pt">
      <xsl:apply-templates/>
    </fo:inline>
  </xsl:template>

</xsl:stylesheet>
