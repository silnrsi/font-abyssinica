<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>
 
<xsl:output method="html" encoding="utf-8"/>
<xsl:template match="strings"> 
	<html>
	
	<head>
	<title><xsl:value-of select="@label"/></title>
	<style type="text/css">
		@font-face { font-family: AbyssinicaTest;  src: url(AbyssinicaSIL-R.woff); }
		td.str { font-family: "AbyssinicaTest", "Times New Roman", Serif;  font-size: 200%; direction: ltr; text-align: left;}
	</style>
	</head>

	<body>
	<h1><xsl:value-of select="@label"/></h1>
	<table border="0" cellpadding="3" cellspacing="3" style="border-collapse: collapse" bordercolor="#111111">

	<xsl:for-each select="//string">
		  <tr>
		    <td><xsl:value-of select="@label"/></td>
		    <td class="str">
<!-- Add style string if there is a feats attribute -->
<xsl:if test="@feats">
		    		<xsl:attribute name="style">-moz-font-feature-settings: <xsl:value-of select="@feats"/></xsl:attribute>
</xsl:if>
<!-- If there is a "text" element then assume the data is there; otherwise the whole node is data -->
<xsl:choose>
	<xsl:when test="text">
		    	<xsl:value-of select="text"/>
	</xsl:when>
	<xsl:otherwise>
				<xsl:value-of select="."/>
	</xsl:otherwise>
</xsl:choose>
		    </td>
<!-- Add column containing feature info -->
		    <td><xsl:value-of select="@feats"/></td>
<!-- If there is a "text" element, then there may also be a "comment", so put that in the next col -->		    
<xsl:if test="text">
		    <td><xsl:value-of select="comment"/></td>
</xsl:if>
		  </tr>
	</xsl:for-each>

	</table>
	<br/>
	</body>
	
	</html>

</xsl:template>
</xsl:stylesheet>
