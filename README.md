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

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {
  'primaryColor': '#ffffff',
  'primaryBorderColor': '#d0d7de',
  'primaryTextColor': '#24292f',
  'lineColor': 'transparent',
  'fontSize': '13px'
}}}%%
flowchart TD
    meshcore_observer"`**meshcore-observer**
A standalone daemon that reads JSON archive files produ
🔵 Python`"
    meshcore_bridge"`**meshcore-bridge**
MeshCore Channel Bridge — selectively relays messages b
🔵 Python`"
    meshcore_gui"`**meshcore-gui**
Native desktop GUI for MeshCore mesh network devices vi
🔵 Python  ⭐ 13  ⑂ 1`"
    meshcore_ble_connect"`**meshcore-ble-connect**
Standalone BLE Connection Manager — ensures a BLE bond 
🔵 Python`"
    meshcore_py"`**meshcore_py**
Python bindings for meshcore
`"
    R0[" "]
    R0 ~~~ meshcore_observer
    R0 ~~~ meshcore_bridge
    style R0 fill:transparent,stroke:transparent,color:transparent,width:0px,height:0px
    R1[" "]
    R1 ~~~ meshcore_gui
    R1 ~~~ meshcore_ble_connect
    R0 ~~~ R1
    style R1 fill:transparent,stroke:transparent,color:transparent,width:0px,height:0px
    R2[" "]
    R2 ~~~ meshcore_py
    R1 ~~~ R2
    style R2 fill:transparent,stroke:transparent,color:transparent,width:0px,height:0px
    click meshcore_observer href "https://github.com/pe1hvh/meshcore-observer" _blank
    click meshcore_bridge href "https://github.com/pe1hvh/meshcore-bridge" _blank
    click meshcore_gui href "https://github.com/pe1hvh/meshcore-gui" _blank
    click meshcore_ble_connect href "https://github.com/pe1hvh/meshcore-ble-connect" _blank
    click meshcore_py href "https://github.com/pe1hvh/meshcore_py" _blank
    style meshcore_observer fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
    style meshcore_bridge fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
    style meshcore_gui fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
    style meshcore_ble_connect fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
    style meshcore_py fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
```


<img src="cards/header-morse-en-cw.svg" width="812"/>

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {
  'primaryColor': '#ffffff',
  'primaryBorderColor': '#d0d7de',
  'primaryTextColor': '#24292f',
  'lineColor': 'transparent',
  'fontSize': '13px'
}}}%%
flowchart TD
    configurable_morse_code_interface"`**configurable_morse_code_interface**
DIY Configurable USB/HID Morse Code Interface for LWCO,
🔴 C++  ⭐ 2  ⑂ 3`"
    VBand_interface"`**VBand_interface**
VBand Interface for the Seeeduino XIAO
🔴 C++`"
    cw_lcwo_pcw_interface"`**cw_lcwo_pcw_interface**
CW interface for using it with Learn CW online and PCWF
🔴 C++`"
    R0[" "]
    R0 ~~~ configurable_morse_code_interface
    R0 ~~~ VBand_interface
    style R0 fill:transparent,stroke:transparent,color:transparent,width:0px,height:0px
    R1[" "]
    R1 ~~~ cw_lcwo_pcw_interface
    R0 ~~~ R1
    style R1 fill:transparent,stroke:transparent,color:transparent,width:0px,height:0px
    click configurable_morse_code_interface href "https://github.com/pe1hvh/configurable_morse_code_interface" _blank
    click VBand_interface href "https://github.com/pe1hvh/VBand_interface" _blank
    click cw_lcwo_pcw_interface href "https://github.com/pe1hvh/cw_lcwo_pcw_interface" _blank
    style configurable_morse_code_interface fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
    style VBand_interface fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
    style cw_lcwo_pcw_interface fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
```


<img src="cards/header-arduino.svg" width="812"/>

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {
  'primaryColor': '#ffffff',
  'primaryBorderColor': '#d0d7de',
  'primaryTextColor': '#24292f',
  'lineColor': 'transparent',
  'fontSize': '13px'
}}}%%
flowchart TD
    frequency_generator"`**frequency-generator**
10kHz to 225MHz VFO / RF Generator
⚫ C  ⭐ 1`"
    platformIO2arduinoIDE"`**platformIO2arduinoIDE**
Convert PlatformIO code to Arduino sketches
🟢 Shell  ⭐ 1`"
    measure_bouncing"`**measure_bouncing**
Simple test program for measure bouncing
🔴 C++`"
    R0[" "]
    R0 ~~~ frequency_generator
    R0 ~~~ platformIO2arduinoIDE
    style R0 fill:transparent,stroke:transparent,color:transparent,width:0px,height:0px
    R1[" "]
    R1 ~~~ measure_bouncing
    R0 ~~~ R1
    style R1 fill:transparent,stroke:transparent,color:transparent,width:0px,height:0px
    click frequency_generator href "https://github.com/pe1hvh/frequency-generator" _blank
    click platformIO2arduinoIDE href "https://github.com/pe1hvh/platformIO2arduinoIDE" _blank
    click measure_bouncing href "https://github.com/pe1hvh/measure_bouncing" _blank
    style frequency_generator fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
    style platformIO2arduinoIDE fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
    style measure_bouncing fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
```


<img src="cards/header-google-timeline.svg" width="812"/>

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {
  'primaryColor': '#ffffff',
  'primaryBorderColor': '#d0d7de',
  'primaryTextColor': '#24292f',
  'lineColor': 'transparent',
  'fontSize': '13px'
}}}%%
flowchart TD
    Timeline_GPX_Exporter"`**Timeline-GPX-Exporter**
Convert Google timeline new JSON format to daily GPX fi
🔵 Python`"
    TimeLine2MariaDB"`**TimeLine2MariaDB**
Tijdlijn van Google Android telefoon omzetten naar Mari
🔵 Python`"
    R0[" "]
    R0 ~~~ Timeline_GPX_Exporter
    R0 ~~~ TimeLine2MariaDB
    style R0 fill:transparent,stroke:transparent,color:transparent,width:0px,height:0px
    click Timeline_GPX_Exporter href "https://github.com/pe1hvh/Timeline-GPX-Exporter" _blank
    click TimeLine2MariaDB href "https://github.com/pe1hvh/TimeLine2MariaDB" _blank
    style Timeline_GPX_Exporter fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
    style TimeLine2MariaDB fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
```


<img src="cards/header-other.svg" width="812"/>

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {
  'primaryColor': '#ffffff',
  'primaryBorderColor': '#d0d7de',
  'primaryTextColor': '#24292f',
  'lineColor': 'transparent',
  'fontSize': '13px'
}}}%%
flowchart TD
    javaPolar"`**javaPolar**
Automates Polar Flow training data export and upload us
⚪ Java`"
    R0[" "]
    R0 ~~~ javaPolar
    style R0 fill:transparent,stroke:transparent,color:transparent,width:0px,height:0px
    click javaPolar href "https://github.com/pe1hvh/javaPolar" _blank
    style javaPolar fill:#ffffff,stroke:#d0d7de,stroke-width:1px,color:#0969da,text-align:left
```

<!-- REPOS_END -->

---

## Interests

`MeshCore / LoRa` &nbsp;·&nbsp; `BLE / BlueZ` &nbsp;·&nbsp; `HF amateur radio` &nbsp;·&nbsp; `CW / Morse` &nbsp;·&nbsp; `ESP32 / Arduino` &nbsp;·&nbsp; `Python` &nbsp;·&nbsp; `PHP` &nbsp;·&nbsp; `NoodNet`
