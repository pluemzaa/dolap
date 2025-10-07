<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:12:18 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDE6NTc6MjcgUE07MjU4Mw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MTI6MTggUE07MzsyNjg1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="c, a, total" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List: &quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <input variable="c"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="a"/>
            <assign variable="total" expression="(c*120)+(a*189)"/>
            <output expression="&quot;You ordered &quot;&amp;c&amp;&quot; children and &quot;&amp;a&amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>