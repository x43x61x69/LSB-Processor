#LSB Processor

[![Author](https://img.shields.io/badge/Author-Zhi--Wei_Cai-red.svg?style=flat-square)](http://vox.vg/)  ![Build](https://img.shields.io/badge/Build-v0.1-green.svg?style=flat-square)  ![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)

**LSB Processor** is a tool inspired by a challenge created by [**ANSSI**][ANSSI] (*Agence nationale de la sécurité des systèmes d'information*), a French intelligence agency.

The challenge manipulated the "**Least Significant Bits**" (LSB) technique to hide information in plain sight.

> *Original image file is provided as `sample.png` in the `test` folder.*

An animation of the original and the extracted ANSSI images by the LSB Processor:

![Demo](demo.gif)

##Usage

```shell
python lsbp.py image_file
```

##Changelog

- **0.1**：Initial release. 

##License

See the `LICENSE` file.

[ANSSI]: http://www.ssi.gouv.fr/