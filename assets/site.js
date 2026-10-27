// 12MAG study site — shared behaviour
(function () {
  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  window.SiteStore = store;

  /* ---------- home tabs ---------- */
  const tabs = document.querySelectorAll('.tab');
  if (tabs.length) {
    const show = (id) => {
      tabs.forEach(t => t.setAttribute('aria-selected', t.dataset.panel === id));
      document.querySelectorAll('.panel').forEach(p => p.hidden = p.id !== id);
      store.set('12mag-tab', id);
    };
    tabs.forEach(t => t.addEventListener('click', () => show(t.dataset.panel)));
    const hash = location.hash.slice(1);
    show(document.getElementById(hash) ? hash : store.get('12mag-tab', tabs[0].dataset.panel));
    // progress badges on cards
    document.querySelectorAll('a.card[data-lesson]').forEach(c => {
      const p = store.get('12mag-' + c.dataset.lesson, null);
      const st = c.querySelector('.st');
      if (p && st && p.done) st.textContent = p.done.length + ' of 5 sections done';
    });
  }

  /* ---------- lesson steps ---------- */
  const lesson = document.querySelector('[data-lesson-id]');
  if (lesson) {
    const key = '12mag-' + lesson.dataset.lessonId;
    const secs = [...document.querySelectorAll('.sec')];
    const btns = [...document.querySelectorAll('.steps button')];
    const state = store.get(key, { done: [], at: secs[0].id });
    const save = () => store.set(key, state);
    const paint = () => {
      btns.forEach(b => {
        b.parentElement.classList.toggle('done', state.done.includes(b.dataset.go));
        b.toggleAttribute('aria-current', false);
        if (b.dataset.go === state.at) b.setAttribute('aria-current', 'step');
      });
      const pct = Math.round(100 * state.done.length / secs.length);
      const bar = document.querySelector('.bar i'); if (bar) bar.style.width = pct + '%';
      const lab = document.querySelector('.progress span'); if (lab) lab.textContent = state.done.length + ' of ' + secs.length + ' sections done';
    };
    const go = (id, scroll = true) => {
      if (!document.getElementById(id)) id = secs[0].id;
      secs.forEach(s => s.hidden = s.id !== id);
      state.at = id; save(); paint();
      if (scroll) window.scrollTo({ top: 0, behavior: 'smooth' });
    };
    window.goStep = go;
    btns.forEach(b => b.addEventListener('click', () => go(b.dataset.go)));
    secs.forEach((s, i) => {
      const nx = s.querySelector('[data-next]');
      if (nx) nx.addEventListener('click', () => {
        if (!state.done.includes(s.id)) state.done.push(s.id);
        go(secs[Math.min(i + 1, secs.length - 1)].id);
      });
      const pv = s.querySelector('[data-prev]');
      if (pv) pv.addEventListener('click', () => go(secs[Math.max(i - 1, 0)].id));
    });
    go(location.hash.slice(1) || state.at, false);
  }

  /* ---------- multiple choice ---------- */
  document.querySelectorAll('.q[data-answer]').forEach(q => {
    const ans = q.dataset.answer;
    const opts = q.querySelectorAll('.opt');
    const fb = q.querySelector('.after');
    opts.forEach(o => o.addEventListener('click', () => {
      const right = o.dataset.k === ans;
      opts.forEach(x => { x.disabled = true; if (x.dataset.k === ans) x.classList.add('is-answer'); });
      o.classList.add(right ? 'picked-right' : 'picked-wrong');
      const v = q.querySelector('.verdict');
      v.className = 'verdict ' + (right ? 'good' : 'bad');
      v.innerHTML = right ? '<b>Correct.</b> The answer is ' + ans + '.' : '<b>Not quite.</b> You chose ' + o.dataset.k + '. The answer is ' + ans + '.';
      fb.hidden = false;
      const r = q.querySelector('.retry'); if (r) r.hidden = false;
    }));
    const r = q.querySelector('.retry');
    if (r) r.addEventListener('click', () => {
      opts.forEach(x => { x.disabled = false; x.className = 'opt'; });
      fb.hidden = true; r.hidden = true;
    });
  });

  /* ---------- typed answers ---------- */
  document.querySelectorAll('.q[data-accept]').forEach(q => {
    const accept = q.dataset.accept.split('|').map(s => s.trim().toLowerCase());
    const inp = q.querySelector('input');
    const fb = q.querySelector('.after');
    const check = () => {
      const val = inp.value.trim().toLowerCase().replace(/[.\s]+$/, '');
      if (!val) return;
      const right = accept.some(a => val === a || val.includes(a));
      const v = q.querySelector('.verdict');
      v.className = 'verdict ' + (right ? 'good' : 'bad');
      v.innerHTML = right ? '<b>Correct.</b>' : '<b>Not quite.</b> Check the solution below, then try again.';
      fb.hidden = false;
    };
    q.querySelector('.check').addEventListener('click', check);
    inp.addEventListener('keydown', e => { if (e.key === 'Enter') check(); });
  });

  /* ---------- sorter ---------- */
  const sorter = document.querySelector('.sorter');
  if (sorter) {
    const types = ['Nominal', 'Ordinal', 'Discrete', 'Continuous'];
    const items = [...sorter.querySelectorAll('.item')];
    const score = document.querySelector('.score');
    const upd = () => {
      const right = items.filter(i => i.classList.contains('right')).length;
      score.textContent = right + ' / ' + items.length + ' correct';
    };
    items.forEach(it => {
      const box = document.createElement('div'); box.className = 'choices';
      types.forEach(t => {
        const b = document.createElement('button'); b.className = 'choice'; b.textContent = t; b.type = 'button';
        b.addEventListener('click', () => {
          const ok = t === it.dataset.type;
          it.classList.toggle('right', ok); it.classList.toggle('wrong', !ok);
          let f = it.querySelector('.fb');
          if (!f) { f = document.createElement('div'); f.className = 'fb'; it.appendChild(f); }
          f.innerHTML = (ok ? '✓ ' : '✗ Try again. ') + (ok ? it.dataset.why : 'Hint: ' + it.dataset.hint);
          upd();
        });
        box.appendChild(b);
      });
      it.insertBefore(box, it.querySelector('.fb'));
    });
    upd();
  }

  /* ---------- print ---------- */
  document.querySelectorAll('[data-print]').forEach(b => b.addEventListener('click', () => {
    const mode = b.dataset.print;
    document.querySelectorAll('.sheet').forEach(sh => { if (mode) { sh.classList.toggle('bw', mode === 'bw'); sh.classList.toggle('colour', mode !== 'bw'); } });
    window.print();
  }));
  // preview toggle: hovering/focusing a print button shows that version
  document.querySelectorAll('[data-print]').forEach(b => ['mouseenter','focus'].forEach(ev => b.addEventListener(ev, () => {
    document.querySelectorAll('.sheet').forEach(sh => { sh.classList.toggle('bw', b.dataset.print === 'bw'); sh.classList.toggle('colour', b.dataset.print !== 'bw'); });
  })));
})();
