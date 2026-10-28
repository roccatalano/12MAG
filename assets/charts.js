// 12MAG chart renderer: uniform scales, baseline and axis labels on every chart.
// <svg data-chart='{"type":"bar"|"seg", ...}'></svg>
(function () {
  const NS = 'http://www.w3.org/2000/svg';
  const FILLS = ['#00838F', '#9fd3d8', '#e3f3f4', '#4fb3bb', '#cfe9ec'];
  const SHEET = ['c1', 'c2', 'c3', 'c4', 'c5'];
  function render(svg, s) {
    const sheet = !!s.sheet, W = 420, H = 260;
    const L = 64, B = 210, T = 18;          // plot left, baseline y, top y
    const ink = sheet ? '#000' : '#1d2328', mute = sheet ? '#000' : '#5f6b75', grid = sheet ? '#bbb' : '#e3e7ea';
    let o = `<g font-family="Inter,Arial,sans-serif" font-size="12">`;
    const max = s.type === 'seg' ? 100 : s.max, step = s.type === 'seg' ? 10 : (s.step || 1);
    const y = v => B - (v / max) * (B - T);
    const R = s.type === 'seg' ? 250 : W - 16;  // plot right edge
    // gridlines + uniform ticks
    for (let v = 0; v <= max + 1e-9; v += step) {
      const yy = y(v).toFixed(1);
      if (v > 0) o += `<line x1="${L}" x2="${R}" y1="${yy}" y2="${yy}" stroke="${grid}" stroke-width="1"/>`;
      o += `<line x1="${L - 5}" x2="${L}" y1="${yy}" y2="${yy}" stroke="${ink}"/>`;
      o += `<text x="${L - 9}" y="${(+yy + 4).toFixed(1)}" text-anchor="end" fill="${mute}">${v}</text>`;
    }
    const fillAttr = i => sheet ? `class="${SHEET[i % 5]}"` : `fill="${FILLS[i % 5]}"`;
    if (s.type === 'bar') {
      const n = s.cats.length, slot = (R - L) / n, bw = Math.min(80, slot * 0.55);
      s.cats.forEach((c, i) => {
        const cx = L + slot * (i + 0.5), v = s.vals[i];
        o += `<rect ${sheet ? 'class="c1"' : 'fill="#00838F"'} x="${(cx - bw / 2).toFixed(1)}" y="${y(v).toFixed(1)}" width="${bw.toFixed(1)}" height="${(B - y(v)).toFixed(1)}" stroke="${sheet ? '#000' : 'none'}"/>`;
        o += `<text x="${cx.toFixed(1)}" y="${B + 16}" text-anchor="middle" fill="${ink}">${c}</text>`;
      });
    } else if (s.type === 'hist') {
      // histogram: touching bars. s.edges = interval boundaries (labels on edges),
      // or s.cats = one label per bar (discrete values, labels centred). s.hl = optional highlight flags.
      const n = s.vals.length, bw = (R - L - 8) / n, x0 = L + 4;
      s.vals.forEach((v, i) => {
        const on = !s.hl || s.hl[i];
        const f = sheet ? `class="${on ? 'c1' : 'c3'}"` : `fill="${on ? '#00838F' : '#cfe9ec'}"`;
        if (v > 0) o += `<rect ${f} x="${(x0 + i * bw).toFixed(1)}" y="${y(v).toFixed(1)}" width="${bw.toFixed(1)}" height="${(B - y(v)).toFixed(1)}" stroke="${sheet ? '#000' : '#fff'}" stroke-width="1"/>`;
      });
      const every = s.every || 1;
      if (s.cats) s.cats.forEach((c, i) => { o += `<text x="${(x0 + (i + 0.5) * bw).toFixed(1)}" y="${B + 16}" text-anchor="middle" fill="${ink}">${c}</text>`; });
      else s.edges.forEach((e, i) => {
        const xx = (x0 + i * bw).toFixed(1);
        o += `<line x1="${xx}" x2="${xx}" y1="${B}" y2="${B + 4}" stroke="${ink}"/>`;
        if (i % every === 0) o += `<text x="${xx}" y="${B + 17}" text-anchor="middle" fill="${ink}" font-size="${s.fs || 12}">${e}</text>`;
      });
    } else {
      const bx = L + 50, bw = 110; let acc = 0;
      s.cats.forEach((c, i) => {
        const v = s.vals[i], y0 = y(acc), y1 = y(acc + v); acc += v;
        o += `<rect ${fillAttr(i)} x="${bx}" y="${y1.toFixed(1)}" width="${bw}" height="${(y0 - y1).toFixed(1)}" stroke="${ink}" stroke-width="1"/>`;
        if (s.inlabels !== false && v >= 12) o += `<text x="${bx + bw / 2}" y="${((y0 + y1) / 2 + 4).toFixed(1)}" text-anchor="middle" font-weight="600" fill="${i === 0 && !sheet ? '#fff' : ink}">${c} ${v}%</text>`;
      });
      s._xl = bx + bw / 2;
      // key (top category first, as it appears in the bar)
      const kx = R + 22; o += `<text x="${kx}" y="${T + 10}" font-weight="600" fill="${ink}">Key</text>`;
      s.cats.slice().reverse().forEach((c, j) => {
        const i = s.cats.length - 1 - j, ky = T + 22 + j * 22;
        o += `<rect ${fillAttr(i)} x="${kx}" y="${ky}" width="14" height="14" stroke="${ink}" stroke-width="1"/><text x="${kx + 20}" y="${ky + 12}" fill="${ink}">${c}</text>`;
      });
    }
    // axes: y-axis line and baseline (x-axis) on every chart
    o += `<line x1="${L}" x2="${L}" y1="${T - 4}" y2="${B}" stroke="${ink}" stroke-width="1.5"/>`;
    o += `<line x1="${L}" x2="${R}" y1="${B}" y2="${B}" stroke="${ink}" stroke-width="1.5"/>`;
    o += `<text x="${s._xl || (L + R) / 2}" y="${s._xl ? B + 22 : B + 36}" text-anchor="middle" font-weight="600" fill="${ink}">${s.xlabel}</text>`;
    o += `<text x="16" y="${(T + B) / 2}" transform="rotate(-90 16 ${(T + B) / 2})" text-anchor="middle" font-weight="600" fill="${ink}">${s.ylabel || (s.type === 'seg' ? 'percentage (%)' : 'number')}</text>`;
    svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
    svg.innerHTML = o + '</g>';
  }
  window.drawChart = render;
  document.querySelectorAll('svg[data-chart]').forEach(el => render(el, JSON.parse(el.dataset.chart)));
})();
