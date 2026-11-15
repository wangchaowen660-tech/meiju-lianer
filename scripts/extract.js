const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

function extract(name, isObject) {
    const re = new RegExp('const ' + name + '\\s*=\\s*(' + (isObject ? '\\{' : '\\[') + '[\\s\\S]*?' + (isObject ? '\\}' : '\\]') + ');');
    const m = html.match(re);
    if (!m) {
        console.error('❌ 没找到 ' + name);
        return null;
    }
    try {
        return eval('(' + m[1] + ')');
    } catch (e) {
        console.error('❌ 解析 ' + name + ' 失败:', e.message);
        return null;
    }
}

const PATTERNS = extract('PATTERNS', false);
const WORD_FAMILIES = extract('WORD_FAMILIES', false);
const IPA_48 = extract('IPA_48', true);

if (!PATTERNS || !WORD_FAMILIES) {
    process.exit(1);
}

const data = { PATTERNS, WORD_FAMILIES, IPA_48 };
fs.writeFileSync('data.json', JSON.stringify(data, null, 2));

let total = 0;
PATTERNS.forEach(p => total += 1 + p.chunks.length * 2);
WORD_FAMILIES.forEach(f => total += 1 + f.w.length);
console.log('✅ 母句:', PATTERNS.length);
console.log('✅ 词族:', WORD_FAMILIES.length);
console.log('📊 预计生成音频数量:', total);