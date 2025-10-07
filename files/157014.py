<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="t1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:22:57 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6NTg6NTMgUE07MjU4NQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MjI6NTcgUE07OTsyNjk3"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="x, y, a, c" type="Integer" array="False" size=""/>
            <assign variable="a" expression="189"/>
            <assign variable="c" expression="120"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <input variable="y"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="x"/>
            <declare name="total" type="Integer" array="False" size=""/>
            <assign variable="total" expression="(y*120)+(x*189)"/>
            <output expression="&quot;You ordered &quot;&amp; y &amp;&quot; children&quot;&amp;&quot; and &quot;&amp; x &amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price:&quot;&amp; total &amp;&quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>