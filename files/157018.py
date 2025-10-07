<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_test1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:32:48 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6NTA6NDggUE07MjU4MQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MzI6NDggUE07MjsyNjkx"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="a, ap, c, cp, total, money" type="Integer" array="False" size=""/>
            <assign variable="ap" expression="189"/>
            <assign variable="cp" expression="120"/>
            <output expression="&quot;Price list: &quot;" newline="True"/>
            <output expression="&quot; - Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot; - Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <input variable="c"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="a"/>
            <assign variable="total" expression="(c*cp)+(a*ap)"/>
            <output expression="&quot;You ordered &quot;&amp; c &amp;&quot; children and &quot; &amp; a &amp; &quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price:&quot; &amp; total &amp; &quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>