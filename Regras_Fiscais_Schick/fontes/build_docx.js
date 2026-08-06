// Reusable ABNT-style .docx builder (docx-js).
// Usage: node build_docx.js <input.txt> <output.docx> [--font Arial|Times]
// Line-prefix DSL:
//   TITLE:   -> document title (centered, bold, 14pt, spacing after)
//   SUB:     -> subtitle line under title (centered, bold 12)
//   CENTER:  -> centered line (12pt)
//   NOTE:    -> small italic note (10pt, justified, no indent)
//   # ...    -> section heading  H1 (bold 12, left)
//   ## ...   -> subsection heading H2 (bold-italic 12, left)
//   ### ...  -> heading H3 (bold 12, left, smaller spacing)
//   * ...    -> bullet item
//   > ...    -> block quote (indented left 4cm... actually 2.5cm extra, italic-off, single-ish)
//   ---      -> horizontal rule (paragraph bottom border)
//   (blank)  -> paragraph break (ignored; paragraphs are per-line)
//   other    -> body paragraph (justified, first-line indent 1.25cm, 1.5 spacing)

const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  LevelFormat, BorderStyle, HeadingLevel, PageBreak,
} = require("docx");

const args = process.argv.slice(2);
const inPath = args[0];
const outPath = args[1];
const fontArg = (args.includes("--font") ? args[args.indexOf("--font") + 1] : "Arial");
const FONT = fontArg === "Times" ? "Times New Roman" : "Arial";

const MARGIN = 1417;      // 2.5 cm in twips
const INDENT = 709;       // 1.25 cm in twips
const LINE = 360;         // 1.5 line spacing
const SIZE = 24;          // 12pt (half-points)

const raw = fs.readFileSync(inPath, "utf8").replace(/\r/g, "");
const lines = raw.split("\n");

// Support simple inline bold with **...**
function runs(text, base = {}) {
  const out = [];
  const parts = text.split(/(\*\*[^*]+\*\*)/g);
  for (const p of parts) {
    if (!p) continue;
    if (p.startsWith("**") && p.endsWith("**")) {
      out.push(new TextRun({ text: p.slice(2, -2), bold: true, font: FONT, size: base.size || SIZE, italics: base.italics }));
    } else {
      out.push(new TextRun({ text: p, font: FONT, size: base.size || SIZE, bold: base.bold, italics: base.italics }));
    }
  }
  if (out.length === 0) out.push(new TextRun({ text: "", font: FONT, size: base.size || SIZE }));
  return out;
}

const children = [];

function body(text) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    spacing: { line: LINE, lineRule: "auto", before: 0, after: 0 },
    indent: { firstLine: INDENT },
    children: runs(text),
  });
}

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  const t = line.trim();
  if (t === "") continue; // blank lines are separators; each content line is its own paragraph

  if (t.startsWith("PAGEBREAK")) {
    children.push(new Paragraph({ children: [new PageBreak()] }));
    continue;
  }
  if (t.startsWith("TITLE:")) {
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { line: LINE, lineRule: "auto", before: 0, after: 240 },
      children: [new TextRun({ text: t.slice(6).trim(), bold: true, font: FONT, size: 28 })],
    }));
    continue;
  }
  if (t.startsWith("SUB:")) {
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { line: LINE, lineRule: "auto", before: 0, after: 120 },
      children: [new TextRun({ text: t.slice(4).trim(), bold: true, font: FONT, size: SIZE })],
    }));
    continue;
  }
  if (t.startsWith("CENTER:")) {
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { line: LINE, lineRule: "auto", before: 0, after: 60 },
      children: runs(t.slice(7).trim()),
    }));
    continue;
  }
  if (t.startsWith("NOTE:")) {
    children.push(new Paragraph({
      alignment: AlignmentType.JUSTIFIED,
      spacing: { line: 276, lineRule: "auto", before: 0, after: 60 },
      children: [new TextRun({ text: t.slice(5).trim(), italics: true, font: FONT, size: 20 })],
    }));
    continue;
  }
  if (t.startsWith("COVH:")) {
    // Cabeçalho do bloco de cobertura do módulo (pequeno, com borda superior)
    children.push(new Paragraph({
      alignment: AlignmentType.LEFT,
      spacing: { line: 240, lineRule: "auto", before: 120, after: 30 },
      border: { top: { color: "AAAAAA", space: 4, style: BorderStyle.SINGLE, size: 4 } },
      children: [new TextRun({ text: t.slice(5).trim(), bold: true, font: FONT, size: 19 })],
    }));
    continue;
  }
  if (t.startsWith("COV:")) {
    // Linha de cobertura (pequena, recuada, com rótulo em negrito via **)
    children.push(new Paragraph({
      alignment: AlignmentType.JUSTIFIED,
      spacing: { line: 240, lineRule: "auto", before: 0, after: 30 },
      indent: { left: 340 },
      children: runs(t.slice(4).trim(), { size: 19 }),
    }));
    continue;
  }
  if (t.startsWith("### ")) {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_3,
      alignment: AlignmentType.LEFT,
      spacing: { line: LINE, lineRule: "auto", before: 180, after: 60 },
      children: [new TextRun({ text: t.slice(4).trim(), bold: true, font: FONT, size: SIZE })],
    }));
    continue;
  }
  if (t.startsWith("## ")) {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_2,
      alignment: AlignmentType.LEFT,
      spacing: { line: LINE, lineRule: "auto", before: 240, after: 60 },
      children: [new TextRun({ text: t.slice(3).trim(), bold: true, italics: true, font: FONT, size: SIZE })],
    }));
    continue;
  }
  if (t.startsWith("# ")) {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_1,
      alignment: AlignmentType.LEFT,
      spacing: { line: LINE, lineRule: "auto", before: 300, after: 120 },
      children: [new TextRun({ text: t.slice(2).trim(), bold: true, font: FONT, size: SIZE })],
    }));
    continue;
  }
  if (t.startsWith("* ")) {
    children.push(new Paragraph({
      numbering: { reference: "bullets", level: 0 },
      alignment: AlignmentType.JUSTIFIED,
      spacing: { line: LINE, lineRule: "auto", before: 0, after: 0 },
      children: runs(t.slice(2).trim()),
    }));
    continue;
  }
  if (t.startsWith("> ")) {
    children.push(new Paragraph({
      alignment: AlignmentType.JUSTIFIED,
      spacing: { line: 276, lineRule: "auto", before: 60, after: 60 },
      indent: { left: 2268 }, // 4 cm recuo de citação longa (ABNT)
      children: [new TextRun({ text: t.slice(2).trim(), font: FONT, size: 20 })],
    }));
    continue;
  }
  if (t === "---") {
    children.push(new Paragraph({
      border: { bottom: { color: "999999", space: 1, style: BorderStyle.SINGLE, size: 6 } },
      spacing: { before: 60, after: 60 },
      children: [new TextRun({ text: "", font: FONT, size: SIZE })],
    }));
    continue;
  }
  children.push(body(t));
}

const doc = new Document({
  creator: "Documento gerado",
  title: outPath,
  styles: {
    default: { document: { run: { font: FONT, size: SIZE } } },
  },
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } },
      }],
    }],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4
        margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN },
      },
    },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outPath, buf);
  console.log("Wrote", outPath, `(${buf.length} bytes, font=${FONT})`);
});
