<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4.1"/>
        <attribute name="authors" value="asus"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:26:11 PM"/>
        <attribute name="created" value="YXN1cztMQVBUT1AtNzM3TDlPSFA7MjAyNS0wNy0xNjswMjowNjo0OSBQTTsyNzY2"/>
        <attribute name="edited" value="YXN1cztMQVBUT1AtNzM3TDlPSFA7MjAyNS0wNy0xNjswMjoyNjoxMSBQTTszOzI4Njc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="c, a, total, cp, ap" type="Integer" array="False" size=""/>
            <assign variable="cp" expression="120"/>
            <assign variable="ap" expression="189"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <input variable="c"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="a"/>
            <assign variable="total" expression="(c*cp)+(a*ap)"/>
            <output expression="&quot;You ordered &quot; &amp;c&amp;&quot; children and &quot;&amp;a&amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>