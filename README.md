# PE1HVH 

Amateur radio operator · Open-source developer 

[![Website](https://img.shields.io/badge/website-pe1hvh.nl-blue?style=flat-square)](https://www.pe1hvh.nl)
[![Website](https://img.shields.io/badge/website-domca.nl-blue?style=flat-square)](https://www.domca.nl)
[![License](https://img.shields.io/badge/projects-open--source-green?style=flat-square)](#)

---

## About me
Focused on open-source tooling for the amateur radio community — from LoRa/MeshCore mesh networks to HF monitoring and CW interfaces.

Active in **NoodNet Zwolle** (emergency communications) and **DOMCA** (Dutch Open MeshCore Activity).

---

## Public repositories

<!-- REPOS_START -->
<!-- 14 repos — auto-updated by GitHub Actions -->

<img src="cards/header-meshcore.svg" width="812"/>

<ol style="display:flex;flex-wrap:wrap;list-style:none;padding:0;margin:4px 0 16px 0;gap:8px;">
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/meshcore-observer" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">meshcore-observer</a></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">A standalone daemon that reads JSON archive files produced by meshcore_gui and meshcore_bridge, aggregates them from all sources, and presents a unified live dashboard. It never connects to a device and never writes to the archive — it only watches and displays</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#3572A5;display:inline-block;flex-shrink:0;"></span><span>Python</span></span></p>
</div></li>
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/meshcore-bridge" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">meshcore-bridge</a></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">MeshCore Channel Bridge — selectively relays messages between channels across independent MeshCore networks</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#3572A5;display:inline-block;flex-shrink:0;"></span><span>Python</span></span></p>
</div></li>
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/meshcore-gui" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">meshcore-gui</a></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">Native desktop GUI for MeshCore mesh network devices via BLE — no firmware changes required</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#3572A5;display:inline-block;flex-shrink:0;"></span><span>Python</span></span><span style="display:inline-flex;align-items:center;gap:3px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.873 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/></svg>13</span><span style="display:inline-flex;align-items:center;gap:3px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878z"/></svg>1</span></p>
</div></li>
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/meshcore-ble-connect" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">meshcore-ble-connect</a></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">Standalone BLE Connection Manager — ensures a BLE bond is established via D-Bus before your application starts.</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#3572A5;display:inline-block;flex-shrink:0;"></span><span>Python</span></span></p>
</div></li>
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878z"/></svg><a href="https://github.com/pe1hvh/meshcore_py" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">meshcore_py</a><span style="font-size:11px;padding:1px 7px;border:1px solid var(--color-border-default,#d0d7de);border-radius:10px;color:var(--color-fg-muted,#57606a);">fork</span></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">Python bindings for meshcore</p>

</div></li>
</ol>


<img src="cards/header-morse-en-cw.svg" width="812"/>

<ol style="display:flex;flex-wrap:wrap;list-style:none;padding:0;margin:4px 0 16px 0;gap:8px;">
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/configurable_morse_code_interface" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">configurable_morse_code_interface</a></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">DIY Configurable USB/HID Morse Code Interface for LWCO, PCWFistcheck, VBand etc.</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#f34b7d;display:inline-block;flex-shrink:0;"></span><span>C++</span></span><span style="display:inline-flex;align-items:center;gap:3px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.873 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/></svg>2</span><span style="display:inline-flex;align-items:center;gap:3px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878z"/></svg>3</span></p>
</div></li>
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/VBand_interface" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">VBand_interface</a></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">VBand Interface for the Seeeduino XIAO</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#f34b7d;display:inline-block;flex-shrink:0;"></span><span>C++</span></span></p>
</div></li>
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/cw_lcwo_pcw_interface" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">cw_lcwo_pcw_interface</a></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">CW interface for using it with Learn CW online and PCWFistCheck</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#f34b7d;display:inline-block;flex-shrink:0;"></span><span>C++</span></span></p>
</div></li>
</ol>


<img src="cards/header-arduino.svg" width="812"/>

<ol style="display:flex;flex-wrap:wrap;list-style:none;padding:0;margin:4px 0 16px 0;gap:8px;">
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/frequency-generator" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">frequency-generator</a></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">10kHz to 225MHz VFO / RF Generator</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#555555;display:inline-block;flex-shrink:0;"></span><span>C</span></span><span style="display:inline-flex;align-items:center;gap:3px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.873 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/></svg>1</span></p>
</div></li>
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/platformIO2arduinoIDE" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">platformIO2arduinoIDE</a></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">Convert PlatformIO code to Arduino sketches</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#89e051;display:inline-block;flex-shrink:0;"></span><span>Shell</span></span><span style="display:inline-flex;align-items:center;gap:3px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.873 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/></svg>1</span></p>
</div></li>
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/measure_bouncing" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">measure_bouncing</a></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">Simple test program for measure bouncing</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#f34b7d;display:inline-block;flex-shrink:0;"></span><span>C++</span></span></p>
</div></li>
</ol>


<img src="cards/header-google-timeline.svg" width="812"/>

<ol style="display:flex;flex-wrap:wrap;list-style:none;padding:0;margin:4px 0 16px 0;gap:8px;">
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878z"/></svg><a href="https://github.com/pe1hvh/Timeline-GPX-Exporter" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">Timeline-GPX-Exporter</a><span style="font-size:11px;padding:1px 7px;border:1px solid var(--color-border-default,#d0d7de);border-radius:10px;color:var(--color-fg-muted,#57606a);">fork</span></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">Convert Google timeline new JSON format to daily GPX files</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#3572A5;display:inline-block;flex-shrink:0;"></span><span>Python</span></span></p>
</div></li>
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/TimeLine2MariaDB" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">TimeLine2MariaDB</a></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">Tijdlijn van Google Android telefoon omzetten naar MariaDB</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#3572A5;display:inline-block;flex-shrink:0;"></span><span>Python</span></span></p>
</div></li>
</ol>


<img src="cards/header-other.svg" width="812"/>

<ol style="display:flex;flex-wrap:wrap;list-style:none;padding:0;margin:4px 0 16px 0;gap:8px;">
<li style="flex:1 1 calc(50% - 4px);min-width:250px;box-sizing:border-box;">
<div style="border:1px solid var(--color-border-default,#d0d7de);border-radius:6px;padding:16px;height:100%;background:var(--color-canvas-default,#ffffff);">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="fill:var(--color-fg-muted,#57606a);flex-shrink:0;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/javaPolar" style="font-weight:600;font-size:14px;color:var(--color-accent-fg,#0969da);text-decoration:none;">javaPolar</a></div>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0 0 12px 0;">Automates Polar Flow training data export and upload using Selenium WebDriver.</p>
<p style="font-size:12px;color:var(--color-fg-muted,#57606a);margin:0;display:flex;gap:12px;flex-wrap:wrap;"><span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;border-radius:50%;background:#8f8f8f;display:inline-block;flex-shrink:0;"></span><span>Java</span></span></p>
</div></li>
</ol>

<!-- REPOS_END -->

---

## Interests

`MeshCore / LoRa` &nbsp;·&nbsp; `BLE / BlueZ` &nbsp;·&nbsp; `HF amateur radio` &nbsp;·&nbsp; `CW / Morse` &nbsp;·&nbsp; `ESP32 / Arduino` &nbsp;·&nbsp; `Python` &nbsp;·&nbsp; `PHP` &nbsp;·&nbsp; `NoodNet`
