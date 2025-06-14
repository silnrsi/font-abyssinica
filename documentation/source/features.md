---
title: Abyssinica SIL - Font Features
fontversion: 2.300
---

Abyssinica SIL is a TrueType font with smart font capabilities added using the OpenType font technology. The Ethiopic script does not require much rendering except for some combining marks for gemination and vowel length. However, there are some glyph variations for the Ethiopic script. Some applications let the user control certain features such as Character Variants to turn on the rendering of variant characters. However, at this point, most applications do not make use of those features so another solution is needed to show the variant characters. [TypeTuner](https://typetunerweb.languagetechnology.org/ttw/fonts2go.cgi) creates tuned fonts that use the variant glyph in place of the standard glyph. TypeTuner also provides the ability to turn on support for the Sebat Bet Gurage and Gumuz languages variants.

See [Using Font Features](https://software.sil.org/fonts/features/). Although that page is not targeted at Ethiopic support, it does provide a comprehensive list of applications that make full use of the OpenType font technology.

## Advanced typographic capabilities

This font supports various advanced typographic capabilities using the OpenType font technology. 

* Auto placement of diacritics on Ethiopic syllables only (not on Latin characters)
* Kerning of almost 200 pairs of Ethiopic syllables
* OpenType Character Variants (alternately-designed glyphs are also provided for a number of characters for use in particular contexts) 
* OpenType support for the Sebat Bet Gurage [sgw] and Gumuz [guk] languages

These capabilities are available in any application that supports OpenType technology, though this requires applications that provide a sufficient level of support for OpenType Character Variant features. 

A sample of diacritic placement and kerning is shown below:

![Abyssinica SIL Sample - Diacritic placement and Kerning](assets/images/Abyssinica_SampleDiacKern.png){.fullsize}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/abyssinica/wp-content/uploads/sites/26/2016/02/Abyssinica_SampleDiacKern.png -->
<figcaption>Abyssinica SIL Sample - Diacritic placement and Kerning</figcaption>


This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Abyssinica SIL as a web font see [Abyssinica SIL Webfont Example](../web/AbyssinicaSIL-webfont-example.html). For detailed information see [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts).

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*


## Customizing with TypeTuner

For applications that do not make use of the OpenType Character Variant features, you can now download fonts customized with the variant glyphs you choose. Read the [Font Features](features.md) page, visit [TypeTuner Web](https://typetunerweb.languagetechnology.org/ttw/fonts2go.cgi), then to choose the variants and download your font.


## Complete feature list

There are some Ethiopic character shape differences in different Ethiopian languages. These can be accessed by using OpenType Character Variants or language support for Sebat Bet Gurage and Gumuz languages. The documents below can be downloaded in order to see all the user-selectable font features that are available in the font. The feature names, feature ids, settings and examples are provided. 


### Language 

<span class='affects'>Affects: U+124A, U+124D, U+1298..U+129F, U+12B2, U+12B5, U+12C2, U+12C5, U+1312, U+1313, U+1315, U+1381, U+1385, U+138D </span>

Language | Sample | Feature setting
------------- | --------------- | ------------- 
default | <span class='abyssinica-R normal'>ቊ ቍ ኘ ኙ ኚ ኛ ኜ ኝ ኞ ኟ ኲ ኵ ዂ ዅ ጒ ጓ ጕ ᎁ ᎅ ᎍ </span> | 
Sebat Bet Gurage (sgw) | <span class='abyssinica-R normal' lang='sgw'><font color="red">ቊ ቍ </font>ኘ ኙ ኚ ኛ ኜ ኝ ኞ ኟ <font color="red">ኲ ኵ ዂ ዅ ጒ ጓ ጕ ᎁ ᎅ ᎍ </font> </span>| `lang=sgw`
Gumuz (guk) |<span class='abyssinica-R normal' lang='guk'>ቊ ቍ<font color="red"> ኘ ኙ ኚ ኛ ኜ ኝ ኞ ኟ </font>ኲ ኵ ዂ ዅ ጒ ጓ ጕ ᎁ ᎅ ᎍ </span>| `lang=guk`


### Character variants

#### Punctuation

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Ethiopic-style | <span class='abyssinica-R normal'>! $ % * + / 0 1 2 3 4 5 6 7 8 9 = ? ¡ © « ² ³ ¹ » × ‘ ’ “ ” ‹ › ⁰ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ €</span> | `cv01=0`
Latin-style | <span class='abyssinica-R normal' style='font-feature-settings: "cv01" 1'>! $ % * + / 0 1 2 3 4 5 6 7 8 9 = ? ¡ © « ² ³ ¹ » × ‘ ’ “ ” ‹ › ⁰ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ €</span> | `cv01=1`

#### Ethiopic digits

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>፩ ፪፫ ፫፬፭ ፺፻፼፻፼፩፼፩፪</span> | `cv02=0`
Connected | <span class='abyssinica-R normal' style='font-feature-settings: "cv02" 1'>፩ ፪፫ ፫፬፭ ፺፻፼፻፼፩፼፩፪</span> | `cv02=1`

#### mwa alternates

<span class='affects'>Affects: U+121F</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ሟ</span> | `cv04=0`
Alternate-1 | <span class='abyssinica-R normal' style='font-feature-settings: "cv04" 1'>ሟ¹</span> | `cv04=1`
Alternate-2 | <span class='abyssinica-R normal' style='font-feature-settings: "cv04" 2'>ሟ²</span> | `cv04=2`

#### rwa alternate 

<span class='affects'>Affects: U+122F</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ሯ</span> | `cv05=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv05" 1'>ሯ²</span> | `cv05=1`

#### xoa alternate 

<span class='affects'>Affects: U+1287</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ኇ</span> | `cv17=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv17" 1'>ኇ</span> | `cv17=1`

#### xwa alternates 

<span class='affects'>Affects: U+1288..U+128D</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ኈ   ኊ ኋ ኌ ኍ</span> | `cv18=0`
Handwriting | <span class='abyssinica-R normal' style='font-feature-settings: "cv18" 1'>ኈ   ኊ ኋ ኌ ኍ</span> | `cv18=1`

#### nwa alternate 

<span class='affects'>Affects: U+1297</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ኗ</span> | `cv19=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv19" 1'>ኗ¹</span> | `cv19=1`

#### nya alternates 

<span class='affects'>Affects: U+1298..U+129E</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ኘ ኙ ኚ ኛ ኜ ኝ ኞ</span> | `cv20=0`
Disconnected | <span class='abyssinica-R normal' style='font-feature-settings: "cv20" 1'>ኘ ኙ ኚ ኛ ኜ ኝ ኞ³</span> | `cv20=1`

#### nywa alternates 

<span class='affects'>Affects: U+129F</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ኟ</span> | `cv21=0`
Disconnected | <span class='abyssinica-R normal' style='font-feature-settings: "cv21" 1'>ኟ³</span> | `cv21=1`
Cohen | <span class='abyssinica-R normal' style='font-feature-settings: "cv21" 2'>ኟ²</span> | `cv21=2`

#### kxwaa alternate 

<span class='affects'>Affects: U+12C3</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ዃ</span> | `cv26=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv26" 1'>ዃ²</span> | `cv26=1`

#### zha alternates 

<span class='affects'>Affects: U+12E0..U+12E6</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ዠ ዡ ዢ ዣ ዤ ዥ ዦ</span> | `cv31=0`
Cohen | <span class='abyssinica-R normal' style='font-feature-settings: "cv31" 1'>ዠ ዡ ዢ ዣ ዤ <font color="red">ዥ</font> ዦ⁴</span> | `cv31=1`
Chaine | <span class='abyssinica-R normal' style='font-feature-settings: "cv31" 2'><font color="red">ዠ ዡ</font> ዢ <font color="red">ዣ ዤ ዥ ዦ</font>⁵</span> | `cv31=2`

#### dda alternates 

<span class='affects'>Affects: U+12F8..U+12FE</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ዸ ዹ ዺ ዻ ዼ ዽ ዾ</span> | `cv32=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv32" 1'>ዸ ዹ ዺ ዻ ዼ ዽ ዾ⁶</span> | `cv32=1`

#### gwaa alternates 

<span class='affects'>Affects: U+1313</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ጓ</span> | `cv40=0`
Sebat Bet | <span class='abyssinica-R normal' style='font-feature-settings: "cv40" 1'>ጓ⁷</span> | `cv40=1`
Alone Stokes | <span class='abyssinica-R normal' style='font-feature-settings: "cv40" 2'>ጓ⁸</span> | `cv40=2`

#### gga alternates 

<span class='affects'>Affects: U+1318..U+131E</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ጘ ጙ ጚ ጛ ጜ ጝ ጞ</span> | `cv41=0`
Disconnected | <span class='abyssinica-R normal' style='font-feature-settings: "cv41" 1'>ጘ ጙ ጚ ጛ ጜ ጝ ጞ⁹</span> | `cv41=1`

#### ggwaa alternate 

<span class='affects'>Affects: U+131F</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ጟ</span> | `cv42=0`
Disconnected | <span class='abyssinica-R normal' style='font-feature-settings: "cv42" 1'>ጟ⁹</span> | `cv42=1`

#### phe alternate 

<span class='affects'>Affects: U+1335</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ጵ</span> | `cv45=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv45" 1'>ጵ¹⁰</span> | `cv45=1`

#### tswa alternate 

<span class='affects'>Affects: U+133F</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ጿ</span> | `cv46=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv46" 1'>ጿ</span> | `cv46=1`

#### fwa alternates 

<span class='affects'>Affects: U+134F</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ፏ</span> | `cv48=0`
Cohen-1 | <span class='abyssinica-R normal' style='font-feature-settings: "cv48" 1'>ፏ¹</span> | `cv48=1`
Cohen-2 | <span class='abyssinica-R normal' style='font-feature-settings: "cv48" 2'>ፏ¹</span> | `cv48=2`

#### rya alternate 

<span class='affects'>Affects: U+1358</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ፘ</span> | `cv49=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv49" 1'>ፘ²</span> | `cv49=1`

#### mya alternate 

<span class='affects'>Affects: U+1359</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ፙ</span> | `cv50=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv50" 1'>ፙ²</span> | `cv50=1`

#### mwi alternates 

<span class='affects'>Affects: U+1381</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ᎁ</span> | `cv60=0`
Sebat Bet | <span class='abyssinica-R normal' style='font-feature-settings: "cv60" 1'>ᎁ⁷</span> | `cv60=1`
Leslau | <span class='abyssinica-R normal' style='font-feature-settings: "cv60" 2'>ᎁ¹¹</span> | `cv60=2`

#### mwe alternates 

<span class='affects'>Affects: U+1383</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ᎃ</span> | `cv61=0`
Sebat Bet | <span class='abyssinica-R normal' style='font-feature-settings: "cv61" 1'>ᎃ⁷</span> | `cv61=1`
Leslau | <span class='abyssinica-R normal' style='font-feature-settings: "cv61" 2'>ᎃ¹¹</span> | `cv61=2`

#### bwe alternate 

<span class='affects'>Affects: U+1387</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ᎇ</span> | `cv62=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv62" 1'>ᎇ¹¹</span> | `cv62=1`

#### fwee alternate 

<span class='affects'>Affects: U+138A</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ᎊ</span> | `cv63=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv63" 1'>ᎊ¹¹</span> | `cv63=1`

#### fwe alternate 

<span class='affects'>Affects: U+138B</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ᎋ</span> | `cv64=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv64" 1'>ᎋ¹¹</span> | `cv64=1`

#### pwe alternate 

<span class='affects'>Affects: U+138F</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ᎏ</span> | `cv65=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv65" 1'>ᎏ¹¹</span> | `cv65=1`

#### ggwa alternates 

<span class='affects'>Affects: U+2D93..U+2D96</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ⶓ ⶔ ⶕ ⶖ</span> | `cv70=0`
Disconnected | <span class='abyssinica-R normal' style='font-feature-settings: "cv70" 1'>ⶓ ⶔ ⶕ ⶖ⁹</span> | `cv70=1`

#### 3rd form alternates

<span class='affects'>Affects: U+124A U+12B2 U+12C2 U+1312 U+1385 U+138D</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ቊ ኲ ዂ ጒ ᎅ ᎍ</span> | `cv80=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv80" 1'>ቊ ኲ ዂ ጒ ᎅ ᎍ⁷</span> | `cv80=1`

#### 6th form alternates

<span class='affects'>Affects: U+124D U+12B5 U+12C5 U+1315</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
Standard | <span class='abyssinica-R normal'>ቍ ኵ ዅ ጕ</span> | `cv85=0`
Alternate | <span class='abyssinica-R normal' style='font-feature-settings: "cv85" 1'>ቍ ኵ ዅ ጕ⁷</span> | `cv85=1`

### Ligatures

#### gzi ligature

<span class='affects'>Affects: U+130D U+200D U+12DA</span>

Feature | Sample | Feature setting
------------- | --------------- | ------------- 
No Joiner | <span class='abyssinica-R normal'>&#x130D;&#x12DA;</span> | U+130D U+12DA
Using ZWJ | <span class='abyssinica-R normal'>&#x130D;&#x200D;&#x12DA;</span></span> | U+130D U+200D U+12DA


## References

Alone, John Philip Herbert Mackenzie. 1946 (Fourth edition). *The Alone-Stokes Short Manual of the Amharic Language (with vocabularies).* Macmillan and Co. Limited: London.

Chaîne, Marius. 1907. *Grammaire éthiopienne.* Imprimerie catholique. Beyrouth.

Cohen, Marcel. 1970 Seconde edition. *Traité de langue amharique (Abyssinie).* Institut d'ethnologie: Paris.

Leslau, Wolf. 1966. *Ethiopians Speak: Studies in Cultural Background. Part 2: Chaha.* University of California Publication. Near Eastern Studies, Volume 9. University of California Press: Berkeley

Praetorius, Franz. 1955. *Aethiopische Grammatik mit Paradigmen, Litteratur, Chrestomathie und Glossar.* Frederick Ungar Publishing Co. New York.

¹Chaîne (p 3), Cohen (table 2) 
²Cohen (table 2) 
³Gumuz language preference 
⁴Alone-Stokes, Chaîne (p 3), Cohen (table 1) 
⁵Chaîne (p 3) 
⁶Archaic Oromo language preference 
⁷Sebat Bet language preference
⁸Alone-Stokes (inside back cover) 
⁹Bilen language preference
¹⁰Praetorius (p 6)
¹¹Leslau


<!-- PRODUCT SITE ONLY
[font id='abyssinica' face='AbyssinicaSIL-Regular' size='150%']
-->
