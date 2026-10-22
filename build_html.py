#!/usr/bin/env python3
f = open("pavillon_viewer.html", "w")
f.write("<!DOCTYPE html>
<html lang=de>
<head>
<meta charset=UTF-8>
")
f.write("<meta name=viewport content=\"width=device-width,initial-scale=1.0\">
")
f.write("<title>Pavillon 3D - Embodied Carbon</title>
<style>
")
f.write("*{margin:0;padding:0;box-sizing:border-box}body{font-family:Segoe UI,Roboto,sans-serif;overflow:hidden;background:#f0f2f5;color:#111}#c{width:100vw;height:100vh;position:relative}
")
f.write("#p{position:absolute;top:16px;left:16px;z-index:100;background:#fff;border-radius:14px;padding:18px;box-shadow:0 4px 24px rgba(0,0,0,.10);min-width:260px;border:1px solid #e4e7eb}
")
f.write("<div id=p>
<h2>Pavillon 3D - Embodied Carbon</h2>
")
f.write("#lg .t{font-size:11px;color:#6b7280;margin-bottom:5px;font-weight:600}
")
f.write("#st .r{display:flex;justify-content:space-between;margin:3px 0}#st .l{color:#6b7280}#st .v{color:#111;font-weight:700}
")
f.write("#lg .lb{display:flex;justify-content:space-between;font-size:10px;color:#9ca3af}
</style>
</head>
<body>
<div id=c>
")
f.write("#lg .bar{width:180px;height:14px;border-radius:3px;background:linear-gradient(90deg,#22c55e,#facc15,#ef4444);margin:5px 0;border:1px solid #e5e7eb}
")
f.write("<div><label>Material</label><select id=mg><option value=standard>Standard (Hochofen/Normbeton)</option><option value=alternative>Alternativ (EAF/EcoPact)</option></select></div>
")
f.write("#st{position:absolute;bottom:24px;left:16px;z-index:100;background:#fff;border-radius:14px;padding:14px;box-shadow:0 4px 24px rgba(0,0,0,.10);border:1px solid #e4e7eb;font-size:12px}
")
f.write("#p h2{font-size:15px;margin-bottom:14px;color:#111;font-weight:600}#p div{margin-bottom:10px}#p label{display:block;font-size:10px;color:#666;margin-bottom:3px;text-transform:uppercase;font-weight:600}
")
f.write("#lg{position:absolute;bottom:24px;right:16px;z-index:100;background:#fff;border-radius:14px;padding:14px;box-shadow:0 4px 24px rgba(0,0,0,.10);border:1px solid #e4e7eb}
")
f.write(".br{display:flex;gap:6px}.br span{flex:1;text-align:center;padding:7px;border-radius:7px;font-size:11px;font-weight:600;cursor:pointer;background:#e5e7eb;color:#374151}.br span.on{background:#3b82f6;color:#fff}
")
f.write("#p select{width:100%;padding:7px 10px;border-radius:7px;border:1px solid #d1d5db;background:#f9fafb;color:#111;font-size:13px;cursor:pointer;outline:none}#p select:focus{border-color:#3b82f6;box-shadow:0 0 0 2px rgba(59,130,246,.15)}
")
f.write("try{
var c=document.getElementById(\"c\");
")
f.write("<div class=br><span id=bCO2 class=on>CO2 Farbe</span><span id=bMat>Material Farbe</span></div>
")
f.write("<div class=r><span class=l>Alternativ:</span><span class=v id=aCO2>-</span></div>
")
f.write("<div class=r><span class=l>Standard:</span><span class=v id=sCO2>-</span></div>
")
f.write("<div id=st>
<div class=r><span class=l>Gesamt CO2:</span><span class=v id=tCO2>-</span></div>
")
f.write("<script>
var DATA = " + json.dumps(m, separators=(",",":")) + ";
")
f.write("<div class=r><span class=l>Einsparung:</span><span class=v id=dCO2>-</span></div></div></div>
")
f.write("<div style=font-size:9px;color:#9ca3af;margin-top:10px>Maus: Drehen / Scroll: Zoomen / Rechts: Verschieben</div></div>
")
f.write("else{
var s=new THREE.Scene();s.background=new THREE.Color(0xf0f2f5);
")
f.write("s.add(new THREE.HemisphereLight(0xffffff,0x8899bb,0.5));
")
f.write("gr.rotation.x=-Math.PI/2;gr.position.y=-0.02;s.add(gr);
")
f.write("var cam=new THREE.PerspectiveCamera(45,innerWidth/innerHeight,0.01,1000);cam.position.set(35,25,40);
")
f.write("s.add(new THREE.DirectionalLight(0x4488ff,0.3).position.set(-25,10,-15));
")
f.write("if(typeof THREE===undefined){c.innerHTML=\"<div style=color:red;padding:40px>THREE.js nicht geladen (Internet?)</div>\"}
")
f.write("<div id=lg><div class=t>CO2-Emission (kg CO2e)</div><div class=bar></div><div class=lb><span id=mnLb>0</span><span id=mxLb>max</span></div></div>
")
f.write("var r=new THREE.WebGLRenderer({antialias:true});r.setSize(innerWidth,innerHeight);r.setPixelRatio(Math.min(devicePixelRatio,2));
")
f.write("r.shadowMap.enabled=true;r.toneMapping=THREE.ACESFilmicToneMapping;r.toneMappingExposure=1.0;c.appendChild(r.domElement);
")
f.write("var o=new THREE.OrbitControls(cam,r.domElement);o.enableDamping=true;o.dampingFactor=.08;o.target.set(8,-5,3);o.update();
")
f.write("var su=new THREE.DirectionalLight(0xfff4e6,1.2);su.position.set(25,35,15);su.castShadow=true;su.shadow.mapSize.set(2048,2048);s.add(su);
")
f.write("var gr=new THREE.Mesh(new THREE.PlaneGeometry(100,60),new THREE.MeshStandardMaterial({color:0xf6f8fa,roughness:0.95}));
")
f.write("<div><label>Lebenszyklus</label><select id=lc><option value=A1A3>A1-A3 (Herstellung)</option><option value=C>C (End-of-Life)</option><option value=D>D (Wiederverwertung)</option></select></div>
")
f.write("var mn=1e99,mx=-1e99;
")
f.write("for(var i=0;i<DATA.length;i++){
")
f.write("var vv=new Float32Array([].concat.apply([],m.verts));
")
f.write("s.add(new THREE.GridHelper(80,40,0xc3ccd6,0xd9dfe6));
")
f.write("var gp=new THREE.Group();s.add(gp);var sT=0,aT=0;
")
f.write("function cv(v){var t=Math.max(0,Math.min(1,(v-mn)/(mx-mn)));return t<0.5?new THREE.Color(t*2,1,0):new THREE.Color(1,2-2*t,0);}
")
f.write("var g=new THREE.BufferGeometry();g.setAttribute(\"position\",new THREE.BufferAttribute(vv,3));g.setIndex(ff);g.computeVertexNormals();
")
f.write("var m=DATA[i];var ff=[];for(var j=0;j<m.faces.length;j++){var f=m.faces[j];ff.push(f[0],f[1],f[2]);if(f.length>3)ff.push(f[0],f[2],f[3]);}
")
f.write("function mc(l){if(l.indexOf(\"Rectangle\")>=0)return 0x9aa5b1;if(l.indexOf(\"RO 139\")>=0)return 0x8b93a1;if(l.indexOf(\"RD\")>=0)return 0x7c8592;return 0x8aa8d8;}
")
f.write("for(var i=0;i<DATA.length;i++){var d=DATA[i];[\"co2_std\",\"co2_alt\",\"co2_c\",\"co2_d\"].forEach(function(k){var v=d[k];if(v!==undefined){if(v<mn)mn=v;if(v>mx)mx=v;}});}
")
f.write("var sc=true;
")
f.write("function ud(){
")
f.write("var t=mg===\"standard\"?sT:aT;
")
f.close()
f.write("var mg=document.getElementById(\"mg\").value;var lc=document.getElementById(\"lc\").value;
")
f.write("var mt=new THREE.MeshPhysicalMaterial({color:mc(m.layer),metalness:.12,roughness:.5,clearcoat:.08});
")
f.write("</script>
")
f.write("var gy=0;gp.children.forEach(function(ch){var bb=new THREE.Box3().setFromObject(ch);if(bb.min.y<gy)gy=bb.min.y;});gp.position.y-=gy;
")
f.write("</body>
</html>
")
f.write("document.getElementById(\"tCO2\").textContent=t.toFixed(1)+\" kg\";
")
print("Members:", len(m))
f.write("var me=new THREE.Mesh(g,mt);me.castShadow=true;me.receiveShadow=true;me.userData=m;me.userData.mc=mc(m.layer);gp.add(me);sT+=m.co2_std||0;aT+=m.co2_alt||0;}
")
f.write("document.getElementById(\"aCO2\").textContent=aT.toFixed(1)+\" kg\";
")
sz = os.path.getsize("pavillon_viewer.html")
f.write("document.getElementById(\"mxLb\").textContent=mx.toFixed(1);
}")
f.write("document.getElementById(\"sCO2\").textContent=sT.toFixed(1)+\" kg\";
")
print(f"Written {sz} bytes ({sz/1024/1024:.2f} MB)")
f.write("gp.children.forEach(function(me){var u=me.userData;me.material.color.copy(sc?cv(u[k]||0):new THREE.Color(u.mc));});
")
f.write("var k=lc===\"A1A3\"?\"co2_\"+(mg===\"standard\"?\"std\":\"alt\"):\"co2_\"+lc.toLowerCase();
")
f.write("document.getElementById(\"mg\").onchange=ud;document.getElementById(\"lc\").onchange=ud;
")
f.write("document.getElementById(\"dCO2\").textContent=(sT-aT).toFixed(1)+\" kg (\"+((sT-aT)/sT*100).toFixed(1)+\"%)\";
")
f.write("function an(){requestAnimationFrame(an);o.update();r.render(s,cam);}an();ud();}}
")
f.write("<script src=https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js></script>
")
f.write("<script src=https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js></script>
")
f.write("}catch(e){document.getElementById(\"c\").innerHTML=\"<div style=color:red;padding:40px>ERROR: \"+e.message+\"</div>\";}
")
f.write("window.onresize=function(){cam.aspect=innerWidth/innerHeight;cam.updateProjectionMatrix();r.setSize(innerWidth,innerHeight);};

")
f.write("document.getElementById(\"bCO2\").onclick=function(){sc=true;document.querySelector(\".br .on\").className=\"";this.className=\"on\";ud();};
")
f.write("document.getElementById(\"bMat\").onclick=function(){sc=false;document.querySelector(\".br .on\").className=\"";this.className=\"on\";ud();};
")
f.write("if(document.readyState.startsWith(\"c\")||document.readyState===\"interactive\")new Function(document.querySelector(\"script\").textContent)();else window.onload=function(){try{new Function(document.querySelector(\"script\").textContent)()}catch(e){}};
")
