---
title: Abyssinica SIL - Frequently Asked Questions
fontversion: 2.200
---

Many questions can be answered by consulting the following FAQ pages. Here are a few sample questions answered in each FAQ:

- [SIL fonts in general](http://software.sil.org/fonts/faq)
    - *How can I type...?*
    - *How can I use font features?*
    - *Will you add support for character...?*
    - *Will you add support for script...?*
    - *WIll you help me...?*

- [The SIL Open Font License (OFL-FAQ)](https://scripts.sil.org/OFL-FAQ_web)
    - *Can I use this font for...?*
    - *Can I modify the font and then include it in...*
    - *If I use the font on a web page do I have to include an acknowledgement?*
    - The full OFL-FAQ.txt is also included in the font package.

Here are a few of the most frequently asked questions specifically regarding Abyssinica SIL:

#### *What is so special about Abyssinica SIL?*
This font is designed to work with two advanced font technologies, Graphite and OpenType. To take advantage of the advanced typographic capabilities of this font, you must be using applications that provide an adequate level of support for Graphite or OpenType. These advanced capabilities provide access to the variant character forms used in some languages.

#### *Do you supply a keyboard to use with Abyssinica SIL?*

[Keyman](https://keyman.com/) is a cross-platform keyboarding system and a number of Ethiopic keyboards are available:

- [SIL Power-G Ethiopic keyboard](https://keyman.com/keyboards/sil_ethiopic_power_g)
- [SIL Ethiopic keyboard](https://keyman.com/keyboards/sil_ethiopic)
- [GFF Blin Keyboard](https://keyman.com/keyboards/gff_blin)
- [GFF Ge'ez Keyboard](https://keyman.com/keyboards/gff_geez)
- [Amharic keyboard](https://keyman.com/keyboards/gff_amharic)
- [GFF Tigrinya-Ethiopia Keyboard](https://keyman.com/keyboards/gff_tigrinya_ethiopia)
- [GFF Tigrinya-Eritrean Keyboard](https://keyman.com/keyboards/gff_tigrinya_eritrea)

Various other means may be available for different operating-system platforms to create additional input methods. For instance, Windows (Vista and above) provides an Ethiopic IME. 

#### *My language uses variant forms of some Ethiopic characters. How do I type these using the Abyssinica SIL font? How do I use features?*

You should type the character the same way you would type the standard form of the character. Then, you need to select the variants to be displayed. If your application supports Graphite or the OpenType Character Variant features, you can use these to access the font features built into the font. See [Font Features](features.md) page for more details.

If your application does not support Graphite features or the OpenType Character Variants, you can use TypeTunerWeb to customize the font with the variants you require. See [Font Features](features.md) page for more details. 

#### *Why did you remove the Stylistic Sets from ver. 2.000 of the Abyssinica SIL font?*

Originally we added the Stylistic Sets because there was not a good solution for accessing the glyph variants in the font. At one point we also tried encoding them in the Private Use Area (PUA). PUA characters have now almost all been unencoded since the characters are now either encoded in Unicode or the variants are available through **Character Variants**. The Stylistic Sets were implemented inconsistently, and because of that we chose to remove them rather than attempt to fix them. If you still wish to use a font with Stylistic Sets, ver. 1.500 is still available on the [Previous Versions](versions.md) page.

#### *I have a copy of the **SIL Abyssinica** font. Can you tell me how this differs from **Abyssinica SIL**?*

It is best to upgrade to **Abyssinica SIL**. **SIL Abyssinica** (and **SIL Abyssinica U** and **SIL Abyssinica G**) was an early, unreleased version of **Abyssinica SIL**. Although a Unicode font, it only supported Unicode 3.0 and thus had a number of PUA characters in it which have since been added to Unicode 4.1 and 6.0. You should convert your data to Unicode 6.0 and use **Abyssinica SIL**. A mapping file to convert your data from PUA to Unicode 6.0 is available here: [sil-pua-unicode](https://github.com/silnrsi/wsresources/tree/master/scripts/Ethi/mappings/sil-pua-unicode). If you do not convert your data to official Unicode codepoints you will never be able to use another Ethiopic font because those are **Private** codepoints and other fonts do not support them.

#### *You have characters which are encoded in the PUA area. Is there any likelihood that these will ever be in Unicode? If so, will you update Abyssinica SIL?*

Version 1.500 incorporated all characters that are in Unicode 6.0. 

With version 2.000 we removed almost all of the PUA characters in the font because they are either available through their official Unicode codepoints or through the Character Variants.

#### *I would like to bundle Abyssinica SIL with my application - can I?*

The [SIL Open Font License](http://scripts.sil.org/OFL) allows bundling with applications, even commercial ones, with some restrictions.

