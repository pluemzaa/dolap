<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4444444444"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 03:05:55 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xODsxMjozMjoyMyBQTTsyNTQz"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xOTswMzowNTo1NSBQTTszOzI2NTk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="iy, lo" type="Integer" array="False" size=""/>
            <declare name="in, im, ink" type="Real" array="False" size=""/>
            <assign variable="lo" expression="1"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="im"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="in"/>
            <assign variable="ink" expression="in/100"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="iy"/>
            <while expression="lo&lt;=iy">
                <assign variable="im" expression="im*(1+ink)"/>
                <output expression="&quot;Year &quot;&amp;lo&amp;&quot;: &quot;&amp;im" newline="True"/>
                <assign variable="lo" expression="lo+1"/>
            </while>
        </body>
    </function>
</flowgorithm>