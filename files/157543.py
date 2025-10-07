<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="AAAA4"/>
        <attribute name="authors" value="Sumat"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 10:30:21 PM"/>
        <attribute name="created" value="U3VtYXQ7VE9OR19UT05HX1NIVVI7MjU2OC0wNy0yMDsxMDoyMjowMiBQTTsyOTM5"/>
        <attribute name="edited" value="U3VtYXQ7VE9OR19UT05HX1NIVVI7MjU2OC0wNy0yMDsxMDozMDoyMSBQTTsxOzMwNDc="/>
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