<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="AAAA4"/>
        <attribute name="authors" value="Sumat"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 11:56:13 AM"/>
        <attribute name="created" value="U3VtYXQ7VE9OR19UT05HX1NIVVI7MjU2OC0wNy0yMDsxMDoyMjowMiBQTTsyOTM5"/>
        <attribute name="edited" value="U3VtYXQ7VE9OR19UT05HX1NIVVI7MjU2OC0wNy0yMDsxMDozMDoyMSBQTTsxOzMwNDc="/>
        <attribute name="edited" value="cHVrYW47REVTS1RPUC0yQ04zQTM2OzIwMjUtMDctMjI7MTE6NTY6MTMgQU07MjsyOTE3"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, year" type="Real" array="False" size=""/>
            <declare name="i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <for variable="i" start="1" end="year" direction="inc" step="1">
                <assign variable="money" expression="money*(1+(interest/100))"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;: &quot; &amp; money" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>