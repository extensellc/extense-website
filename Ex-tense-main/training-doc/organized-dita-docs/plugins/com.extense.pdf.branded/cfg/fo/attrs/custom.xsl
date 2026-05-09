<?xml version="1.0" encoding="UTF-8"?>
<!--
  Extense LLC — Branded PDF Attribute Overrides
  
  Overrides default PDF2 attribute-sets to apply:
  • Extense brand colours (navy #1D397C, gold #E9AC15, green #0ACB8B)
  • Sans-serif body font (Helvetica / sans-serif)
  • Branded cover page with navy background + gold title
  • Chapter/part headings in navy with gold rule
  • Headers and footers with company name + page numbers
  • Code block and table styling
  • Note/tip/warning callout colours
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:fo="http://www.w3.org/1999/XSL/Format"
                version="3.0">

  <!-- ═══════════════════════════════════════════════════════════════
       COLOUR VARIABLES (referenced via xsl:attribute below)
       ═══════════════════════════════════════════════════════════════ -->

  <!-- ═══════════════════════════════════════════════════════════════
       PAGE LAYOUT — US Letter, 25mm side margins, 20mm top/bottom
       
       Left/right margins go on simple-page-master so that ALL
       regions (header, body, footer) share the same side margins.
       Top/bottom margins on simple-page-master create the overall
       page inset; region-body top/bottom margins carve out space
       for headers and footers.
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:variable name="page-width">215.9mm</xsl:variable>
  <xsl:variable name="page-height">279.4mm</xsl:variable>
  <xsl:variable name="mirror-page-margins" select="false()"/>

  <!-- Override the page-margin variables to 0 — we handle everything
       via attribute-sets so that header/footer/body all align. -->
  <xsl:variable name="page-margins">0mm</xsl:variable>
  <xsl:variable name="page-margin-inside">0mm</xsl:variable>
  <xsl:variable name="page-margin-outside">0mm</xsl:variable>
  <xsl:variable name="page-margin-top">0mm</xsl:variable>
  <xsl:variable name="page-margin-bottom">0mm</xsl:variable>

  <!-- Remove default body content indent (25pt) — page-level margins
       on simple-page-master already handle all spacing. -->
  <xsl:variable name="side-col-width">0pt</xsl:variable>

  <!-- Page master: 25mm left/right, 18mm top/bottom.
       All three regions (before, body, after) inherit these side margins. -->
  <xsl:attribute-set name="simple-page-master">
    <xsl:attribute name="page-width" select="$page-width"/>
    <xsl:attribute name="page-height" select="$page-height"/>
    <xsl:attribute name="margin-left">25mm</xsl:attribute>
    <xsl:attribute name="margin-right">25mm</xsl:attribute>
    <xsl:attribute name="margin-top">18mm</xsl:attribute>
    <xsl:attribute name="margin-bottom">18mm</xsl:attribute>
  </xsl:attribute-set>

  <!-- Region-body: top/bottom margins create space between
       header/footer and the main text block. Left/right explicitly
       set to 0 so body aligns with header/footer (side margins
       are handled by simple-page-master for all regions). -->
  <xsl:attribute-set name="region-body.odd">
    <xsl:attribute name="margin-top">14mm</xsl:attribute>
    <xsl:attribute name="margin-bottom">12mm</xsl:attribute>
    <xsl:attribute name="margin-left">0mm</xsl:attribute>
    <xsl:attribute name="margin-right">0mm</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="region-body.even">
    <xsl:attribute name="margin-top">14mm</xsl:attribute>
    <xsl:attribute name="margin-bottom">12mm</xsl:attribute>
    <xsl:attribute name="margin-left">0mm</xsl:attribute>
    <xsl:attribute name="margin-right">0mm</xsl:attribute>
  </xsl:attribute-set>

  <!-- Header/footer region extents — must be ≤ region-body margins -->
  <xsl:attribute-set name="region-before">
    <xsl:attribute name="extent">12mm</xsl:attribute>
    <xsl:attribute name="display-align">after</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="region-after">
    <xsl:attribute name="extent">10mm</xsl:attribute>
    <xsl:attribute name="display-align">before</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       FRONT MATTER / COVER PAGE
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="__frontmatter">
    <xsl:attribute name="text-align">center</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__frontmatter__title" use-attribute-sets="common.title">
    <xsl:attribute name="space-before">60mm</xsl:attribute>
    <xsl:attribute name="space-before.conditionality">retain</xsl:attribute>
    <xsl:attribute name="font-size">28pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="line-height">140%</xsl:attribute>
    <xsl:attribute name="color">#E9AC15</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__frontmatter__subtitle" use-attribute-sets="common.title">
    <xsl:attribute name="font-size">16pt</xsl:attribute>
    <xsl:attribute name="font-weight">normal</xsl:attribute>
    <xsl:attribute name="line-height">140%</xsl:attribute>
    <xsl:attribute name="color">#FFFFFF</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
    <xsl:attribute name="space-before">8pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__frontmatter__owner" use-attribute-sets="common.title">
    <xsl:attribute name="space-before">36pt</xsl:attribute>
    <xsl:attribute name="font-size">14pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="line-height">normal</xsl:attribute>
    <xsl:attribute name="color">#0ACB8B</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__frontmatter__owner__container">
    <xsl:attribute name="position">absolute</xsl:attribute>
    <xsl:attribute name="top">200mm</xsl:attribute>
    <xsl:attribute name="bottom">20mm</xsl:attribute>
    <xsl:attribute name="right">20mm</xsl:attribute>
    <xsl:attribute name="left">20mm</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__frontmatter__owner__container_content">
    <xsl:attribute name="text-align">center</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       BODY TEXT
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="__fo__root">
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
    <xsl:attribute name="font-size">10pt</xsl:attribute>
    <xsl:attribute name="color">#2D2D2D</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       HEADINGS — Navy with gold bottom border effect
       ═══════════════════════════════════════════════════════════════ -->
  <!-- topic.title = <h1> equivalent -->
  <!-- H1 — Topic title (top-level within a chapter) -->
  <xsl:attribute-set name="topic.title" use-attribute-sets="common.title">
    <xsl:attribute name="border-bottom">3pt solid #E9AC15</xsl:attribute>
    <xsl:attribute name="space-before">18pt</xsl:attribute>
    <xsl:attribute name="space-before.conditionality">discard</xsl:attribute>
    <xsl:attribute name="space-after">12pt</xsl:attribute>
    <xsl:attribute name="font-size">18pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="padding-top">4pt</xsl:attribute>
    <xsl:attribute name="padding-bottom">6pt</xsl:attribute>
    <xsl:attribute name="margin-left">0pt</xsl:attribute>
    <xsl:attribute name="margin-right">0pt</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
    <xsl:attribute name="keep-with-next.within-column">always</xsl:attribute>
  </xsl:attribute-set>

  <!-- H2 -->
  <xsl:attribute-set name="topic.topic.title" use-attribute-sets="common.title">
    <xsl:attribute name="space-before">16pt</xsl:attribute>
    <xsl:attribute name="space-after">8pt</xsl:attribute>
    <xsl:attribute name="font-size">15pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="padding-top">2pt</xsl:attribute>
    <xsl:attribute name="padding-bottom">2pt</xsl:attribute>
    <xsl:attribute name="margin-left">0pt</xsl:attribute>
    <xsl:attribute name="margin-right">0pt</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
    <xsl:attribute name="keep-with-next.within-column">always</xsl:attribute>
  </xsl:attribute-set>

  <!-- H3 -->
  <xsl:attribute-set name="topic.topic.topic.title" use-attribute-sets="common.title">
    <xsl:attribute name="space-before">14pt</xsl:attribute>
    <xsl:attribute name="space-after">6pt</xsl:attribute>
    <xsl:attribute name="font-size">12pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="padding-top">2pt</xsl:attribute>
    <xsl:attribute name="padding-bottom">2pt</xsl:attribute>
    <xsl:attribute name="margin-left">0pt</xsl:attribute>
    <xsl:attribute name="margin-right">0pt</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
    <xsl:attribute name="keep-with-next.within-column">always</xsl:attribute>
  </xsl:attribute-set>

  <!-- H4 -->
  <xsl:attribute-set name="topic.topic.topic.topic.title" use-attribute-sets="common.title">
    <xsl:attribute name="space-before">12pt</xsl:attribute>
    <xsl:attribute name="space-after">5pt</xsl:attribute>
    <xsl:attribute name="font-size">12pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="font-style">normal</xsl:attribute>
    <xsl:attribute name="padding-top">2pt</xsl:attribute>
    <xsl:attribute name="padding-bottom">2pt</xsl:attribute>
    <xsl:attribute name="margin-left">0pt</xsl:attribute>
    <xsl:attribute name="margin-right">0pt</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
    <xsl:attribute name="keep-with-next.within-column">always</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       PART & CHAPTER TITLES
       ═══════════════════════════════════════════════════════════════ -->
  <!-- These attribute sets style the Part/Chapter title pages produced by bookmap -->
  <xsl:attribute-set name="__chapter__frontmatter__name__container">
    <xsl:attribute name="font-size">24pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
    <xsl:attribute name="padding-bottom">8pt</xsl:attribute>
    <xsl:attribute name="space-before">40pt</xsl:attribute>
    <xsl:attribute name="space-after">14pt</xsl:attribute>
    <xsl:attribute name="margin-left">0pt</xsl:attribute>
    <xsl:attribute name="margin-right">0pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__chapter__frontmatter__number__container">
    <xsl:attribute name="font-size">36pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="color">#E9AC15</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       BODY PARAGRAPHS — Consistent spacing
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="common.block">
    <xsl:attribute name="space-before">6pt</xsl:attribute>
    <xsl:attribute name="space-after">6pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="section.title" use-attribute-sets="common.title">
    <xsl:attribute name="space-before">14pt</xsl:attribute>
    <xsl:attribute name="space-after">6pt</xsl:attribute>
    <xsl:attribute name="font-size">13pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="padding-top">4pt</xsl:attribute>
    <xsl:attribute name="padding-bottom">2pt</xsl:attribute>
    <xsl:attribute name="margin-left">0pt</xsl:attribute>
    <xsl:attribute name="margin-right">0pt</xsl:attribute>
    <xsl:attribute name="border-bottom">1pt solid #D0D5DD</xsl:attribute>
    <xsl:attribute name="keep-with-next.within-column">always</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       TABLE OF CONTENTS
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="__toc__header" use-attribute-sets="common.title">
    <xsl:attribute name="space-before">0pt</xsl:attribute>
    <xsl:attribute name="space-after">16.8pt</xsl:attribute>
    <xsl:attribute name="font-size">20pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="padding-bottom">6pt</xsl:attribute>
    <xsl:attribute name="border-bottom">3pt solid #E9AC15</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__toc__topic__content">
    <xsl:attribute name="font-size">10pt</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__toc__chapter__content" use-attribute-sets="__toc__topic__content">
    <xsl:attribute name="font-size">12pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="padding-top">8pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__toc__part__content" use-attribute-sets="__toc__topic__content">
    <xsl:attribute name="font-size">14pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="padding-top">12pt</xsl:attribute>
    <xsl:attribute name="padding-bottom">4pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__toc__appendix__content" use-attribute-sets="__toc__chapter__content">
    <xsl:attribute name="font-style">normal</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       HEADERS & FOOTERS
       ═══════════════════════════════════════════════════════════════ -->
  <!-- Base header: navy bottom border -->
  <xsl:attribute-set name="odd__header">
    <xsl:attribute name="font-size">8pt</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="text-align-last">justify</xsl:attribute>
    <xsl:attribute name="border-bottom">0.5pt solid #E9AC15</xsl:attribute>
    <xsl:attribute name="padding-bottom">4pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="even__header">
    <xsl:attribute name="font-size">8pt</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="text-align-last">justify</xsl:attribute>
    <xsl:attribute name="border-bottom">0.5pt solid #E9AC15</xsl:attribute>
    <xsl:attribute name="padding-bottom">4pt</xsl:attribute>
  </xsl:attribute-set>

  <!-- Base footer: gold top border -->
  <xsl:attribute-set name="odd__footer">
    <xsl:attribute name="font-size">8pt</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
    <xsl:attribute name="color">#666666</xsl:attribute>
    <xsl:attribute name="text-align-last">justify</xsl:attribute>
    <xsl:attribute name="border-top">0.5pt solid #E9AC15</xsl:attribute>
    <xsl:attribute name="padding-top">4pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="even__footer">
    <xsl:attribute name="font-size">8pt</xsl:attribute>
    <xsl:attribute name="font-family">Helvetica, Arial, sans-serif</xsl:attribute>
    <xsl:attribute name="color">#666666</xsl:attribute>
    <xsl:attribute name="text-align-last">justify</xsl:attribute>
    <xsl:attribute name="border-top">0.5pt solid #E9AC15</xsl:attribute>
    <xsl:attribute name="padding-top">4pt</xsl:attribute>
  </xsl:attribute-set>

  <!-- Override base header/footer attribute-sets to remove
       end-indent="10pt" so edges align with body content. -->
  <xsl:attribute-set name="__body__odd__header" use-attribute-sets="odd__header">
    <xsl:attribute name="start-indent">0pt</xsl:attribute>
    <xsl:attribute name="end-indent">0pt</xsl:attribute>
    <xsl:attribute name="space-before">10pt</xsl:attribute>
    <xsl:attribute name="space-before.conditionality">retain</xsl:attribute>
    <xsl:attribute name="text-align">end</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__body__even__header" use-attribute-sets="even__header">
    <xsl:attribute name="start-indent">0pt</xsl:attribute>
    <xsl:attribute name="end-indent">0pt</xsl:attribute>
    <xsl:attribute name="space-before">10pt</xsl:attribute>
    <xsl:attribute name="space-before.conditionality">retain</xsl:attribute>
    <xsl:attribute name="text-align">start</xsl:attribute>
  </xsl:attribute-set>

  <!-- Hide headers on first pages of chapters -->
  <xsl:attribute-set name="__body__first__header" use-attribute-sets="odd__header">
    <xsl:attribute name="border-bottom">none</xsl:attribute>
    <xsl:attribute name="start-indent">0pt</xsl:attribute>
    <xsl:attribute name="end-indent">0pt</xsl:attribute>
    <xsl:attribute name="space-before">10pt</xsl:attribute>
    <xsl:attribute name="space-before.conditionality">retain</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__body__odd__footer" use-attribute-sets="odd__footer">
    <xsl:attribute name="start-indent">0pt</xsl:attribute>
    <xsl:attribute name="end-indent">0pt</xsl:attribute>
    <xsl:attribute name="space-after">10pt</xsl:attribute>
    <xsl:attribute name="space-after.conditionality">retain</xsl:attribute>
    <xsl:attribute name="text-align">end</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__body__even__footer" use-attribute-sets="even__footer">
    <xsl:attribute name="start-indent">0pt</xsl:attribute>
    <xsl:attribute name="end-indent">0pt</xsl:attribute>
    <xsl:attribute name="space-after">10pt</xsl:attribute>
    <xsl:attribute name="space-after.conditionality">retain</xsl:attribute>
    <xsl:attribute name="text-align">start</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__body__first__footer" use-attribute-sets="odd__footer">
    <xsl:attribute name="start-indent">0pt</xsl:attribute>
    <xsl:attribute name="end-indent">0pt</xsl:attribute>
    <xsl:attribute name="space-after">10pt</xsl:attribute>
    <xsl:attribute name="space-after.conditionality">retain</xsl:attribute>
  </xsl:attribute-set>

  <!-- TOC header/footer overrides -->
  <xsl:attribute-set name="__toc__odd__header" use-attribute-sets="odd__header">
    <xsl:attribute name="start-indent">0pt</xsl:attribute>
    <xsl:attribute name="end-indent">0pt</xsl:attribute>
    <xsl:attribute name="space-before">10pt</xsl:attribute>
    <xsl:attribute name="space-before.conditionality">retain</xsl:attribute>
    <xsl:attribute name="text-align">end</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__toc__even__header" use-attribute-sets="even__header">
    <xsl:attribute name="start-indent">0pt</xsl:attribute>
    <xsl:attribute name="end-indent">0pt</xsl:attribute>
    <xsl:attribute name="space-before">10pt</xsl:attribute>
    <xsl:attribute name="space-before.conditionality">retain</xsl:attribute>
    <xsl:attribute name="text-align">start</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__toc__odd__footer" use-attribute-sets="odd__footer">
    <xsl:attribute name="start-indent">0pt</xsl:attribute>
    <xsl:attribute name="end-indent">0pt</xsl:attribute>
    <xsl:attribute name="space-after">10pt</xsl:attribute>
    <xsl:attribute name="space-after.conditionality">retain</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__toc__even__footer" use-attribute-sets="even__footer">
    <xsl:attribute name="start-indent">0pt</xsl:attribute>
    <xsl:attribute name="end-indent">0pt</xsl:attribute>
    <xsl:attribute name="space-after">10pt</xsl:attribute>
    <xsl:attribute name="space-after.conditionality">retain</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       CODE BLOCKS & PRE-FORMATTED TEXT
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="codeblock" use-attribute-sets="common.block">
    <xsl:attribute name="font-family">monospace</xsl:attribute>
    <xsl:attribute name="font-size">8.5pt</xsl:attribute>
    <xsl:attribute name="background-color">#F4F6FA</xsl:attribute>
    <xsl:attribute name="border">0.5pt solid #D0D5DD</xsl:attribute>
    <xsl:attribute name="border-radius">3pt</xsl:attribute>
    <xsl:attribute name="padding">8pt</xsl:attribute>
    <xsl:attribute name="space-before">6pt</xsl:attribute>
    <xsl:attribute name="space-after">6pt</xsl:attribute>
    <xsl:attribute name="keep-together.within-page">auto</xsl:attribute>
    <xsl:attribute name="white-space-treatment">preserve</xsl:attribute>
    <xsl:attribute name="white-space-collapse">false</xsl:attribute>
    <xsl:attribute name="linefeed-treatment">preserve</xsl:attribute>
    <xsl:attribute name="wrap-option">wrap</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="pre" use-attribute-sets="common.block">
    <xsl:attribute name="font-family">monospace</xsl:attribute>
    <xsl:attribute name="font-size">8.5pt</xsl:attribute>
    <xsl:attribute name="white-space-treatment">preserve</xsl:attribute>
    <xsl:attribute name="white-space-collapse">false</xsl:attribute>
    <xsl:attribute name="linefeed-treatment">preserve</xsl:attribute>
    <xsl:attribute name="wrap-option">wrap</xsl:attribute>
  </xsl:attribute-set>

  <!-- Inline code -->
  <xsl:attribute-set name="codeph">
    <xsl:attribute name="font-family">monospace</xsl:attribute>
    <xsl:attribute name="font-size">9pt</xsl:attribute>
    <xsl:attribute name="background-color">#F0F2F5</xsl:attribute>
    <xsl:attribute name="padding-start">2pt</xsl:attribute>
    <xsl:attribute name="padding-end">2pt</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       TABLES
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="table.title" use-attribute-sets="common.title">
    <xsl:attribute name="font-size">10pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="space-before">6pt</xsl:attribute>
    <xsl:attribute name="space-after">4pt</xsl:attribute>
    <xsl:attribute name="keep-with-next.within-column">always</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="thead.row.entry">
    <xsl:attribute name="background-color">#1D397C</xsl:attribute>
    <xsl:attribute name="color">#FFFFFF</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="font-size">9pt</xsl:attribute>
    <xsl:attribute name="padding">4pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="tbody.row.entry">
    <xsl:attribute name="padding">5pt</xsl:attribute>
    <xsl:attribute name="font-size">9pt</xsl:attribute>
    <xsl:attribute name="border-bottom">0.5pt solid #D0D5DD</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       NOTES, TIPS, WARNINGS
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="note" use-attribute-sets="common.block">
    <xsl:attribute name="background-color">#EBF0FA</xsl:attribute>
    <xsl:attribute name="border-start-width">4pt</xsl:attribute>
    <xsl:attribute name="border-start-style">solid</xsl:attribute>
    <xsl:attribute name="border-start-color">#1D397C</xsl:attribute>
    <xsl:attribute name="padding">8pt</xsl:attribute>
    <xsl:attribute name="space-before">6pt</xsl:attribute>
    <xsl:attribute name="space-after">6pt</xsl:attribute>
    <xsl:attribute name="font-size">9pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="note__label">
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       LINKS
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="common.link">
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="text-decoration">underline</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       LISTS (ordered / unordered)
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="ul" use-attribute-sets="common.block">
    <xsl:attribute name="provisional-distance-between-starts">5mm</xsl:attribute>
    <xsl:attribute name="provisional-label-separation">1mm</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="ol" use-attribute-sets="common.block">
    <xsl:attribute name="provisional-distance-between-starts">5mm</xsl:attribute>
    <xsl:attribute name="provisional-label-separation">1mm</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       DEFINITION LISTS
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="dlentry.dt" use-attribute-sets="common.title">
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="keep-with-next.within-column">always</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       FIGURE
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="fig.title" use-attribute-sets="common.title">
    <xsl:attribute name="font-size">9pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="font-style">italic</xsl:attribute>
    <xsl:attribute name="color">#1D397C</xsl:attribute>
    <xsl:attribute name="space-before">4pt</xsl:attribute>
    <xsl:attribute name="space-after">8pt</xsl:attribute>
    <xsl:attribute name="keep-with-previous.within-page">always</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       SHORT DESCRIPTION
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="topic__shortdesc">
    <xsl:attribute name="font-style">italic</xsl:attribute>
    <xsl:attribute name="color">#555555</xsl:attribute>
    <xsl:attribute name="space-before">4pt</xsl:attribute>
    <xsl:attribute name="space-after">8pt</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       LIST ITEMS — Inter-item spacing
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="ul.li">
    <xsl:attribute name="space-before">2pt</xsl:attribute>
    <xsl:attribute name="space-after">2pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="ol.li">
    <xsl:attribute name="space-before">3pt</xsl:attribute>
    <xsl:attribute name="space-after">3pt</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       DEFINITION LIST — Term/definition spacing
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="dlentry">
    <xsl:attribute name="space-before">4pt</xsl:attribute>
    <xsl:attribute name="space-after">4pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="dlentry.dd">
    <xsl:attribute name="space-before">1pt</xsl:attribute>
    <xsl:attribute name="space-after">2pt</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       TASK — Prerequisites, context, and result styling
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="prereq" use-attribute-sets="common.block">
    <xsl:attribute name="background-color">#FDF8ED</xsl:attribute>
    <xsl:attribute name="border-start-width">4pt</xsl:attribute>
    <xsl:attribute name="border-start-style">solid</xsl:attribute>
    <xsl:attribute name="border-start-color">#E9AC15</xsl:attribute>
    <xsl:attribute name="padding">8pt</xsl:attribute>
    <xsl:attribute name="space-before">8pt</xsl:attribute>
    <xsl:attribute name="space-after">8pt</xsl:attribute>
    <xsl:attribute name="font-size">9pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="result" use-attribute-sets="common.block">
    <xsl:attribute name="border-top">1pt solid #0ACB8B</xsl:attribute>
    <xsl:attribute name="padding-top">6pt</xsl:attribute>
    <xsl:attribute name="space-before">10pt</xsl:attribute>
  </xsl:attribute-set>

  <!-- ═══════════════════════════════════════════════════════════════
       RELATED LINKS — Visual separation from body
       ═══════════════════════════════════════════════════════════════ -->
  <xsl:attribute-set name="related-links">
    <xsl:attribute name="space-before">14pt</xsl:attribute>
    <xsl:attribute name="border-top">1pt solid #D0D5DD</xsl:attribute>
    <xsl:attribute name="padding-top">8pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="related-links__content">
    <xsl:attribute name="font-size">9pt</xsl:attribute>
  </xsl:attribute-set>

</xsl:stylesheet>
