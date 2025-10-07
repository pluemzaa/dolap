<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Dolab4_1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 06:12:40 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6NTA6MDkgUE07MjU4MA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6MTI6NDAgUE07MzsyNjg0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="children, adults, total" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <input variable="children"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="adults"/>
            <assign variable="total" expression="(children * 120) + (adults * 189)"/>
            <output expression="&quot;You ordered &quot; &amp; children &amp; &quot; children&quot; &amp; &quot; and &quot;&amp; adults &amp; &quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>