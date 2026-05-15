import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(scriptDir, '..');
const exerciseOpenTagPattern = /<Exercise\b[\s\S]*?>/g;
const headingPattern = /^\s{0,3}#{2,6}\s+\S/;

const skippedDirectories = new Set([
  '.git',
  '.mwt',
  'agent-rules-private',
  'node_modules',
]);

const toDisplayPath = (filePath) => path.relative(repoRoot, filePath).split(path.sep).join('/');

const listMdxFiles = (dirPath) => {
  const entries = fs.readdirSync(dirPath, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    if (entry.isDirectory()) {
      if (skippedDirectories.has(entry.name)) continue;
      files.push(...listMdxFiles(path.join(dirPath, entry.name)));
      continue;
    }

    if (entry.isFile() && entry.name.endsWith('.mdx')) {
      files.push(path.join(dirPath, entry.name));
    }
  }

  return files;
};

const lineNumberAt = (source, index) => source.slice(0, index).split(/\r?\n/).length;

const previousNonBlankLine = (lines, startIndex) => {
  for (let index = startIndex; index >= 0; index -= 1) {
    if (lines[index].trim() !== '') return { line: lines[index], index };
  }

  return null;
};

const validateExerciseTags = (filePath) => {
  const source = fs.readFileSync(filePath, 'utf8');
  const lines = source.split(/\r?\n/);
  const errors = [];

  for (const match of source.matchAll(exerciseOpenTagPattern)) {
    const [tag] = match;
    const tagLineNumber = lineNumberAt(source, match.index);
    const tagLineIndex = tagLineNumber - 1;
    const previousLine = previousNonBlankLine(lines, tagLineIndex - 1);

    if (/\btitle\s*=/.test(tag)) {
      errors.push(`${toDisplayPath(filePath)}:${tagLineNumber} <Exercise> must not use a title prop.`);
    }

    if (!previousLine || !headingPattern.test(previousLine.line)) {
      errors.push(
        `${toDisplayPath(filePath)}:${tagLineNumber} <Exercise> must be immediately preceded by a non-empty Markdown heading (## through ######), allowing only blank lines between them.`,
      );
    }
  }

  return errors;
};

const errors = listMdxFiles(repoRoot).flatMap(validateExerciseTags);

if (errors.length > 0) {
  console.error('Exercise heading verification failed:');
  for (const error of errors) {
    console.error(`- ${error}`);
  }
  process.exit(1);
}

console.log('Exercise heading verification passed.');
