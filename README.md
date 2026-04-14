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

<div style="overflow:hidden;margin-bottom:8px;">
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/meshcore-observer" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">meshcore-observer</a></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">A standalone daemon that reads JSON archive files produced by meshcore_gui and meshcore_bridge, aggregates them from all sources, and presents a unified live dashboard. It never connects to a device and never writes to the archive — it only watches and displays</p>
<p style="margin:0;"><span style="color:#3572A5;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">Python</span></p>
</div>
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/meshcore-bridge" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">meshcore-bridge</a></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">MeshCore Channel Bridge — selectively relays messages between channels across independent MeshCore networks</p>
<p style="margin:0;"><span style="color:#3572A5;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">Python</span></p>
</div>
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/meshcore-gui" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">meshcore-gui</a></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">Native desktop GUI for MeshCore mesh network devices via BLE — no firmware changes required</p>
<p style="margin:0;"><span style="color:#3572A5;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">Python</span><svg height="14" viewBox="0 0 16 16" width="14" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.873 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/></svg><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">13</span><svg height="14" viewBox="0 0 16 16" width="14" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878z"/></svg><span style="font-size:12px;color:#57606a;vertical-align:middle;">1</span></p>
</div>
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/meshcore-ble-connect" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">meshcore-ble-connect</a></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">Standalone BLE Connection Manager — ensures a BLE bond is established via D-Bus before your application starts.</p>
<p style="margin:0;"><span style="color:#3572A5;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">Python</span></p>
</div>
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878z"/></svg><a href="https://github.com/pe1hvh/meshcore_py" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">meshcore_py</a><span style="font-size:11px;border:1px solid #d0d7de;padding:1px 6px;margin-left:8px;color:#57606a;vertical-align:middle;">fork</span></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">Python bindings for meshcore</p>
<p style="margin:0;"></p>
</div>
<div style="clear:both"></div>
</div>


<img src="cards/header-morse-en-cw.svg" width="812"/>

<div style="overflow:hidden;margin-bottom:8px;">
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/configurable_morse_code_interface" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">configurable_morse_code_interface</a></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">DIY Configurable USB/HID Morse Code Interface for LWCO, PCWFistcheck, VBand etc.</p>
<p style="margin:0;"><span style="color:#f34b7d;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">C++</span><svg height="14" viewBox="0 0 16 16" width="14" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.873 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/></svg><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">2</span><svg height="14" viewBox="0 0 16 16" width="14" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878z"/></svg><span style="font-size:12px;color:#57606a;vertical-align:middle;">3</span></p>
</div>
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/VBand_interface" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">VBand_interface</a></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">VBand Interface for the Seeeduino XIAO</p>
<p style="margin:0;"><span style="color:#f34b7d;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">C++</span></p>
</div>
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/cw_lcwo_pcw_interface" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">cw_lcwo_pcw_interface</a></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">CW interface for using it with Learn CW online and PCWFistCheck</p>
<p style="margin:0;"><span style="color:#f34b7d;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">C++</span></p>
</div>
<div style="clear:both"></div>
</div>


<img src="cards/header-arduino.svg" width="812"/>

<div style="overflow:hidden;margin-bottom:8px;">
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/frequency-generator" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">frequency-generator</a></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">10kHz to 225MHz VFO / RF Generator</p>
<p style="margin:0;"><span style="color:#555555;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">C</span><svg height="14" viewBox="0 0 16 16" width="14" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.873 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/></svg><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">1</span></p>
</div>
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/platformIO2arduinoIDE" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">platformIO2arduinoIDE</a></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">Convert PlatformIO code to Arduino sketches</p>
<p style="margin:0;"><span style="color:#89e051;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">Shell</span><svg height="14" viewBox="0 0 16 16" width="14" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.873 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/></svg><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">1</span></p>
</div>
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/measure_bouncing" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">measure_bouncing</a></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">Simple test program for measure bouncing</p>
<p style="margin:0;"><span style="color:#f34b7d;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">C++</span></p>
</div>
<div style="clear:both"></div>
</div>


<img src="cards/header-google-timeline.svg" width="812"/>

<div style="overflow:hidden;margin-bottom:8px;">
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878z"/></svg><a href="https://github.com/pe1hvh/Timeline-GPX-Exporter" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">Timeline-GPX-Exporter</a><span style="font-size:11px;border:1px solid #d0d7de;padding:1px 6px;margin-left:8px;color:#57606a;vertical-align:middle;">fork</span></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">Convert Google timeline new JSON format to daily GPX files</p>
<p style="margin:0;"><span style="color:#3572A5;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">Python</span></p>
</div>
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/TimeLine2MariaDB" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">TimeLine2MariaDB</a></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">Tijdlijn van Google Android telefoon omzetten naar MariaDB</p>
<p style="margin:0;"><span style="color:#3572A5;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">Python</span></p>
</div>
<div style="clear:both"></div>
</div>


<img src="cards/header-other.svg" width="812"/>

<div style="overflow:hidden;margin-bottom:8px;">
<div style="float:left;width:48%;margin:0 1% 8px 1%;border:1px solid #d0d7de;padding:16px;overflow:hidden;">
<div style="margin-bottom:8px;"><svg height="16" viewBox="0 0 16 16" width="16" aria-hidden="true" style="display:inline-block;vertical-align:middle;fill:#57606a;margin-right:4px;"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"/></svg><a href="https://github.com/pe1hvh/javaPolar" style="font-weight:600;font-size:13px;color:#0969da;text-decoration:none;vertical-align:middle;">javaPolar</a></div>
<p style="font-size:12px;color:#57606a;margin:0 0 12px 0;">Automates Polar Flow training data export and upload using Selenium WebDriver.</p>
<p style="margin:0;"><span style="color:#8f8f8f;font-size:14px;vertical-align:middle;margin-right:4px;">&#9679;</span><span style="font-size:12px;color:#57606a;vertical-align:middle;margin-right:14px;">Java</span></p>
</div>
<div style="clear:both"></div>
</div>

<!-- REPOS_END -->

---

## Interests

`MeshCore / LoRa` &nbsp;·&nbsp; `BLE / BlueZ` &nbsp;·&nbsp; `HF amateur radio` &nbsp;·&nbsp; `CW / Morse` &nbsp;·&nbsp; `ESP32 / Arduino` &nbsp;·&nbsp; `Python` &nbsp;·&nbsp; `PHP` &nbsp;·&nbsp; `NoodNet`
