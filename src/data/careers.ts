/*
  Careers data — single source of truth for the open-positions roster.

  Consumed by:
    - src/pages/company/careers.astro        (roster index + shared boilerplate)
    - src/pages/company/careers/[slug].astro (per-role detail pages)

  The `id` field doubles as the URL slug for the detail page route.
*/

export interface Job {
  id: string;
  number: string;
  postingRef: string;
  title: string;
  subtitle: string;
  department: string;
  employmentType: string;
  workArrangement: string;
  salaryBand: string;
  aboutRole: string;
  keyResponsibilities: string[];
  requiredQualifications: string[];
  preferredQualifications: string[];
  bonusPoints?: string[];
  education: string;
}

export const CAREERS_EMAIL = "careers@extense.co";

// Shown on every detail page below the salary band.
export const SALARY_NOTE =
  "The range is intentionally wide; final compensation depends on the candidate's experience, qualifications, technical skills, and applicable government-contracting rates.";

// Prepended as the first item of Required Qualifications on every role.
// Tighter than the previous “U.S. Persons (22 CFR 120.62)” framing —
// all positions now require U.S. citizenship outright.
export const UNIVERSAL_CITIZENSHIP_REQ =
  "U.S. citizenship is required; selected candidate must be willing to undergo a federal background investigation.";

export const jobs: Job[] = [
  {
    id: "technical-publications-ietm-lead",
    number: "01",
    postingRef: "EXT-TPL-2026-01",
    title: "Technical Publications / IETM Lead",
    subtitle: "Lead delivery of IETM baselining and technical-manual programs for defense and aerospace customers.",
    department: "Technical Publications & IETM Practice",
    employmentType: "Full-Time, Exempt",
    workArrangement: "Remote (U.S.) with periodic travel to customer / partner sites",
    salaryBand: "$95K – $160K base, plus benefits",
    aboutRole: "The Technical Publications / IETM Lead owns delivery of Extense's Interactive Electronic Technical Manual (IETM) and structured-content programs supporting U.S. military aviation, rotorcraft, and aerospace customers. You will coordinate technical writers, S1000D / XML specialists, illustrators, QA, and aircraft SMEs to plan, execute, and release configuration-controlled publication baselines. You will serve as the senior Extense point of contact to prime contractors and government end-customers, and you will be accountable for technical accuracy, schedule, and contractual compliance of every deliverable that leaves the practice.",
    keyResponsibilities: [
      "Lead end-to-end execution of IETM baseline updates, including planning, scoping, work breakdown, scheduling, risk management, and customer reporting.",
      "Coordinate a multi-disciplinary team of authors, XML / XSLT developers, illustrators, QA analysts, configuration analysts, and aircraft / equipment SMEs.",
      "Serve as primary client interface with prime-contractor program offices and government customers; manage review cycles, comment resolution, and acceptance.",
      "Translate Engineering Change Proposals (ECPs), Engineering Change Notices (ECNs), and Technical Directives into a documentation impact analysis and update plan.",
      "Enforce compliance with applicable specifications including S1000D, MIL-STD-40051-1, MIL-STD-3001, and customer Business Rules / BREX.",
      "Manage publication baselines and release packages; coordinate with Configuration Management to ensure data-module revisions match the approved aircraft / equipment configuration.",
      "Track CDRL deliverables, ensure on-time submission, and own corrective action when reviews identify defects.",
      "Mentor and develop technical-publication staff; conduct technical reviews and promote consistency in authoring quality.",
      "Support business development by contributing to capability statements, proposal narratives, work statements, and labor / effort estimates for new opportunities.",
    ],
    requiredQualifications: [
      "10+ years of experience in technical-publication delivery for defense, aerospace, or other regulated-equipment industries.",
      "5+ years of direct experience leading IETM, IETP, or large structured-content programs from kickoff through customer acceptance.",
      "Demonstrated working knowledge of S1000D (Issue 4.x or later), Data Module concepts, DMRL, BREX, applicability / effectivity, and Common Source Database (CSDB) workflows.",
      "Working knowledge of MIL-STD-40051-1 (digital technical information / IETM) and related military technical-manual specifications.",
      "Proven experience managing a multi-disciplinary team (authors, illustrators, XML developers, QA, SMEs) on a single technical-publication program.",
      "Strong client-facing communication skills; demonstrated experience interacting with prime contractor or government program offices.",
      "Hands-on experience with CDRL preparation, review-comment dispositioning, and release-package compilation.",
      "Strong written English, technical-editing eye, and ability to enforce style and consistency across a team.",
    ],
    preferredQualifications: [
      "Direct program experience supporting U.S. Navy, U.S. Marine Corps, U.S. Army Aviation, or U.S. Air Force aircraft / rotorcraft technical-manual programs.",
      "Experience with rotorcraft (H-1 family, AH-64, UH-60, CH-47, V-22, MH-60, or similar) or fixed-wing platforms.",
      "Familiarity with one or more CSDB / IETM platforms (e.g., Arbortext PE, Inmedius, Adept, Astoria, Auster, Mekon, SDL/Trisoft, or equivalent).",
      "PMP, PMI-ACP, or equivalent program-management certification.",
      "Active U.S. Government security clearance (Secret or higher).",
      "Prior experience as a subcontractor team lead on prime-led DoD programs.",
    ],
    bonusPoints: [
      "Familiarity with DITA in addition to S1000D.",
      "Experience supporting transition from legacy SGML / Word-based manuals to S1000D / IETM.",
      "Familiarity with Section 508 / WCAG 2.1 requirements for federal digital technical content.",
    ],
    education: "Bachelor's degree in English, Technical Communication, Engineering, Computer Science, Aviation, or a related field. Equivalent professional experience (15+ years) in defense or aerospace technical publications will be considered in lieu of a degree.",
  },
  {
    id: "s1000d-xml-content-architect",
    number: "02",
    postingRef: "EXT-S1A-2026-02",
    title: "S1000D / XML Content Architect",
    subtitle: "Define and govern the structured-content architecture for defense aviation IETM programs.",
    department: "Technical Publications & IETM Practice",
    employmentType: "Full-Time, Exempt",
    workArrangement: "Remote (U.S.) with occasional travel",
    salaryBand: "$80K – $145K base, plus benefits",
    aboutRole: "The S1000D / XML Content Architect is the structured-content authority for Extense's aviation and defense IETM programs. You will design and govern the data-module strategy, DMRL, applicability model, Business Rules / BREX, and publication-module structure that the rest of the team builds against. You will work closely with the IETM Lead, customer architects, and XML/XSLT engineering to ensure that source content is reusable, validates cleanly, and publishes correctly into IETM, HTML, and PDF outputs.",
    keyResponsibilities: [
      "Design the S1000D content architecture for new and existing programs: data module taxonomy, Data Module Codes (DMC), information types, applicability model, and naming conventions.",
      "Develop and maintain Data Module Requirement Lists (DMRLs) aligned to engineering / configuration baselines.",
      "Author, govern, and evolve project Business Rules and BREX (Business Rules Exchange) files; review data modules for BREX compliance.",
      "Define publication-module structures and content-reuse strategies (CIRs, common information repositories, warning / caution catalogs, etc.).",
      "Lead applicability and effectivity strategy across multiple aircraft / configuration variants.",
      "Review and correct authored data modules for schema, BREX, and editorial conformance before release.",
      "Support CSDB structure, status workflow, and content-promotion rules.",
      "Coordinate with XML/XSLT engineering on transformation, validation, and publishing pipelines so source architecture and output behavior remain aligned.",
      "Maintain authoritative architecture documentation: style guide, business rules, applicability model, DMC scheme, and content-reuse policies.",
      "Mentor authors and reviewers on correct S1000D practice; act as escalation point for complex content-modeling questions.",
    ],
    requiredQualifications: [
      "8+ years of structured-content / XML technical-publications experience.",
      "5+ years of direct hands-on experience with S1000D (Issue 4.0.1, 4.1, 4.2, or later) on a production program.",
      "Demonstrated experience defining and governing a DMRL, BREX, and applicability model for a real-world aircraft, vehicle, or equipment program.",
      "Strong working knowledge of S1000D schemas, information types, DMC structure, ICN management, and CIR usage.",
      "Hands-on experience with at least one CSDB platform (e.g., Arbortext PE / Inmedius S1000D Suite, Auster, eXtyles, SDL, Mekon, or equivalent).",
      "Solid grasp of XML fundamentals: XSD, DTD, XPath, and XML validation tooling.",
      "Experience interpreting Engineering Change documentation and translating it into S1000D content-impact decisions.",
      "Clear written communication skills; able to write architecture documentation that authors and developers can follow.",
    ],
    preferredQualifications: [
      "Experience on U.S. military aviation programs governed by MIL-STD-40051-1.",
      "Experience supporting an IETM Level 4 / Level 5 program (decision trees, fault isolation logic, interactive graphics, integrated diagnostics).",
      "Familiarity with the S1000D Bridge to ATA iSpec 2200 or to DITA, where programs require cross-publishing.",
      "Experience converting legacy SGML, Word, or FrameMaker source to S1000D.",
      "Schematron rule authoring for business-rule enforcement beyond what BREX covers.",
      "Active U.S. Government security clearance.",
    ],
    education: "Bachelor's degree in Computer Science, Information Science, Linguistics, Technical Communication, Engineering, or a related field. Equivalent professional experience (10+ years) in S1000D production environments will be considered in lieu of a degree.",
  },
  {
    id: "xml-xslt-publishing-automation-developer",
    number: "03",
    postingRef: "EXT-XSL-2026-03",
    title: "XML / XSLT Publishing Automation Developer",
    subtitle: "Build the transformation, validation, and publishing pipelines behind aerospace IETM and technical-manual delivery.",
    department: "Technical Publications & IETM Practice",
    employmentType: "Full-Time, Exempt",
    workArrangement: "Remote (U.S.)",
    salaryBand: "$75K – $135K base, plus benefits",
    aboutRole: "The XML / XSLT Publishing Automation Developer is the engineering core of Extense's publishing stack. You will build and maintain the transformations, validation rules, and automation scripts that move S1000D and other structured content through cleanup, validation, baseline comparison, and publication into IETM, HTML, and PDF outputs. This is a hands-on technical role for someone who enjoys writing XSLT, debugging XPath, and turning messy XML into reliable, traceable publishing pipelines.",
    keyResponsibilities: [
      "Develop, maintain, and optimize XSLT (1.0, 2.0, and 3.0) transformations to convert S1000D / DITA / structured XML into HTML, PDF, and IETM-ready output formats.",
      "Build and maintain Schematron rule sets to enforce business rules beyond what XSD / BREX can express.",
      "Implement validation pipelines: XSD validation, BREX checking, link / cross-reference verification, ICN / graphics reference checks, and applicability validation.",
      "Develop scripts (Python, Bash, Node.js, or equivalent) for batch processing of XML repositories: cleanup, normalization, mass tagging, ID generation, and baseline diff reports.",
      "Customize and maintain DITA-OT or equivalent publishing toolchains as program needs require.",
      "Build baseline-comparison utilities to identify changed, added, and deleted data modules between releases.",
      "Support CSDB integrations: import / export jobs, content migration, and bulk update tooling.",
      "Diagnose and resolve XML, XSLT, XPath, validation, and output-fidelity issues raised by authors, QA, and the IETM Lead.",
      "Document toolchain configuration, transformations, and operational procedures so the pipeline is maintainable by the broader team.",
      "Collaborate with the S1000D Architect on content-model changes and with QA on validation-report formats.",
    ],
    requiredQualifications: [
      "6+ years of professional experience as an XML / XSLT developer in a technical-publications, documentation, or structured-content environment.",
      "Expert-level XSLT 2.0 / 3.0 and XPath 2.0 / 3.1; able to write, debug, and optimize complex transformations from scratch.",
      "Strong working knowledge of XSD, DTD, and Schematron.",
      "Hands-on experience with at least one production publishing toolchain (DITA-OT, custom XSLT pipelines, Antenna House / RenderX / FOP for PDF, etc.).",
      "Proficiency in at least one general-purpose scripting language (Python, Node.js, Bash, PowerShell) for batch XML processing and pipeline automation.",
      "Experience using XML editors and processors such as oXygen XML Editor, Saxon, Xalan, or equivalent.",
      "Comfort working from the command line; version-control proficiency (Git or equivalent).",
      "Ability to write clear technical documentation for the pipelines you build.",
    ],
    preferredQualifications: [
      "Hands-on production experience with S1000D content and CSDB platforms.",
      "Experience building IETM / IETP publishing pipelines for defense or aerospace customers.",
      "XSL-FO experience and PDF accessibility (tagged PDF / PDF/UA) experience.",
      "Familiarity with REST APIs and integration with content-management or CSDB systems.",
      "Familiarity with controlled-document environments and configuration management workflows.",
      "Active U.S. Government security clearance.",
    ],
    bonusPoints: [
      "Contributions to open-source DITA-OT plugins, Saxon utilities, or S1000D community tooling.",
      "Experience with XQuery and native XML databases (BaseX, eXist-db, MarkLogic).",
    ],
    education: "Bachelor's degree in Computer Science, Software Engineering, Information Science, or a related technical field. Equivalent professional experience (8+ years) building production XML / XSLT systems will be considered in lieu of a degree.",
  },
  {
    id: "s1000d-ietm-technical-author",
    number: "04",
    postingRef: "EXT-TWA-2026-04",
    title: "S1000D / IETM Technical Author",
    subtitle: "Write the maintenance procedures, troubleshooting paths, and operating content that make aerospace IETMs usable in the field.",
    department: "Technical Publications & IETM Practice",
    employmentType: "Full-Time, Exempt",
    workArrangement: "Remote (U.S.) with periodic SME / customer visits",
    salaryBand: "$60K – $105K base, plus benefits",
    aboutRole: "The S1000D / IETM Technical Author writes the procedural, descriptive, and operational content that lives inside Extense's structured technical manuals and IETMs. You will translate engineering data, SME interviews, drawings, schematics, and Engineering Change Notices into clear, accurate, configuration-controlled data modules. You will work closely with the S1000D Architect, illustrators, troubleshooting authors, and aircraft / equipment SMEs to make sure every procedure is technically right, safely sequenced, and properly tagged.",
    keyResponsibilities: [
      "Author and revise S1000D data modules — procedural (remove / install / inspect / test / service), descriptive, fault-isolation, and IPD-related — in accordance with project Business Rules and BREX.",
      "Translate Engineering Change Proposals, redlines, SME notes, and source drawings into clear, properly sequenced maintenance procedures.",
      "Apply correct warnings, cautions, notes, tools, consumables, support equipment, personnel requirements, and figure references.",
      "Tag data modules with correct applicability / effectivity values for the supported aircraft or equipment variants.",
      "Coordinate with technical illustrators to specify and validate figures, callouts, and hotspots.",
      "Respond to customer review comments (Government, prime contractor, and internal QA) and disposition them in coordination with SMEs and the IETM Lead.",
      "Use the project CSDB to check out, check in, and progress data modules through the configured status workflow.",
      "Maintain authoring quality metrics: BREX-clean modules, low rework rate, low defect rate at QA.",
      "Contribute to the project style guide; surface recurring authoring issues to the S1000D Architect.",
    ],
    requiredQualifications: [
      "5+ years of professional technical-writing experience, with at least 3 years authoring in a structured-content environment (S1000D, DITA, or equivalent XML schema).",
      "Hands-on experience authoring procedural maintenance content for aircraft, military vehicles, weapons systems, industrial equipment, or other regulated hardware.",
      "Demonstrated experience working from engineering drawings, schematics, parts catalogs, and SME notes.",
      "Working knowledge of S1000D data-module structure, information types, and applicability tagging.",
      "Experience with at least one S1000D authoring environment (Arbortext Editor, oXygen XML Editor with S1000D framework, XMetaL, or equivalent).",
      "Strong written English; ability to write controlled, unambiguous procedural language.",
      "Comfort interacting with engineering and maintenance SMEs to extract and validate technical content.",
    ],
    preferredQualifications: [
      "Direct experience on U.S. military aviation or rotorcraft technical-manual programs.",
      "Experience with MIL-STD-40051-1 IETM content.",
      "Familiarity with ASD-STE100 Simplified Technical English.",
      "Background as an aircraft maintainer, field service representative, or aviation technician who has transitioned into writing.",
      "Experience authoring fault-isolation / troubleshooting procedures.",
      "Active U.S. Government security clearance.",
    ],
    education: "Bachelor's degree in English, Technical Communication, Engineering, Aviation, or a related field. Military technical-training background combined with relevant experience (7+ years) will be considered in lieu of a degree.",
  },
  {
    id: "ietm-qa-configuration-analyst",
    number: "05",
    postingRef: "EXT-QAC-2026-05",
    title: "IETM QA / Configuration Analyst",
    subtitle: "Make sure every IETM baseline that leaves Extense is link-clean, BREX-clean, applicability-correct, and traceable to the right configuration.",
    department: "Technical Publications & IETM Practice",
    employmentType: "Full-Time, Exempt",
    workArrangement: "Remote (U.S.)",
    salaryBand: "$60K – $100K base, plus benefits",
    aboutRole: "The IETM QA / Configuration Analyst is the last line of defense before an Extense technical-publication deliverable goes to the customer. You will validate XML source content and IETM output for completeness, link integrity, applicability correctness, BREX conformance, schema validity, and faithful representation of the approved engineering baseline. You will also own the configuration / baseline comparison work that lets the program prove what changed between one release and the next.",
    keyResponsibilities: [
      "Run schema validation, BREX validation, Schematron checks, and link / cross-reference checks across S1000D / XML source repositories.",
      "Test IETM output for navigation, search behavior, applicability filtering, link traversal, figure display, and procedure rendering on the target IETM viewer.",
      "Maintain the program baseline-comparison matrix: which data modules changed, were added, or were removed between releases, and why.",
      "Track defects from identification through correction and verification using the program defect-tracking tool (Jira, Azure DevOps, or equivalent).",
      "Verify that customer review comments have been correctly dispositioned and that the resulting changes are present in the next baseline.",
      "Coordinate release readiness: validation report, defect closure, baseline manifest, change summary, and CDRL submission package.",
      "Maintain version / revision history of data modules and align it with engineering configuration data (ECP / ECN / TD references).",
      "Surface systemic authoring or transformation issues to the S1000D Architect and XML / XSLT Developer for upstream correction.",
      "Support audit and customer-acceptance activities, including First Article / In-Process Reviews and Final Verification Reviews.",
    ],
    requiredQualifications: [
      "5+ years of experience in technical-publication QA, configuration management, or technical-data analysis.",
      "Hands-on experience validating structured content (S1000D, DITA, or equivalent XML).",
      "Comfort with XML, XPath, and at least basic XSLT — enough to read transformations and write simple validation queries.",
      "Experience using defect-tracking and version-control tools (Jira, Azure DevOps, Git, Subversion, or equivalent).",
      "Strong attention to detail; demonstrated ability to detect inconsistencies others miss.",
      "Clear written communication; able to produce validation reports and defect descriptions that authors and developers can act on.",
    ],
    preferredQualifications: [
      "Direct experience supporting IETM / IETP programs for U.S. military aviation or aerospace customers.",
      "Experience with CSDB platforms and S1000D status workflow.",
      "Familiarity with MIL-STD-40051-1, MIL-STD-3001, and configuration-management standards (EIA-649, MIL-HDBK-61).",
      "Section 508 / WCAG 2.1 awareness for digital deliverables.",
      "Active U.S. Government security clearance.",
    ],
    education: "Bachelor's degree in Technical Communication, Information Science, Engineering, Computer Science, or a related field. Equivalent professional experience (7+ years) in technical-publication QA or configuration management will be considered in lieu of a degree.",
  },
];
