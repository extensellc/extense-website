# DITA Working Examples

Complete starter projects demonstrating real-world DITA implementations.

## 📚 Projects in this section

### [dita-html5-sidebar-starter-v1](dita-html5-sidebar-starter-v1/)
**Basic HTML5 Starter Project**

A minimal, easy-to-understand DITA project demonstrating core concepts.

#### What's Included
- **DITA Content**
  - Sample map (getting-started.ditamap)
  - Concept topic (what-is-dita.dita)
  - Task topic (install.dita)
  - Reference topic (cli-reference.dita)
  - Reuse snippets file (shared/reuse-snippets.dita)

- **Customization**
  - HTML5 sidebar plug-in (com.acme.html5.sidebar)
  - Custom CSS (brand.css)
  - Site JavaScript (site.js)
  - XSLT overrides for sidebar TOC

- **Build Configuration**
  - Property file (html5-sidebar.properties)
  - Build scripts (build.sh + build.ps1)
  - .gitignore for outputs

#### Use Cases
- ✅ Learning DITA basics
- ✅ Quick proof-of-concept
- ✅ Understanding plug-in structure
- ✅ Single-variant documentation sites

#### Quick Start
```bash
cd dita-html5-sidebar-starter-v1
./build/build.sh          # Linux/Mac
./build/build.ps1         # Windows
```

View output in `out/html/` directory.

---

### [dita-html5-sidebar-starter-v2](dita-html5-sidebar-starter-v2/)
**Production Multi-Variant Starter Project**

An advanced DITA project demonstrating real-world multi-variant publishing.

#### What's Included (Beyond v1)

- **Extended DITA Content**
  - Enhanced getting-started map with keys
  - Additional concept topic (elements-cookbook.dita)
  - Profiled content for multiple audiences
  - Platform-specific content (web vs print)

- **Multi-Variant Build System**
  - **Web variant** (web.ditaval) — Full navigation, interactive features
  - **Print variant** (print.ditaval) — Print-optimized, PDF-ready
  - **Admin variant** (audience-admin.ditaval) — Advanced content visible
  - **Novice variant** (audience-novice.ditaval) — Simplified content only

- **Enhanced Customization**
  - Improved responsive CSS
  - Variant-specific styling hooks
  - Advanced TOC customization
  - Better mobile experience

- **Production Build Scripts**
  - Separate scripts per variant
  - Dedicated property files
  - DITAVAL filters in build/ditaval/
  - Parallel build capability

#### Use Cases
- ✅ Enterprise documentation with multiple audiences
- ✅ Product variants (web vs desktop, basic vs pro)
- ✅ Multi-platform publishing (online vs PDF)
- ✅ Role-based content delivery (admin vs end-user)
- ✅ Learning advanced DITA patterns

#### Quick Start
```bash
cd dita-html5-sidebar-starter-v2

# Build all variants
./build/build-web.sh      # Web-optimized
./build/build-print.sh    # Print-optimized
./build/build-admin.sh    # Admin audience
./build/build-novice.sh   # Novice audience
```

View outputs in `out/` subdirectories (html-web, html-print, etc.).

---

## 🎯 Choosing the Right Starter

### Use v1 if you:
- Are learning DITA for the first time
- Need a minimal working example
- Want to understand core concepts without complexity
- Have a single-audience, single-format requirement
- Are building a proof-of-concept quickly

### Use v2 if you:
- Need multiple build variants (audience, platform, format)
- Want to see production-ready patterns
- Are building enterprise documentation
- Need to understand DITAVAL filtering
- Want to learn advanced DITA features

### Use both if you:
- Want to see progression from simple to advanced
- Are training a team with varying skill levels
- Need examples for different project scales

---

## 📊 Feature Comparison

| Feature | v1 (Basic) | v2 (Production) |
|---------|------------|-----------------|
| Sample topics | 4 | 5 |
| Maps | 1 | 1 (with keys) |
| Build variants | 1 | 4 |
| DITAVAL files | 0 | 4 |
| Build scripts | 2 | 8 |
| Property files | 1 | 5 |
| CSS complexity | Basic | Advanced responsive |
| Keys/keyrefs | No | Yes |
| Profiled content | No | Yes (audience + platform) |
| Reuse examples | Basic conref | Conref + keyref + conkeyref |
| TOC customization | Basic sidebar | Advanced nested sections |
| Mobile support | Basic | Fully responsive |
| Production-ready | Learning tool | Production template |

---

## 🛠️ Project Structure Deep Dive

### Common Structure (Both Projects)

```
starter-project/
├── README.md                    # Project documentation
├── .gitignore                   # Ignore outputs and temp files
├── build/                       # Build configuration
│   ├── *.properties            # DITA-OT parameters
│   ├── build.sh / build.ps1    # Build scripts
│   └── ditaval/                # Filters (v2 only)
├── css/                         # Stylesheets
│   └── brand.css               # Custom CSS
├── js/                          # JavaScript
│   └── site.js                 # Site interactions
├── dita/                        # DITA source content
│   ├── maps/                   # DITA maps
│   ├── topics/                 # DITA topics
│   │   ├── concepts/           # Concept topics
│   │   ├── tasks/              # Task topics
│   │   ├── reference/          # Reference topics
│   │   └── shared/             # Reusable snippets
│   └── media/                  # Images and media
└── plugins/                     # Custom plug-ins
    └── com.acme.html5.sidebar/ # Sidebar plug-in
        ├── plugin.xml          # Plug-in descriptor
        └── xsl/                # XSLT overrides
```

### Build Output Structure

```
out/
├── html/                        # v1 output
├── html-web/                    # v2 web variant
├── html-print/                  # v2 print variant
├── html-admin/                  # v2 admin variant
└── html-novice/                 # v2 novice variant
```

---

## 🧪 Hands-On Exercises

### Exercise 1: Explore v1 (30 minutes)
1. Extract and examine project structure
2. Read topics in `dita/topics/`
3. Review map in `dita/maps/`
4. Build with `./build/build.sh`
5. Examine output in `out/html/`
6. Modify `css/brand.css` and rebuild

**Learning:** Basic DITA structure, build process

---

### Exercise 2: Add Content to v1 (60 minutes)
1. Create new concept topic
2. Add to map
3. Use conref from shared snippets
4. Rebuild and verify
5. Add image to media/ folder
6. Reference image in topic

**Learning:** Authoring workflow, reuse, media handling

---

### Exercise 3: Customize v1 Plug-in (90 minutes)
1. Examine `plugins/com.acme.html5.sidebar/`
2. Review XSLT in `xsl/html5/override.xsl`
3. Add custom CSS class to paragraphs
4. Reinstall plug-in: `dita install`
5. Rebuild and verify change
6. Document customization

**Learning:** Plug-in structure, XSLT overrides

---

### Exercise 4: Explore v2 Variants (45 minutes)
1. Examine DITAVAL files in `build/ditaval/`
2. Review profiled content in topics
3. Build web variant: `./build/build-web.sh`
4. Build print variant: `./build/build-print.sh`
5. Compare outputs
6. Identify what content changed

**Learning:** Conditional processing, build variants

---

### Exercise 5: Create Custom Variant (2 hours)
1. Create new DITAVAL file (developer.ditaval)
2. Add profiling attributes to topics
3. Create new property file
4. Create new build script
5. Test build
6. Document variant purpose

**Learning:** Advanced filtering, build configuration

---

### Exercise 6: Production Deployment (2 hours)
1. Choose v2 as base
2. Replace sample content with real topics
3. Customize CSS for brand
4. Configure build variants for your needs
5. Set up CI/CD (see [Developer Handbook](../developer-guides/dita-ot-developer-handbook.md))
6. Deploy to hosting

**Learning:** Real-world implementation

---

## 🎓 Learning Paths

### Path 1: Content Creator (v1 focus)
1. Extract v1
2. Read all sample topics
3. Complete Exercises 1-2
4. Write 5 new topics
5. Build and review output

**Time:** 4-6 hours  
**Outcome:** Can author DITA content

---

### Path 2: Technical Publisher (v2 focus)
1. Complete Path 1
2. Extract v2
3. Complete Exercises 4-5
4. Set up multi-variant build
5. Document build process

**Time:** 8-12 hours  
**Outcome:** Can manage multi-variant publishing

---

### Path 3: Developer (Both projects)
1. Complete Path 1
2. Complete Exercise 3 (plug-in customization)
3. Extract v2
4. Complete Exercise 6 (production deployment)
5. Follow [XSLT Tutorial](../plugins-and-customization/dita-ot-html5-xslt-customization-final.md)

**Time:** 15-20 hours  
**Outcome:** Can build custom DITA toolchains

---

## 🔧 Customization Starting Points

### Branding
**File:** `css/brand.css`
- Change colors (CSS variables)
- Update fonts
- Modify spacing
- Add logo

### Navigation
**Files:** `plugins/*/xsl/toc/toc-override.xsl`
- Change TOC structure
- Add/remove TOC elements
- Customize link behavior
- Add metadata display

### HTML Structure
**Files:** `plugins/*/xsl/html5/override.xsl`
- Override element templates
- Add CSS classes
- Inject JavaScript
- Modify topic headers/footers

### Build Configuration
**Files:** `build/*.properties`
- Change output directory
- Set chunking strategy
- Configure nav-toc display
- Add custom parameters

---

## 📦 Installation & Prerequisites

### Required Software
- **DITA-OT 4.x** — [Download from dita-ot.org](https://www.dita-ot.org)
- **Java 17+** — Required by DITA-OT
- **Bash** (Linux/Mac) or **PowerShell** (Windows) — For build scripts

### Optional Software
- **Git** — For version control
- **Visual Studio Code** — With DITA extension
- **Oxygen XML Editor** — Professional DITA authoring
- **Docker** — For containerized builds

### Installation Steps
```bash
# 1. Install DITA-OT
wget https://github.com/dita-ot/dita-ot/releases/download/4.2/dita-ot-4.2.zip
unzip dita-ot-4.2.zip
export DITA_HOME=/path/to/dita-ot-4.2

# 2. Extract starter project
cd dita-html5-sidebar-starter-v1

# 3. Install custom plug-in
cd plugins/com.acme.html5.sidebar
dita install

# 4. Build
cd ../../
./build/build.sh
```

---

## 🔗 Related Documentation

**Tutorials:**
- [DITA Quick Introduction](../getting-started/dita_intro_guide.md) — Before using starters
- [XSLT Customization Tutorial](../plugins-and-customization/dita-ot-html5-xslt-customization-final.md) — Deep customization guide

**Guides:**
- [DITA Authoring](../core-topics/dita-topic-2-authoring.md) — Writing effective topics
- [Reuse and Variants](../core-topics/dita-topic-3-reuse-variants.md) — Advanced filtering
- [Publishing with DITA-OT](../core-topics/dita-topic-4-publishing-dita-ot.md) — Build workflows

**Developer Resources:**
- [Developer Handbook](../developer-guides/dita-ot-developer-handbook.md) — Architecture and CI/CD
- [Architecture Diagram](../reference/dita-ot-architecture-ascii-snippet.md) — Visual reference

---

## 💡 Tips for Success

### Working with Starter Projects
✅ **Do:** Start with one variant, add complexity gradually  
✅ **Do:** Read all README files in project  
✅ **Do:** Examine sample topics before creating your own  
✅ **Do:** Version-control your customizations  
❌ **Don't:** Modify core DITA-OT files  
❌ **Don't:** Skip plug-in installation step  
❌ **Don't:** Ignore validation errors  

### Customizing for Production
✅ **Do:** Document all customizations  
✅ **Do:** Test across all browsers  
✅ **Do:** Validate HTML output  
✅ **Do:** Check accessibility (WCAG)  
✅ **Do:** Performance-test with large doc sets  

### Building Teams
✅ **Do:** Use v1 for onboarding  
✅ **Do:** Use v2 for real projects  
✅ **Do:** Share build scripts with team  
✅ **Do:** Establish naming conventions  
✅ **Do:** Create internal customization guide  

---

## 🚀 Next Steps

After exploring these examples:

1. **Choose your base** (v1 or v2)
2. **Replace sample content** with your documentation
3. **Customize branding** (CSS, logos, colors)
4. **Configure variants** for your needs
5. **Set up version control** (Git repository)
6. **Automate builds** (CI/CD pipeline)
7. **Deploy** to your hosting platform

---

## 📞 Getting Help

**Project-Specific:**
- Check README.md in each project
- Review comments in build scripts
- Examine XSLT comments

**General DITA:**
- [Main Documentation Index](../README.md)
- [DITA-OT Documentation](https://www.dita-ot.org)
- [DITA Users Group](https://groups.io/g/dita-users)

---

Return to [Main Documentation Index](../README.md)
