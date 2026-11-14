"""Make tools/deck/engine.html: the slide engine (CSS, charts, boxplots, reveal engine) with no slides, plus <!--SLIDES--> marker.
Built from S3's deck + the S4 boxplot code (s4/build_v1.py). Re-run after changing s4/extra.js or s4/extra.css."""
import os, subprocess, re
H=os.path.dirname(os.path.abspath(__file__))
subprocess.run(['python3',f'{H}/s4/build_v1.py'],check=True,env=dict(os.environ,S4OUT='/tmp/_s4_engine.html'),stdout=subprocess.DEVNULL)
h=open('/tmp/_s4_engine.html',encoding='utf-8').read()
j=h.find('<section'); k=h.rfind('</section>')+len('</section>')
open(f'{H}/engine.html','w',encoding='utf-8').write(h[:j]+'<!--SLIDES-->'+h[k:])
print('engine.html written')
