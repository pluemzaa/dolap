<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test1_lab3"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 06:28:35 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MTA6MDggUE07MjU3NQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6Mjg6MzUgUE07MjsyNjk0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <declare name="Total, Child, Adult" type="Integer" array="False" size=""/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <input variable="Child"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="Adult"/>
            <assign variable="Total" expression="(Child * 120) + (Adult * 189)"/>
            <output expression="&quot;You ordered &quot; &amp; Child &amp; &quot; children and &quot; &amp; Adult &amp; &quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price:&quot; &amp;Total&amp; &quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>